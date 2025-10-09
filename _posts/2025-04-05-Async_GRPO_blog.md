---
layout: post
title: Async-GRPO - Open, Fast, and Performant
date: 2025-04-05
image:  'https://hackmd.io/_uploads/HJrSol0ake.svg'
description: Introducing Async-GRPO - an open-source library for scalable reinforcement learning with 42% efficiency gains over VERL and 11x over TRL for GRPO training.
---

Written by Aldo Pareja, Mustafa Eyceoz

## Introducing Async-GRPO

With the increasing popularity of reasoning and long-context models, the generation lengths required for reinforcement learning tasks have expanded greatly, creating a significant bottleneck—especially for online policy optimization methods like Group Relative Policy Optimization (GRPO) that require a large amount of live rollouts. Current available implementations of GRPO often lead to high GPU idle times due to the synchronous nature of alternating between generation and training processes, as well as inflexibility in resource task allocation. This often leads to math and reasoning experiments taking far too long and being overly reduced to toy scenarios, and adds further difficulty when trying to scale up.

To address these challenges, we are excited to introduce [Async-GRPO](https://github.com/Red-Hat-AI-Innovation-Team/async-grpo), a new library designed to enhance flexibility and scalability for reinforcement learning tasks. With Async-GRPO, practitioners can now independently scale and schedule training and inference across all available GPUs, regardless of node configurations. This asynchronous approach covers the three core stages of GRPO (Actor Rollout Generation, Reference Log Probabilities Inference, and Actor Training) simultaneously. leaving minimal GPU idle time and allowing for optimal resource allocation to eliminate bottlenecks on a per-scenario basis.


![async10.drawio](https://hackmd.io/_uploads/HJrSol0ake.svg)



## Top-Tier Efficiency with Performance to Match

We ran a comparison between Async-GRPO and other popular open source libraries with GRPO implementations, Huggingface’s [TRL](https://github.com/huggingface/trl/tree/main) and ByteDance’s [VERL](https://github.com/volcengine/verl). To measure the efficiency of the libraries, we used a consistent scenario that shows real math improvement on reasoning models: reproducing [DeepScaleR](https://github.com/agentica-project/deepscaler?tab=readme-ov-file#evaluation)’s use of GRPO to improve the math performance of [DeepSeek-R1-Distill-Qwen-1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B).

We used the same model, the same data, the same hardware (2 nodes, each 8xH100, connected with RDMA), same reward function (DeepScaleR reward function), max sequence length (8192), sampling parameters, training hyperparameters, etc.

We also ensured that each library was set up optimally, e.g. making sure we were maximizing TRL’s GRPOTrainer GPU memory and utilization and minimizing gradient accumulation, and using a separate TRL vLLM instance for best generation throughput.

With a consistent 128 samples per step, we measure the following time-per-step (s):
![Steps per Hour (Higher is Better)](https://hackmd.io/_uploads/Sye2ex0TJl.svg)

In the 8-rollout scenario, Async-GRPO sees a 42.4% efficiency gain over VERL (v0.2.0.post2), and an 11x gain over TRL (v0.16.0). In the 32-rollout scenario, Async-GRPO sees a 28.8% gain over VERL, and a 12.5x gain over TRL. All testing was done with vLLM for rollout generation (VERL has also recently added a preview for SGLang support in single-node settings), and all results were gathered using released library versions (TRL has an open PR for worker GPU co-location that is expected to 2x their current throughput).

Of course, speed only matters when the performance results are also there. With the same scenario, we demonstrate that the Async-GRPO library is providing the same or better model-improvement, and at the same rate.

![experiment_plots](https://hackmd.io/_uploads/Hk3r2J06ke.svg)

Our reward increase and initial average sample length decrease is fully consistent with DeepScaleR's findings at 8k max sequence length in their [blog](https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e2), with average AIME 2024 Pass@1 scores also aligned.

## Architecture Overview

**At its core, Async-GRPO is a distributed system built on Ray.** We divide responsibilities among specialized workers (training and two types of inference) and run them all in parallel, removing traditional “stop-and-wait” bottlenecks.

---

#### Key Components

1. **Training Workers**  
   - **What They Do:** Handle the main model-updating loop.  
   - **How They Do It:** Each training worker runs a copy of the model wrapped in FSDP to efficiently handle large models in distributed setups. They communicate asynchronously with inference workers to fetch rollouts (the sequences used for reinforcement learning updates) and the log probabilities of these rollouts.

2. **Generation Workers**  
   - **What They Do:** Generate new rollouts (sequences) using vLLM.  
   - **Why It Matters:** The system can spin up as many of these as needed to keep training busy. Meanwhile, each worker can internally handle multiple generation requests at once (async generation).

3. **Logprob Workers**  
   - **What They Do:** Compute log probabilities (reference policy scores) for the tokens generated by the actor.  
   - **Why It Matters:** This information is crucial for GRPO’s loss calculation and advantage estimates. Like generation workers, these run independently and can be scaled as needed.

---

#### How Everything Ties Together

1. **Ray for Distributed Management**  
   - Ray coordinates all workers—launching them, monitoring them, and enabling message-passing. This lets Async-GRPO smoothly operate across multiple nodes and GPUs with minimal manual setup.

2. **Experience Batcher**  
   - Sits between training workers and inference workers.  
   - Collects or “batches” sample requests from training, sends them to the inference workers (both generation and logprob), and returns the processed results.  
   - Ensures that no GPU resources sit idle by efficiently packing requests so workers stay busy.

3. **Weight Updates**  
   - Training workers share updated weights with inference workers to keep everyone on the same page.  
   - Currently uses Ray Object Store for these updates (future updates will streamline this via PyNCCL for better performance).

---

#### GRPO-Specific Details

1. **Rollouts + Rewards**  
   - Generation workers produce candidate sequences (“rollouts”) and compute a reward (e.g., from math-verify).  
   - Each sample’s reward is normalized and stored so we can compare how good each rollout was.

2. **Reference Log Probs**  
   - Logprob workers compute the reference policy’s log probabilities over tokens in the rollouts.  
   - This helps measure how “surprising” or “expected” each token is under the reference distribution—part of the GRPO update.

3. **Gradient Updates**  
   - Training workers receive the rollouts and their log probabilities, compute the GRPO loss, and perform a gradient step.  
   - The model weights get updated, and changes are sent back to inference workers so they, too, remain up to date.

---

### Putting It All Together

By splitting generation, log-prob calculation, and training into separate pools of independently scalable workers, **Async-GRPO** maximizes GPU usage and accelerates reinforcement learning tasks. This asynchronous design eliminates the slow step-by-step “generate-then-train-then-generate” pattern and allows each part of the pipeline to progress at its own pace.

The result? Faster experiments, less idle time, and an overall more efficient way to run long-context RL tasks—particularly ones involving extensive rollouts on large models.

## Reproducing Results Step-by-Step with Async-GRPO

#### Environment setup

To set up base environments, run the following on each node being used:
```
conda create -n base python=3.12 -y
conda activate base
pip install -r requirements_base.txt
```

Next, set up a Ray cluster across the nodes. On the head node, run:
```
ray start --head \
--resources='{"verification_slot":100}' \
--port=6379 \
--object-manager-port=8076 \
--temp-dir=/dev/shm/ray

```

and on each additional node, run:
```
conda activate base
ray start --address=head_node_ip:6379
```

#### Inference workers

Once the Ray cluster has been set up, the next step is to spin up the inference workers (this includes both the vLLM rollout workers and the reference logprob workers). On each node being used for inference, launch inference workers on the desired GPUs. For example, in our case we had 11 vLLM rollout workers across our 16 GPUs and one logprob worker.

On one node, we ran the following for 8 vLLM rollout workers:
```
for i in (seq 0 7)
    echo "Launching generation worker on GPU $i..."
    python worker_dispatcher.py \
        --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
        --mode generation \
        --tensor_parallel_size 1 \
        --max_num_seqs 64 \
        --write_failed_generation_samples \
        --global_num_verifiers 50 | tee generation_worker_$i.log &
end
```

And on the other, we ran the following for 3 more vLLM workers and one ref logprob worker:
```
for i in (seq 0 3)
    if test $i -lt 3
        echo "Launching generation worker on GPU $i..."
        python worker_dispatcher.py \
            --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
            --mode generation \
            --tensor_parallel_size 1 \
            --max_num_seqs 128 \
            --write_failed_generation_samples \
            --global_num_verifiers 50 | tee generation_worker_$i.log &
    else
        echo "Launching logprob worker on GPU $i..."
        torchrun --nproc_per_node=1 --master_port=1234$i worker_dispatcher.py \
            --model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B \
            --mode logprob \
            --max_tokens_per_gpu 100000 2>&1 | tee logprob_worker_$i.log &
    end
end
```

#### Training

Finally, the last step is to launch the training on the remaining GPUs. In our case, our last four GPUs were dedicated to training, so on the node with remaining GPUs we ran:
```
conda create grpo python=3.12 -y
conda activate grpo
pip install -r requirements_fsdp.txt
pip install -r requirements_base.txt

torchrun --nproc_per_node=4 --master_port=12345 trainer_core.py 2>&1 | tee train_qwen.log
```
Hyperparameters can be passed as arguments or adjusted directly in [trainer_core.py](https://github.com/Red-Hat-AI-Innovation-Team/async-grpo/blob/main/trainer_core.py#L302):
```
    --model_name_or_path $base_model_path \
    --learning_rate $learning_rate \
    --batch_size $batch_size \
    --lr_scheduler $lr_scheduler \
    --num_warmup_steps $num_warmup_steps \
    --fsdp_sharding_strategy $fsdp_sharding_strategy \
    --max_tokens_per_gpu $max_tokens_per_gpu \
    --samples_per_question $samples_per_question \
    --loss_chunksize $loss_chunksize \
    --temperature $temperature \
    --max_generation_tokens $max_generation_tokens \
    --data_path $data_path \
    --min_samples_per_checkpoint $min_samples_per_checkpoint \
    --output_dir $output_dir \
```

For our specific run, we used the following:
```
set base_model_path deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B
set learning_rate 2e-6
set batch_size 128
set samples_per_question 8
set infinite_sampler_seed 223
set lr_scheduler "constant_with_warmup"
set num_warmup_steps 5
set fsdp_sharding_strategy "SHARD_GRAD_OP"
set max_tokens_per_gpu 80000
set loss_chunksize 2048
set temperature 0.6
set max_generation_tokens 8192
set data_path = sample-data/deepscaler.jsonl
set min_samples_per_checkpoint 30000
```

## Fully Open, From the Start

Async-GRPO aims to provide a practical, scalable solution for researchers and developers working with reinforcement learning. The library is lightweight, easy to set up, and designed to be adaptable for various use cases.

Rather than hold onto the library in private until it has matured, we believe that development should also be an open, transparent, and community-focused effort. As an open-source initiative with frequent updates, we encourage others to engage with the project, whether by using the library or contributing to its development. 

There are a number of updates, optimizations, and refinements coming soon:
* PyNCCL weight update from the actor to the generation and reference workers - currently using Ray Object storage which doesn't use RDMA for communication.
* Tensor parallel vLLM workers for long CoTs on large models >= 32B parameters.
* PyPI package releases.
* Improved logging and visualizations.

Join us in our effort to refine and expand the capabilities of Async-GRPO, and build out an amazing community-driven flexible, asynchronous RL library!
