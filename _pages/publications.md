---
layout: page
title: Publications
permalink: /publications/
image:
description: Research publications from the AI Innovation Team on LLM optimization, continual learning, synthetic data generation, and inference-time scaling.
---

## Select Publications

Below is a selection of recent publications from our team, showcasing our work in large language models, machine learning, and AI research. Publications are listed in reverse chronological order.

NeurIPS 2025: We are proud to have 5 papers accepted at this years conference. We will add them below after the camera ready deadline later in October.

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2506.03303" target="_blank" rel="noopener">Hopscotch: Discovering and Skipping Redundancies in Language Models</a></h3>
<strong>Authors:</strong> Mustafa Eyceoz, <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Modern causal language models stack many attention blocks to improve performance, but not all blocks are necessary for every task. We propose Hopscotch, a simple yet effective method that identifies and skips attention blocks with least contributions to a task and adapts to preserve output quality. Hopscotch jointly optimizes which blocks to skip and how to scale the outputs of the remaining layers. By introducing lightweight, trainable scaling parameters to attention and MLP blocks, it mitigates distribution shifts in hidden states caused by removing attention blocks. Hopscotch does not modify model weights or require access to pretraining or instruction-tuning data, and is compatible with existing model compression techniques. When applied to 𝙻𝚕𝚊𝚖𝚊-𝟹.𝟷-𝟾𝙱 and 𝚀𝚠𝚎𝚗𝟸.𝟻-𝟽𝙱, Hopscotch achieves less than a 2% drop in performance even after skipping four attention blocks.
</details>
<strong><a href="https://arxiv.org/abs/2506.03303">📄 Arxiv</a> | <a href="https://youtube.com/live/1PGHYKqrE94?si=OkjefuYN7hK76NWU">🎥 Video</a></strong><br>
<strong>Date:</strong> 2025-06-03
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2504.07097" target="_blank" rel="noopener">Sculpting Subspaces: Constrained Full Fine-Tuning in LLMs for Continual Learning</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, Krishnateja Killamsetty, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en" target="_blank">Abhishek Bhandwaldar</a>, Prateek Chanda, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en" target="_blank">Aldo Pareja</a>, Oleg Silkin, Mustafa Eyceoz, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Continual learning in large language models (LLMs) is prone to catastrophic forgetting, where adapting to new tasks significantly degrades performance on previously learned ones. Existing methods typically rely on low-rank, parameter-efficient updates that limit the model's expressivity and introduce additional parameters per task, leading to scalability issues. To address these limitations, we propose a novel continual full fine-tuning approach leveraging adaptive singular value decomposition (SVD). Our method dynamically identifies task-specific low-rank parameter subspaces and constrains updates to be orthogonal to critical directions associated with prior tasks, thus effectively minimizing interference without additional parameter overhead or storing previous task gradients. We evaluate our approach extensively on standard continual learning benchmarks using both encoder-decoder (T5-Large) and decoder-only (LLaMA-2 7B) models, spanning diverse tasks including classification, generation, and reasoning. Empirically, our method achieves state-of-the-art results, up to 7% higher average accuracy than recent baselines like O-LoRA, and notably maintains the model's general linguistic capabilities, instruction-following accuracy, and safety throughout the continual learning process by reducing forgetting to near-negligible levels. Our adaptive SVD framework effectively balances model plasticity and knowledge retention, providing a practical, theoretically grounded, and computationally scalable solution for continual learning scenarios in large language models.
</details>
<strong><a href="https://arxiv.org/abs/2504.07097">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/orthogonal-subspace-learning">💻 Code</a> | <a href="https://ai-innovation.team/blog/orthogonal-subspace-learning">📝 Blog</a> | <a href="https://www.youtube.com/watch?v=A5Eg1RZK3oE">🎥 Video</a></strong><br>
<strong>Date:</strong> 2025-04-09
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2503.24358" target="_blank" rel="noopener">SQuat: Subspace-orthogonal KV Cache Quantization</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  The key-value (KV) cache accelerates LLMs decoding by storing KV tensors from previously generated tokens. It reduces redundant computation at the cost of increased memory usage. To mitigate this overhead, existing approaches compress KV tensors into lower-bit representations; however, quantization errors can accumulate as more tokens are generated, potentially resulting in undesired outputs. In this paper, we introduce SQuat (Subspace-orthogonal KV cache quantization). It first constructs a subspace spanned by query tensors to capture the most critical task-related information. During key tensor quantization, it enforces that the difference between the (de)quantized and original keys remains orthogonal to this subspace, minimizing the impact of quantization errors on the attention mechanism's outputs. SQuat requires no model fine-tuning, no additional calibration dataset for offline learning, and is grounded in a theoretical framework we develop. Through numerical experiments, we show that our method reduces peak memory by 2.17 to 2.82, improves throughput by 2.45 to 3.60, and achieves more favorable benchmark scores than existing KV cache quantization algorithms.
</details>
<strong><a href="https://arxiv.org/abs/2503.24358">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/SQuat">💻 Code</a> | <a href="https://ai-innovation.team/squat/">🌐 Website</a></strong><br>
<strong>Date:</strong> 2025-03-31
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.02421" target="_blank" rel="noopener">Activation-Informed Merging of Large Language Models</a></h3>
<strong>Authors:</strong> Amin Heyrani Nobari, Kaveh Alimohammadi, Ali ArjomandBigdeli, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Faez Ahmed, Navid Azizan<br>
<details>
  <summary>View Abstract</summary>
  Model merging, a method that combines the parameters and embeddings of multiple fine-tuned large language models (LLMs), offers a promising approach to enhance model performance across various tasks while maintaining computational efficiency. This paper introduces Activation-Informed Merging (AIM), a technique that integrates the information from the activation space of LLMs into the merging process to improve performance and robustness. AIM is designed as a flexible, complementary solution that is applicable to any existing merging method. It aims to preserve critical weights from the base model, drawing on principles from continual learning (CL) and model compression. Utilizing a task-agnostic calibration set, AIM selectively prioritizes essential weights during merging. We empirically demonstrate that AIM significantly enhances the performance of merged models across multiple benchmarks. Our findings suggest that considering the activation-space information can provide substantial advancements in the model merging strategies for LLMs, with up to a 40% increase in benchmark performance.
</details>
<strong><a href="https://arxiv.org/abs/2502.02421">📄 Arxiv</a> | <a href="https://github.com/ahnobari/ActivationInformedMerging">💻 Code</a></strong><br>
<strong>Date:</strong> 2025-02-04
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.01618" target="_blank" rel="noopener">Rollout Roulette: A Probabilistic Inference Approach to Inference-Time Scaling of LLMs using Particle-Based Monte Carlo Methods</a></h3>
<strong>Authors:</strong> Isha Puri, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Large language models (LLMs) have achieved significant performance gains via scaling up model sizes and/or data. However, recent evidence suggests diminishing returns from such approaches, motivating scaling the computation spent at inference time. Existing inference-time scaling methods, usually with reward models, cast the task as a search problem, which tends to be vulnerable to reward hacking as a consequence of approximation errors in reward models. In this paper, we instead cast inference-time scaling as a probabilistic inference task and leverage sampling-based techniques to explore the typical set of the state distribution of a state-space model with an approximate likelihood, rather than optimize for its mode directly. We propose a novel inference-time scaling approach by adapting particle-based Monte Carlo methods to this task. Our empirical evaluation demonstrates that our methods have a 4-16x better scaling rate over our deterministic search counterparts on various challenging mathematical reasoning tasks. Using our approach, we show that Qwen2.5-Math-1.5B-Instruct can surpass GPT-4o accuracy in only 4 rollouts, while Qwen2.5-Math-7B-Instruct scales to o1 level accuracy in only 32 rollouts. Our work not only presents an effective method to inference-time scaling, but also connects the rich literature in probabilistic inference with inference-time scaling of LLMs to develop more robust algorithms in future work.
</details>
<strong><a href="https://arxiv.org/abs/2502.01618">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/its_hub">💻 Code</a> | <a href="https://probabilistic-inference-scaling.github.io/">🌐 Website</a></strong><br>
<strong>Date:</strong> 2025-02-03
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2412.13337" target="_blank" rel="noopener">Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en" target="_blank">Aldo Pareja</a>, <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Krishnateja Killamsetty, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, Wenlong Zhao, Seungwook Han, <a href="https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en" target="_blank">Abhishek Bhandwaldar</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Luke Inglis, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  The rise of large language models (LLMs) has created a significant disparity: industrial research labs with their computational resources, expert teams, and advanced infrastructures, can effectively fine-tune LLMs, while individual developers and small organizations face barriers due to limited resources. In this paper, we aim to bridge this gap by presenting a comprehensive study on supervised fine-tuning of LLMs using instruction-tuning datasets spanning diverse knowledge domains and skills. We focus on small-sized LLMs (3B to 7B parameters) for their cost-efficiency and accessibility. We explore various training configurations and strategies across four open-source pre-trained models. We provide detailed documentation of these configurations, revealing findings that challenge several common training practices, including hyperparameter recommendations from TULU and phased training recommended by Orca. Key insights from our work include: (i) larger batch sizes paired with lower learning rates lead to improved model performance on benchmarks such as MMLU, MTBench, and Open LLM Leaderboard; (ii) early-stage training dynamics, such as lower gradient norms and higher loss values, are strong indicators of better final model performance, enabling early termination of sub-optimal runs and significant computational savings; (iii) through a thorough exploration of hyperparameters like warmup steps and learning rate schedules, we provide guidance for practitioners and find that certain simplifications do not compromise performance; and (iv) we observed no significant difference in performance between phased and stacked training strategies, but stacked training is simpler and more sample efficient. With these findings holding robustly across datasets and models, we hope this study serves as a guide for practitioners fine-tuning small LLMs and promotes a more inclusive environment for LLM research.
</details>
<strong><a href="https://arxiv.org/abs/2412.13337">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-12-17
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2411.02481" target="_blank" rel="noopener">Dr. SoW: Density Ratio of Strong-over-weak LLMs for Reducing the Cost of Human Annotation in Preference Tuning</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Preference tuning relies on high-quality human preference data, which is often expensive and time-consuming to gather. In this paper, we introduce Dr. Sow (Density Ratio of Strong over Weak) a cost-effective method that eliminates the reliance for human annotation by leveraging off-the-shelf LLMs for preference data annotation. Dr. Sow uses the log-density ratio between a better-aligned and a less-aligned LLM as a reward signal. We evaluate Dr. Sow across 221 different LLM pairs and empirically find a strong correlation between the performance gap of the paired models and the quality of the reward signal. This insight provides a practical guideline for selecting LLMs for data annotation. 
  Additionally, we introduce an end-to-end pipeline that customizes reward functions based on user query domains. Without fine-tuning, it improves accuracy on domain-specific evaluations. With a pair of Mistral-7B models, Dr. Sow achieves a RewardBench score of 82.6, outperforming the best trained reward functions from same model class and demonstrating competitive performance against SoTA models in Safety (91.0) and Reasoning (88.0) domains. Further, we preference-tune Llama-3-8B-Instruct using data annotated by Dr. Sow. Our approach pushes Llama-3-8B to achieve a 37.4 % (+15.1 %) win rate on ArenaHard and a 40.7 % (+17.8 %) win rate on length-controlled AlpacaEval 2.0.
</details>
<strong><a href="https://arxiv.org/abs/2411.02481">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/reward_hub">💻 Code</a> | <a href="https://www.redhat.com/en/blog/smarter-enterprise-ai-inference-time-scaling">📝 Blog</a></strong><br>
<strong>Date:</strong> 2024-11-04
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2403.01081" target="_blank" rel="noopener">Lab: Large-scale alignment for chatbots</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en" target="_blank">Abhishek Bhandwaldar</a>, <a href="https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en" target="_blank">Aldo Pareja</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, David D. Cox, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  This work introduces LAB (Large-scale Alignment for chatBots), a novel methodology designed to overcome the scalability challenges in the instruction-tuning phase of large language model (LLM) training. Leveraging a taxonomy-guided synthetic data generation process and a multi-phase tuning framework, LAB significantly reduces reliance on expensive human annotations and proprietary models like GPT-4. We demonstrate that LAB-trained models can achieve competitive performance across several benchmarks compared to models trained with traditional human-annotated or GPT-4 generated synthetic data. Thus offering a scalable, cost-effective solution for enhancing LLM capabilities and instruction-following behaviors without the drawbacks of catastrophic forgetting, marking a step forward in the efficient training of LLMs for a wide range of applications.
</details>
<strong><a href="https://arxiv.org/abs/2403.01081">📄 Arxiv</a> | <a href="https://github.com/instructlab">💻 Code</a></strong><br>
<strong>Date:</strong> 2024-03-02
</div>

## Team Members

For comprehensive publication lists and detailed research profiles of individual team members, please visit their Google Scholar pages below:

- [Akash Srivastava](https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en)
- [Kai Xu](https://scholar.google.com/citations?user=kf3C60wAAAAJ) 
- [Hao Wang](https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ)
- [Ligong Han](https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en)
- [Giorgio Giannone](https://scholar.google.com/citations?user=1qsJQhkAAAAJ&hl=en)
- [Aldo Pareja](https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en)
- [Abhishek Bhandwaldar](https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en)
- [Shivchander Sudalairaj](https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en)
- [Guangxuan Xu](https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en)
- [Mustafa Eyceoz](https://arxiv.org/search/cs?searchtype=author&query=Eyceoz,+M)
- [Nikhil Nayak](https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en)