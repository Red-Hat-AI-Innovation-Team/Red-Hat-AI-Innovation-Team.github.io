---
layout: post
title: Update 3 - On Reasoning vs Inference-time scaling - Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)
date: 2025-02-17
image:  'https://probabilistic-inference-scaling.github.io/assets/images/process_video_cover.jpg'
tags:   [reasoning, inference-time-scaling]
description: Understanding the distinction between reasoning and inference-time scaling in LLMs - insights from our R1 reproduction experiments.
---

Written by Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona, GX Xu of the Red Hat AI Innovation Team

> This is the third update on our journey to reproduce R1-like reasoning in small LLMs.
> The original blog post can be found [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning) and the first update is [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning-update-1) and the second update is [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning-update-2).

---

## Let's Start with the Results  

Last week, we shared some exciting findings from our paper on a **particle-filtering-based [inference-time scaling method](https://arxiv.org/abs/2502.01618)**. We demonstrated that using our method, even a **7B model** could match the performance of a significantly larger reasoning model, **o1-preview**, on the **Math500 dataset**. You can check out that [LinkedIn post](https://www.linkedin.com/posts/dr-akash-sri_were-kicking-off-the-second-week-of-our-activity-7294901426877546498-G3SD?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAQzpaEBoCVqmL5C9AIS3IcpKtXoSQqoNNk).  

While all models showed **strong performance** on Math500 when scaled at inference time using particle filtering, none were able to reach **o1-preview's** performance on the much more challenging **AIME-2024 dataset**.  

This week, we pushed our method further by scaling up with a **larger 32B Qwen-instruct model**, paired with an even larger **72B Qwen PRM**. The results? We're thrilled to share that **without any additional training**—meaning absolutely **no distillation from R1 or similar techniques**—we **outperformed o1-preview by one question**! 🎉  

---

## What Are "Reasoning" Models Really Doing?  

If you’ve spent enough time analyzing R1's output traces, as we have, you’ve probably noticed that its so-called **"reasoning"** often looks more like **a search process**. The model starts by generating an initial response, then critiques or evaluates its own draft, and if necessary, backtracks or restarts. This iterative search process continues until the model decides it has found the best answer to return.  

Interestingly, if you apply particle filtering, you’ll see strikingly similar patterns, with some differences. Our method starts by **generating multiple draft responses**, then uses a **PRM (preference ranking model) score** to evaluate and critique each partial draft. The promising responses continue, while weaker ones are eliminated, repeating until the model arrives at a final answer.  

This raises an intriguing question:  
**Is reasoning just a form of learned search?** 🤔  

---

## Training to Reason: Amortizing Inference-Time Scaling  

Inference-time scaling can be computationally expensive, requiring both the **transition model** and the **PRM**—sometimes even multiple PRMs. A natural next question is:  

**Can we use reinforcement learning (RL) or other training methods to make the transition model itself act as a PRM?**  

In other words, can we train the model to not only generate responses but also judge and refine its own drafts? This could effectively **amortize** the cost of inference-time scaling by training the model to perform this reasoning process upfront.  Moving forward, we’ll be focusing our efforts on testing this hypothesis and will continue sharing our findings. Stay tuned!  

---

If you want to cite our work, you can use the following BibTeX entry of the original blog post.

```bibtex
@misc{srivastava2024lessonsonreproducing,  
      title={Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)},  
      author={Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona and GX Xu},  
      url={https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning},  
      year={2025},  
}  
```