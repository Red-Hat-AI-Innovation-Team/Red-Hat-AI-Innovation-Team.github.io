---
layout: post
title: Update 2 - Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)
date: 2025-02-07
image:  'https://probabilistic-inference-scaling.github.io/assets/images/process_video_cover.jpg'
tags:   [reasoning, inference-time-scaling]
description: Second update on R1 reasoning research - new results on training small LLMs with synthetic reasoning data and particle filtering methods.
---

Written by Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona, GX Xu

> This is the second update on our journey to reproduce R1-like reasoning in small LLMs.
> The original blog post can be found [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning) and the first update is [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning-update-1).

---

**Today’s Updates: More Experiments, More Insights**

Yesterday, we ran **two new experiments** to push our small models even further:

🔹 **Testing the LIMO dataset on Granite** – Can a really small model develop reasoning abilities with just **\~800 high-quality examples**?

Unfortunately, this one **didn’t pan out**. Neither **Llama** nor **Granite** showed much improvement, even though this dataset significantly boosted **Phi-4’s** performance. The original paper demonstrated strong results on **Qwen-32B**, but based on our experiment, it’s clear that the effectiveness of this approach is **very model-dependent**.

In short: **Qwen-32B is just a beast.** It already has strong mathematical and reasoning abilities, so training on a relatively tiny dataset helps refine what’s already there. For smaller models? Not so much. (*Guess there’s no such thing as a free lunch after all\! 😅*)

🔹 **Generating synthetic data using particle filtering on LIMO dataset questions** – Could this enhance reasoning abilities?

This one was interesting\! Running **Phi-4** with our **particle filtering-based inference scaling method**, it successfully solved **about half** of the **\~800 LIMO problems** using a **512-particle count**.

Here’s what happened next:

* We **built a backtracking-based reasoning dataset** using these filtered solutions and fine-tuned the same **Phi-4** model that we used for generation.

* **Did it work?** Nope. The model actually solved **fewer AIME24 problems** than the base model. ❌

* However, when we trained using **only the correct solution dataset**, the model managed to **preserve its performance**.

* Comparing the **LIMO dataset solutions** with those from Phi-4, we found that **LIMO solutions were 2–3 times longer**.

* Training on a **380-sample subset** of this data **slightly improved AIME24 performance**, but *only* by solving **one more question**. 🤷‍♂️

**What’s Next? New Experiments Underway 🚀**

We finally **killed off our older GRPO runs** after running them for quite a few iterations. The reason? **The reward had plateaued**, and the trained models showed **no further improvements** on AIME24.

At this point, I’m starting to wonder: **Is AIME24 just too difficult for small models unless they’ve been trained with distilled data from larger reasoning models?** 🤔 We’ll keep using it for now, but we might reconsider another benchmark later.

Today, we launched **two new experiments**:

🔹 **GRPO on “But Wait” Phi Checkpoint & LIMO Questions**

* We’re testing if the **increased difficulty** of the **LIMO** questions can **trigger any reasoning sparks** in our best **“But Wait” Phi checkpoint**—which already shows **R1-style reflection and reasoning**.

🔹 **Introducing GRPO-Direct**

* Instead of our usual **“generate synthetic data → SFT → GRPO”** loop, we’re trying a **direct** approach:

	1\.	**Generate synthetic data** inside **GRPO** itself.

	2\.	**Immediately train the model on it** within the same loop.

We’re running this on the **LIMO dataset**, using a **Phi checkpoint** that has already been trained on synthetic data it generated from the **380 LIMO samples**.

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