---
layout: post
title: Update 1 - Lessons on Reproducing R1-like Reasoning in Small LLMs without using DeepSeek-R1-Zero (or its derivatives)
date: 2025-02-06
image:  'https://probabilistic-inference-scaling.github.io/assets/images/process_video_cover.jpg'
tags:   [reasoning, inference-time-scaling]
description: First update on R1-like reasoning experiments - Granite models show significant gains with particle filtering and new data quality experiments.
---

Written by Akash Srivastava, Isha Puri, Kai Xu, Shivchander Sudalairaj, Mustafa Eyceoz, Oleg Silkin, Abhishek Bhandwaldar, Aldo Genaro Pareja Cardona, GX Xu

> This is the first update on our journey to reproduce R1-like reasoning in small LLMs.
> The original blog post can be found [here](https://red-hat-ai-innovation-team.github.io/posts/r1-like-reasoning).

---

Today was mostly about **organizing results**, evaluating **new checkpoints**, and making sense of all the numbers. We also kicked off a fresh experiment to **test the impact of data quality on reasoning in small LLMs**—but more on that later.

**Granite \+ Particle Filtering \= Big Gains 📈**

We already knew from our earlier experiments that **particle filtering works well** across multiple small models. But as we were compiling today’s results, we found something even more exciting: **Granite models also benefit significantly from our method\!** 🎉

Here’s how Granite 8B performed on the key benchmarks:

✅ **MATH-500:** **0.78** (Granite 8B)

✅ **AIME 2024:** **16.6** (Granite 8B)

This is **huge**—our **particle filtering method actually makes Granite better than GPT-4o on Math-500 and AIME 2024\!** 🎉🎉

**More Cool Results 🔥**

Across the board, **introducing reasoning**—using all the methods we talked about earlier—led to **consistent performance gains** on the **Math-500 and AIME 2024** benchmarks. Here’s a giant results table summarizing where we stand **(adding it here soon 👀)**.

| model | dataset | ckpt | (expected) aime@1 | aime@8 | note |
| :---- | :---- | :---- | :---- | :---- | :---- |
| deepseek-ai/DeepSeek-R1-Distill-Llama-8B | \- | \- | 33.75 | 66.67 | baselines/aime/DeepSeek-R1-Distill-Llama-8B |
| meta-llama/Llama-3.1-8B-Instruct | \- | \- | 2.92 | 10.00 | baselines/aime/Llama-3.1-8B-Instruct (This is without a specific prompt) |
| Llama-3.1-8B-Instruct | Bespoke-prompt | llama-r1-bmo-bespoke-system-numinamath/samples\_819150 | 5.83 | 16.67 |  |
| Llama-3.1-8B-Instruct | Bespoke-prompt \+ grpo | new\_grpo\_llama\_solo/ckpt-105 | 7.08 | 20.00 |  |
| Llama-3.1-8B-Instruct | Bespoke-prompt \+ grpo | new\_grpo\_llama\_solo/ckpt-120 | 7.50 | 20.00 | Our best llama |
| Llama-3.1-8B-Instruct | Bespoke-prompt \+ grpo | new\_grpo\_llama\_solo/ckpt-135 | 5.83 | 20.00 |  |
| Llama-3.1-8B-Instruct | Bespoke-prompt \+ grpo | new\_grpo\_llama\_solo/ckpt-150 | 6.25 | 20.00 |  |
|  |  |  |  |  |  |
| ibm-granite/granite-3.1-8b-instruct | \- | \- | 1.25 | 3.33 (was 10.00) |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
| microsoft/phi-4 | \- | \- | 19.17 | 43.33 | baselines/aime/phi-4 |
| Phi-4 | Bespoke-prompt | (add sft here) |  |  |  |
| Phi-4 | Bespoke-prompt \+ grpo | phi-r1-test-new-checkpoint-75 | 18.33 | 36.67 |  |
| Phi-4 | Bespoke-prompt \+ grpo | new\_grpo\_phi/ckpt-90 | 15.42 | 33.33 |  |
| Phi-4 | Bespoke-prompt \+ grpo | new\_grpo\_phi/ckpt-105 | 13.75 | 30.00 |  |
| Phi-4 | Backtrack | numinamath-phi4-traj-8x1-0.8-backtracked\_numinamath\_phi\_4/samples\_209128 | 16.67 | 36.67 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-165 | 12.08 | 26.67 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-255 | 14.58 | 30.00 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-285 | 13.33 | 26.67 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-315 | 16.25 | 43.33 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-405 | 15.00 | 26.67 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-450 | 15.83 | 23.33 |  |
| Phi-4 | Backtrack \+ grpo (beta 0.01) | grpo\_backtrack\_phi\_beta\_01/ckpt-465 | 16.25 | 33.33 |  |
| Phi-4 | But-Wait | but\_wait\_numinamath\_phi\_4/samples\_121519 | 17.08 | 36.67 |  |
| Phi-4 | But-Wait \+ grpo (beta 0.01) | grpo\_but\_wait\_phi\_beta\_01/ckpt-150 | 18.75 | 38.46 |  |
| Phi-4 | But-Wait \+ grpo (beta 0.01) | grpo\_but\_wait\_phi\_beta\_01/ckpt-210 | 17.08 | 36.67 |  |
| Phi-4 | But-Wait \+ grpo (beta 0.01) | grpo\_but\_wait\_phi\_beta\_01/ckpt-270 | 20.00 | 46.67 | Our best phi |
| Phi-4 | But-Wait \+ grpo (beta 0.01) | grpo\_but\_wait\_phi\_beta\_01/ckpt-360 | 16.67 | 40.00 |  |
| Phi-4 | Direct evolution GRPO | grpo\_evolution\_phi\_beta\_01/ckpt-15 | 13.75 | 36.67 |  |
| Phi-4 | Direct evolution GRPO | grpo\_evolution\_phi\_beta\_01/ckpt-30 | 15.83 | 26.67 |  |
| Phi-4 | Direct evolution GRPO MINI | grpo\_evolution\_mini\_phi\_beta\_01/ckpt-5 | 15.42 | 30.00 |  |
| Phi-4  | Direct evolution GRPO MINI | grpo\_evolution\_mini\_phi\_beta\_01/ckpt-10 | 17.08 | 26.67 |  |
| Phi-4  | Direct evolution GRPO MINI | grpo\_evolution\_mini\_phi\_beta\_01/ckpt-15 | 16.25 | 33.33 |  |
| Phi-4 | LIMO- no system prompt. Used \<thinking\>\<thinking\> and \<answer\>\<answer\> on the training. | limo\_phi\_4\_lr\_6e-6/samples\_1\`1159 | 32.00 | 48.00 | LIMO has 817 samples. LIMO has AIME-ish and MATH-ish data. |

**Data Quality: A Game-Changer?**

We came across this fascinating paper today: 🔗 [https://arxiv.org/abs/2502.03387](https://arxiv.org/abs/2502.03387), which dives deep into the importance of **data quality** in reasoning. The results are wild—they trained a **Qwen-32B** model on just **\~800 high-quality reasoning samples** and got **O1/R1-level performance** on MATH-500 and AIME24\!

Naturally, we had to try it out ourselves. **And guess what? It worked\!** Applying the same strategy to **Phi-4** gave us Phi-LIMO which is the best performing model so far (investigating the evaluation script as the numbers on the second run turned out to be lower), ~~which is **on par with the R1-distilled Llama-8B model**~~ 

**Most Interesting Takeaway of the Day**

Our **synthetic data-based reasoning methods** actually resulted in a **Phi-4 model that reasons better than vanilla Phi-4**—*and* it **shows its reasoning** in the process. That’s a big win for using synthetic data to enhance reasoning capabilities.

**What’s Still Running?**

Most of our compute is tied up with existing runs, so today we’re launching just **two more experiments**:

🔹 **Testing the LIMO dataset on Granite** – Can a really small model **develop reasoning** with just **\~800 high-quality examples**? We’ll let you know tomorrow.

🔹 **Generating synthetic data using particle filtering** on LIMO dataset questions—will this further enhance reasoning abilities?

This is funny so I have to mention it, GPT4-o just told me the following:   
**Did you know?** The human brain makes **approx. 35,000 decisions per day**, many of them involving subconscious “particle filtering” to evaluate possible outcomes. Teaching LLMs to backtrack and refine their reasoning is, in a way, mimicking our own decision-making process. 

What? 🤯

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