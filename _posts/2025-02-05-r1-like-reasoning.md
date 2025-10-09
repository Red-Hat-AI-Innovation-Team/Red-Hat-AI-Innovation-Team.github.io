---
layout: post
title: Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)
date: 2025-02-05
image:  'https://probabilistic-inference-scaling.github.io/assets/images/process_video_cover.jpg'
tags:   [reasoning, inference-time-scaling]
description: Learn how to reproduce R1-like reasoning in small LLMs using particle filtering, synthetic data, and GRPO - achieving GPT-4o accuracy with only 4 rollouts.
---

Written by Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona, GX Xu

> Disclaimer: We have been working on this nonstop since the ICML deadline and have lost some of the incredible Shakespearean writing abilities that we traditionally possess. 
> Apologies for any mistakes or sloppiness, we will soon ply ourselves with sugar and return better than ever! This is also a live doc, so we will be updating the sections (especially the recipe/results!) as we get results day by day! 
> We will continue to add more code/details/make this more robust as we go. Join us for our chaotic  yellow brick road journey to Oz R1!

## Section 1: Path from CoT to Inference-Time Scaling
Our journey in R1-like reasoning starts from how CoT data was synthesized to improve models.


__CoT__: The LLM community’s journey to inference scaling begins long, long ago with the arrival of CoT - aka Chain of Thought. In their 2022 paper, the team over at Google Brain discovered that just asking models to “think step by step” before answering a question boosted reasoning ability - simply by structuring the model’s response as a sequence of logical steps.


__Orca__: Researchers soon realized that prompting alone had its limits. While CoT-style reasoning helped models on some reasoning benchmarks, it wasn’t an inherent skill the models possessed - it was just an artifact of the inference time prompt. Microsoft’s Orca paper tackled this problem head on by distilling intermediate reasoning steps from GPT-4 into smaller models. Instead of just training a model to generate correct final answers, Orca explicitly supervised the reasoning process by encouraging models to imitate the structured, step-by-step reasoning of stronger models. This created a fundamental shift - instead of just CoT-style prompting, we were now CoT-style training, assigning reasoning to be an explicit learned objective. We also realized that smaller models could punch above their weight, so to speak, by mimicking the reasoning structures of more powerful models.


__Tree/Forest of Thought and Beam Search__: While CoT/Orca focused on single threads of reasoning, there was still a gap. Human problem solving is not linear! We explore multiple different solutions before deciding on just one! This insight leads us to Tree of Thought, where models generate multiple reasoning paths and explore different possible steps before committing to a final answer. Instead of solving problems in a single pass, Tree of Thought branches into multiple possibilities, evaluates and prunes bad reasoning paths, and in general allows for self correction and more robust decision making. Forest of Thought extended this idea by allowing parallel rees explore multiple reasoning paradigms at once.


### Process Supervision:

At this stage, a crucial problem emerges. Even if a model generates a correct answer, its reasoning process may be unreliable or produce shortcut solutions! We need a way to validate the process of thinking itself - indeed, this is what we learned in school - show your work! This leads us to process supervision, where models are rewarded not just for getting the right answer, but also for following a reasoning path that aligns with human expectations. Unlike general outcome based reward models, Process Supervision evaluates the logical correctness of each intermediate step. If a model follows a flawed but correct-looking reasoning chain, it is penalized even if the final answer is correct. This is where we introduce Process Reward Models, which learn to predict the likelihood of each reasoning step being correct. By using PRMs, we get more granular control over the logical consistency of a model’s reasoning steps. They offer a pathway towards allowing models to self-verify and guide their own reasoning trajectories.


### Inference Scaling:

We have arrived at the Inference Time Scaling stop on our journey through time! Inference scaling refers to methods that improve a model’s reasoning ability and performance at runtime, without any requiring additional training or fine tuning! As shown by the Large Language Monkeys paper that came out of Stanford, many small, open sourced language models will eventually produce a correct answer for even challenging problems when prompted enough times. This suggests that smaller language models have better performance ability locked up within them - we just have to coax it out of them! The question then becomes - how can we intelligently navigate the space of the LM’s possible answers to help it achieve its full potential?


This is where our method comes in!

## Section 2: Our Inference Scaling Method (particle filtering)

So what's wrong with current inference scaling methods?

Well, many current inference-time scaling methods "guide" their search process with Process Reward Models—off-the-shelf models that take a problem and a (partial or complete) answer and return a reward score. These methods (beam search, DVTS, etc) take the "top-N" options at every step and explore these.

The problem, however, is that PRMs, as in the case of almost all Reward Models, are imperfect. They are often inadequate approximations of the ground truth, and following them leads to Reward Hacking, where the final output is optimized to score well according to the reward model but fails to be useful and/or correct.

This is where our method comes in. We ask the following:
Can we frame inference-time scaling as a probabilistic inference task?

What do we do differently?

Instead of allowing the PRM to completely determine which answers we unroll further, we do the following:

Initialize a set of “particles”
Generate a “step” for each particle. (How an answer is broken into “steps” is determined by automatic delimiters - in this case, we use “\n\n”)
Use the PRM to give a score to each particle given the question and answer so far. Convert this raw PRM score into a “weight” using softmax.
Resample the particles according to these weights - every particle in this next stage can be sampled from every particle in the previous stage with whatever the softmax score probability was!
Continue steps 2-4 until all the particles have generated completed answers!
Pick your “final answer” by choosing whichever particle has the highest RM score.
For a super easy-to-understand, intuitive explanation of our method, see this video!

<video 
  width="100%" 
  controls 
  poster="https://probabilistic-inference-scaling.github.io/assets/images/process_video_cover.jpg">
  <source src="https://probabilistic-inference-scaling.github.io/assets/videos/process_video.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>


So what are our results? 

We get some very cool numbers!

Our method scales 4-16x better than the deterministic inference scaling methods out there.

On the MATH dataset, our method:

- Can scale Qwen2.5 Math 1.5B Instruct to GPT-4o accuracy with only 4 rollouts!
- Can scale Qwen2.5 Math 7B Instruct achieves o1 level accuracy with only 32 rollouts!
- Can scale Llama 1B model to almost reach Llama 70B and can scale Llama 8B model to reach GPT-4o!
- ![](/images/posts/2025-02-05-r1-like-reasoning/table.png)  
- ![](/images/posts/2025-02-05-r1-like-reasoning/llama-1b.png)  
- ![](/images/posts/2025-02-05-r1-like-reasoning/llama-8b.png)
- ![](/images/posts/2025-02-05-r1-like-reasoning/qwen-7b.png)


### Why is this so cool? 

We do all of this - scaling small models to such fantastic numbers - without training anything at all! Our method is able to efficiently guide a small, open source off-the-shelf model to “discover its potential” and make truly staggering improvements, just by intelligently navigating the search space!

Just to provide some comparison points, this recent work https://arxiv.org/pdf/2502.02508 trains a base model on trajectories generated from Qwen-2.5-Math-7B-Instruct and achieves an accuracy of 85.6% on MATH500, while our method is able to get to an accuracy of 87% just by milking the Qwen 2.5 Math 7B Instruct model itself for all its worth. Our results underline the novelty and elegance of this inference scaling method and again points to the core idea - how can we guide a language model through a search space to help it reach its full potential?

## Section 3: How We Connect Inference-Time Scaling to Training
Inference-time scaling is pretty wild—it lets us take a (relatively speaking) small model and boost its performance to rival some of the biggest names in mathematical reasoning benchmarks (OpenAI’s o1 for example). In simple terms, this means a tiny model (or for the RL folks, the policy) actually can reason mathematically, given the right conditions. But that raises the obvious question: how do we train a model to learn to inference-scale instead of orchestrating it with a PRM, at runtime?

Let’s break it down. As we saw earlier, inference-time scaling needs a method—like best-of-N (BoN) or particle filtering—and a reward model. This setup can be super expensive to run. So, how do we make it cheaper? One way is to train the model to imitate the inference-time scaling method (learn to generate trajectories similar to particle filtering or beam search) and self-evaluate (to replace PRM/ORM) its own reasoning before locking in an answer. Basically, instead of paying the full cost every time we run inference, we get the model to internalize the process through training.

### Training Models to Learn Inference-Time Scaling

So how do we actually do this? Well, we already have most of the pieces in place: a policy, a reward model, and an exploration method. If we throw in a reinforcement learning approach—like PPO or GRPO—we can close the loop and teach the model to “think” or “reason” on its own.

But that’s not the only approach. Another way is to use a small or a larger teacher model to generate trajectory data using inference time-scaling first. We can then fine-tune a smaller model with Supervised Fine-Tuning (SFT), and maybe follow it up with GRPO to reinforce the best reasoning strategies.

### Learning from R1: A Model That Knows When to Backtrack

Lately, I’ve been fascinated by R1’s approach. What stands out is how it generates multiple answers, evaluates them at intermediate steps or at the end, and then decides whether to backtrack, restart, or finalize an answer if it thinks it’s correct. This feels eerily similar to how a model under particle filtering would behave—exploring different paths before settling on the best one.

Of course, the “oh wait” moments (aka reflections 😆) aren’t as organic here because a reward model is guiding the process. But it’s still super impressive that DS managed to set up conditions where the model learned inference-time scaling just by using RL. The downside? Running that process requires a ton of compute, way more than we’d like to spend.

So instead, we’re taking what we’ve learned—that “it's likely” that training a model to learn inference-time scaling leads to reasoning-like abilities—and using it to make small models smarter.

### A Live Experiment Blog

The next section is where things get real. We’re going to document our experiments in real time—sharing our code, models, ideas, and results (including what didn’t work). The goal? Finding a more efficient way to make small models reason like o1 and R1—without the ridiculous compute costs. Let’s figure this out together. 🚀

## Section 4: Our Recipe / (a work in progress)

Building on our findings of inference-time scaling methods, we come up with a recipe to bake R1-like reasoning ability to small LLMs efficiently.


First of all, how is DeepSeek-R1 trained? DeepSeek-R1 is trained in a few phases:

1. R1-Zero / Reasoning Data: DeepSeek built R1-Zero by taking its existing MoE model, DeepSeek-V3-base, and applying a fresh, large-scale reinforcement learning training approach. It is then used to generate high-quality synthetic reasoning data, together with some other synthetic data approaches like few-shot CoT, reflection-verification prompting.
2. Warm Start: The synthetic data from the previous step is used to fine-tune DeepSeek-V3-base with standard instruction tuning to warm up small LLMs to be ready for reasoning RL (although they do have a limited style of reasoning at this moment). If you wanted to learn how to do full finetuning on LLMs, here is ICLR paper from our group that's almost a practitioner's guide to SFT: https://arxiv.org/abs/2412.13337
3. RL for Reasoning: After that, the model goes through another round of RL-based training (just like in step 1) to free up the limitations and unlock new reasoning capabilities, boosting its reasoning skills even further.
4. Rejection Sampling + SFT: Up to this point, the model has mainly been focused on reasoning. Now, it’s trained on a broader set of skills, kind of like what we do in InstructLab.
5. Preference Tuning: Finally, the model goes through a final round of RL-based tuning to make sure it’s safe and aligned with human preferences.

If you’re curious about steps 4 and 5, here’s a paper from our team explaining how to do this without human annotations: https://arxiv.org/abs/2411.02481.


So now we are looking for a way to obtain R1-like reasoning in small LLMs. We came up with a recipe that does not use DeepSeek-R1 nor its derivatives, and that is we are working on at the moment. Here is a side-by-side comparison between DeepSeek’s approach and our recipe.

|                          | DeepSeek                                                        | Us                                                         |
| :----------------------- | :-------------------------------------------------------------- | :--------------------------------------------------------- |
| R1-Zero / Reasoning Data | R1-Zero (???B), few-shot CoT, reflection-verification prompting | Phi-4 (14B) w/ inference-time scaling (BoN, Gibbs, PF)     |
| Warm Start               | DeepSeek-V3-base (???B)                                         | Granite-3.1-Lab (8B), Llama-3.1-Instruct (8B), Phi-4 (14B) |
| RL for Reasoning         | GRPO                                                            | GRPO                                                       |
| General Capability       | Rejection Sampling \+ SFT \-\> Preference Tuning                | DPO w/ Dr. SoW                                             |

### Here's a breakdown

1. R1-Zero / Reasoning Data: Instead of training R1-Zero to obtain high-quality reasoning data, we instead use inference-time scaling methods to generate reasoning trajectories that can be used to synthesize high-quality reasoning data (detailed below).
2. Warm Start: With the high-quality reasoning data generated, we then do the similar SFT on the models we are interested in training.
3. RL for Reasoning: After warming up, we perform the same RL training with GRPO.
4. General Capability: Our approach to obtaining general capability is based on DPO with preference data annotated by a reward model. This reward model is based on recent work from our team and it's a human annotation-free method called Dr. SoW. It matches (or even outperforms) the state of the art. Check it out here: https://arxiv.org/abs/2411.02481.


## Results: What Worked, What Didn’t, and What’s Next

Disclaimer:  
These results are a messy, chaotic, absolutely massive work in progress, and we’ll update code and results as we continue to get them\! We have not gotten very much sleep and we sincerely apologize for any gaps in the results table. Please pray to the gods of LLMs with us to help populate it\! Thank you for your cooperation \<3 

**Bespoke Dataset: A Good Start, but Not Enough**

Like pretty much everyone else, we kicked things off by working with the reasoning dataset created by Bespoke. From what we know, it’s distilled from R1, making it a solid starting point. But for our specific experiments, it didn’t quite hit the mark. Still, we wanted to see how far small models could go by just fine-tuning (SFT) on this dataset—and more importantly, whether training on a math-heavy reasoning dataset could help generalize the model’s reasoning ability to *non-math* tasks.

Turns out, it kinda worked\! Training on this dataset did help smaller Granite and Llama models mimic R1-like reasoning patterns. However, there was a catch: while they *looked* like they were reasoning, their actual benchmark performance didn’t improve after SFT.

So, we took the best SFT checkpoint and ran GRPO on it, hoping that the reasoning skills bootstrapped during fine-tuning would become more refined. Once again… no major improvement in benchmarks for Llama or Granite. 

**BoN with Phi-4: Prompting It to Think**

After some quick brainstorming and research, we decided to give **Phi-4** a shot. This model is seriously underrated—it performs ridiculously well on nearly every benchmark and even shows promising reasoning skills, at least in math. Best part? It’s only **14B parameters** and **fully open source**. Huge shoutout to Microsoft Research for that one\! 🎉

Given our past work with **InstructLab**, we like to think we know a thing or two about **synthetic data generation (SDG)** 😆. So, it didn’t take long to figure out how to prompt Phi-4 into generating reasoning trajectories.

Here’s what we did:

1. For each question, we generated **64 samples**.  
2. We used a **verifier** (from our inference-scaling paper) to pick the best trajectory—i.e., the one with the correct answer.  
3. We reformatted the data to match R1’s style, wrapping it in \<|thought|\> blocks **(Can someone check this for precision? 😅)**.  
4. We used this dataset (D-verified) to fine-tune our small models, followed by another round of GRPO.

This time, we saw some **really interesting results**:

✅ **Math scores improved for Llama**

✅ **AIME scores improved**

✅ **It even solved a problem posed by our chief scientist 😆**

**What We Learned: Two Big Gaps**

After looking at our results (and a bit of soul-searching 😛), we realized two major issues in how our models reasoned compared to R1:

1️⃣ **Short responses:** Our model’s answers were too concise—R1-style reasoning tends to be longer.

2️⃣ **No backtracking:** The model wasn’t self-reflecting or revising its own answers. We had hoped GRPO would make this emerge naturally, but it didn’t.

**What’s Next: Iterating on Phi-4 as Teacher & Student**

Back to the whiteboard we went\! One key insight: maybe it’s just **too hard** for an 8B model to develop reflection *without being explicitly trained on reflection examples*. R1 does this, so maybe we need to as well.

Since R1’s own paper suggests that the model being trained with RL needs to be reasonably strong, we decided to keep using **Phi-4**—not just as the **teacher**, but also as the **student** in our next experiments. Stay tuned. 🚀

—

**Teaching Models to Revise Their Own Thinking**

**Naïve Stitch: Making Mistakes on Purpose (and Fixing Them\!)**

Our first shot at making the model reason more like R1 was pretty simple: **force it to revise its own mistakes**. We took our BoN-generated data and created what we’re calling **D-stitch**.

Here’s how it works:

1\.	For each question, we start with the **thought process from a wrong sample**.

2\.	Then, we add a transition phrase like *“Hold on\! I made a mistake. Let me try again.”*

3\.	Finally, we append the thought process and solution from a **verified** correct sample.

4\.	Bonus: We can add more than one wrong thought before the correct one\!

The results? **A slight improvement**, but the real win was that the model actually started **revising its full reasoning process**. That’s a good sign\! Encouraged by this, we decided to push further and generate even more R1-like training data.

**PF Backtrack: Getting the Model to Doubt Itself**

While revising an entire answer is nice, it’s still not quite the reasoning we’re after. What we really want is **partial backtracking**—where the model recognizes errors midway, doubts itself, and changes course like R1.

This reminded us of something: **particle filtering (or any tree search method)**. Algorithmically, this kind of reasoning looks a lot like pruning bad search paths in a tree. So, we decided to generate backtrack data using particle filtering.

Here’s how we did it:

• We ran our **particle filtering method**, recording all the “dead” particles at each step (basically, failed reasoning paths).

• This gave us a **search tree** where we could verify the final solutions from the correct paths.

• We then synthesized new reasoning data by **intentionally stitching in incorrect branches** before returning to a correct path.

• Whenever the model backtracked, we added a phrase like *“Hold on\! I made a mistake. Let me try again.”*

We’re calling this dataset **D-backtrack**, and it’s designed to **train models to doubt and backtrack at intermediate steps, not just at the end**.

**Gibbs with “But Wait”: Inspired by S1**

While we were working on this, the **S1 paper** (🔗 [https://arxiv.org/abs/2501.19393](https://arxiv.org/abs/2501.19393)) dropped, giving us even more ideas\! Inspired by their approach, we created **D-but-wait**, a dataset designed to push the model toward deeper reasoning.

Here’s how we built it:

* When generating reasoning steps, we **force the model to pause** after completing the first thought.  
* Then, we append a phrase like **“But wait,”** and **force it to continue reasoning further** before finalizing the solution.

This setup encourages the model to naturally question its first thought, a bit like **Gibbs sampling** where you iterate until the solution stabilizes.

**Next Steps: Refining Backtracking and Doubt Mechanisms**

With these different approaches—D-stitch, D-backtrack, and D-but-wait—we’re getting models that **at least attempt to revise themselves**. But there’s still more to do\! We’re now exploring how to make backtracking even more structured and whether we need larger models to *fully* develop this behavior.

Let’s see where this takes us. 🚀

| Model                                                                            | Dataset                                                                                            | Method        | AIME 2024 (Pass@8) | MATH500 (Pass@8) |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------- | ------------------ | ---------------- |
| [Llama 3.1 8B Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | \-                                                                                                 | \-            | 6/30               | 73.6             |
|                                                                                  | [bespokelabs/Bespoke-Stratos-35k](https://huggingface.co/datasets/bespokelabs/Bespoke-Stratos-35k) | SFT           | ⏳                  | ⏳                |
|                                                                                  | Think-v1-13k (ours)                                                                                | SFT \+ GRPO   | 7/30               | 80.2             |
| [Phi-4](https://huggingface.co/microsoft/phi-4)                                  | \-                                                                                                 | \-            | 12/30              | 88.2             |
|                                                                                  | Think-v1-13k (ours)                                                                                | SFT \+ Dr.SoW | 10/30              | 90.8             |
|                                                                                  | But-wait-10k (ours)                                                                                | SFT \+ GRPO   | 10/30              | 87.8             |
|                                                                                  | Backtrack-22k(ours)                                                                               | SFT \+ GRPO   | 10/30              | ⏳                |

---

If you want to cite this blog post, you can use the following BibTeX entry

```bibtex
@misc{srivastava2024lessonsonreproducing,  
      title={Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)},  
      author={Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona and GX Xu},  
      url={https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning},  
      year={2025},  
}  
```