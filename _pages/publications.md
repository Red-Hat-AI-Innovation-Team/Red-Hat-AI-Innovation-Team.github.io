---
layout: page
title: Publications
permalink: /publications/
image:
description: Research publications from the AI Innovation Team on LLM optimization, continual learning, synthetic data generation, and inference-time scaling.
---

## Select Publications

Below is a selection of recent publications from our team, showcasing our work in large language models, machine learning, and AI research. Publications are listed in reverse chronological order.

We are proud to have 5 papers accepted at NeurIPS 2025.

<div class="publication-card">
<h3><a href="https://haowang94.github.io/files/specbench.pdf" target="_blank" rel="noopener">Turning Intent into Specifications: A Benchmark and an Interactive User-Assistant Agent</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Today's agents are highly effective at implementing well-scoped software design plans, but user intent is often vague and admits multiple equally valid solutions. In this paper, we introduce SpecBench, a new benchmark for evaluating an agent's ability to translate user intent into a structured, executable specification that aligns with user preferences. The agent is given access to past user conversations and may interact with the user for a fixed number of rounds to ask clarifying questions. We find that existing agents exhibit two extreme behaviors: they either (i) struggle to collaborate proactively with users, entering implementation mode too quickly while overestimating their understanding of user preferences, or (ii) exhaust their question budget by asking about every ambiguous design choice. To address this limitation, we introduce a user-assistant agent: Buddy. It follows a workflow inspired by classical morphological analysis, decomposing user intent into a structured space of design dimensions and candidate choices. It then creates simulated users to evaluate these choices, before engaging the real user to resolve remaining ambiguities and finalize the specification. By shifting the focus from execution to specification, SpecBench and Buddy emphasize agent-user collaboration (not just code generation) as a key frontier in future agent design.
</details>
<strong><a href="https://haowang94.github.io/files/specbench.pdf">📄 Paper</a> | <a href="https://github.com/haowang94/intent2spec">💻 Code</a> | <a href="https://huggingface.co/datasets/haowang94/specbench">🤗 Data</a> | <a href="https://haowang94.github.io/blog/specbench/">📝 Blog</a> | <a href="https://ai-innovation.team/specbench/">🌐 Website</a></strong><br>
<strong>Date:</strong> 2026-05-18
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2605.17842" target="_blank" rel="noopener">SNLP: Layer-Parallel Inference via Structured Newton Corrections</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Autoregressive language models execute Transformer layers sequentially, creating a latency bottleneck that is not removed by conventional tensor or pipeline parallelism. We study whether this layerwise dependency can be relaxed by treating the hidden-state trace across layers as the solution of a nonlinear residual equation and solving it with parallel Newton-style updates. While this view is principled, exact Newton corrections require expensive Jacobian-vector products and naive fixed-point iterations are unstable on trained Transformers. We introduce Structured Newton Layer Parallelism (SNLP), a training and inference framework that replaces exact layer Jacobians with cheap architecture-induced surrogate dynamics. In residual Transformers, this yields Identity Newton (IDN), where the correction reduces to a prefix-sum-like update; in mHC-style architectures, HC Newton (HCN) uses the model's residual mixing matrix. We further introduce SNLP-aware regularization, which trains models to make one or a few structured Newton iterations accurately approximate the sequential forward. Experiments on nanochat-scale Transformers show that SNLP regularization improves layer-parallel compatibility and can also improve standard sequential perplexity, reducing baseline PPL by 4.7%-23.4%. At inference time, SNLP combined with layer fusion and chunkwise decomposition achieves practical wall-clock speedups: on a 0.5B Nanochat model, it reaches 2.3x speedup while still improving PPL by 6.1%. These results suggest that layer-parallel inference is not merely a numerical approximation to sequential execution, but can act as a useful solver-induced inference bias. We also characterize limitations: off-the-shelf pretrained models are less amenable to this procedure, and exact convergence recovers the sequential computation rather than providing monotonic inference-time scaling.
</details>
<strong><a href="https://arxiv.org/abs/2605.17842">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2026-05-18
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2603.27448" target="_blank" rel="noopener">GIFT: Bootstrapping Image-to-CAD Program Synthesis via Geometric Feedback</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=1qsJQhkAAAAJ&hl=en" target="_blank">Giorgio Giannone</a>, Anna Clare Doris, Amin Heyrani Nobari, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Faez Ahmed<br>
<details>
  <summary>View Abstract</summary>
  Generating executable CAD programs from images requires alignment between visual geometry and symbolic program representations, a capability that current methods fail to learn reliably as design complexity increases. Existing fine-tuning approaches rely on either limited supervised datasets or expensive post-training pipelines, resulting in brittle systems that restrict progress in generative CAD design. We argue that the primary bottleneck lies not in model or algorithmic capacity, but in the scarcity of diverse training examples that align visual geometry with program syntax. This limitation is especially acute because the collection of diverse and verified engineering datasets is both expensive and difficult to scale, constraining the development of robust generative CAD models. We introduce Geometric Inference Feedback Tuning (GIFT), a data augmentation framework that leverages geometric feedback to turn test-time compute into a bootstrapped set of high-quality training samples. GIFT combines two mechanisms: Soft-Rejection Sampling (GIFT-REJECT), which retains diverse high-fidelity programs beyond exact ground-truth matches, and Failure-Driven Augmentation (GIFT-FAIL), which converts near-miss predictions into synthetic training examples that improve robustness on challenging geometries. By amortizing inference-time search into the model parameters, GIFT captures the benefits of test-time scaling while reducing inference compute by 80%. It improves mean IoU by 12% over a strong supervised baseline and remains competitive with more complex multimodal systems, without requiring additional human annotation or specialized architectures.
</details>
<strong><a href="https://arxiv.org/abs/2603.27448">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2026-03-28<br>
<span class="conference-badge">ICML 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2601.08000" target="_blank" rel="noopener">Reasoning over Precedents Alongside Statutes: Case-Augmented Deliberative Alignment for LLM Safety</a></h3>
<strong>Authors:</strong> Can Jin, Rui Wu, Tong Che, Qixin Zhang, Hongwu Peng, Jiahui Zhao, Zhenting Wang, Wenqi Wei, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Zhao Zhang, Yuan Cao, Ruixiang Tang, Dimitris N. Metaxas<br>
<details>
  <summary>View Abstract</summary>
  Ensuring that Large Language Models (LLMs) adhere to safety principles without refusing benign requests remains a significant challenge. While OpenAI introduces deliberative alignment (DA) to enhance the safety of its o-series models through reasoning over detailed "code-like" safety rules, the effectiveness of this approach in open-source LLMs, which typically lack advanced reasoning capabilities, is understudied. In this work, we systematically evaluate the impact of explicitly specifying extensive safety codes versus demonstrating them through illustrative cases. We find that referencing explicit codes inconsistently improves harmlessness and systematically degrades helpfulness, whereas training on case-augmented simple codes yields more robust and generalized safety behaviors. By guiding LLMs with case-augmented reasoning instead of extensive code-like safety rules, we avoid rigid adherence to narrowly enumerated rules and enable broader adaptability. Building on these insights, we propose CADA, a case-augmented deliberative alignment method for LLMs utilizing reinforcement learning on self-generated safety reasoning chains. CADA effectively enhances harmlessness, improves robustness against attacks, and reduces over-refusal while preserving utility across diverse benchmarks, offering a practical alternative to rule-only DA for improving safety while maintaining helpfulness.
</details>
<strong><a href="https://arxiv.org/abs/2601.08000">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2026-01-12<br>
<span class="conference-badge">ACL 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2510.23667" target="_blank" rel="noopener">Optimize Any Topology: A Foundation Model for Shape- and Resolution-Free Topology Optimization</a></h3>
<strong>Authors:</strong> Amin Heyrani Nobari, Lyle Regenwetter, Cyril Picard, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Faez Ahmed<br>
<details>
  <summary>View Abstract</summary>
  Structural topology optimization (TO) is central to engineering design but remains computationally intensive due to complex physics and hard constraints. Existing deep-learning methods are limited to fixed square grids, a few hand-coded boundary conditions, and post-hoc optimization, preventing general deployment. We introduce Optimize Any Topology (OAT), a foundation-model framework that directly predicts minimum-compliance layouts for arbitrary aspect ratios, resolutions, volume fractions, loads, and fixtures. OAT combines a resolution- and shape-agnostic autoencoder with an implicit neural-field decoder and a conditional latent-diffusion model trained on OpenTO, a new corpus of 2.2 million optimized structures covering 2 million unique boundary-condition configurations. On four public benchmarks and two challenging unseen tests, OAT lowers mean compliance up to 90% relative to the best prior models and delivers sub-1 second inference on a single GPU across resolutions from 64 x 64 to 256 x 256 and aspect ratios as high as 10:1. These results establish OAT as a general, fast, and resolution-free framework for physics-aware topology optimization and provide a large-scale dataset to spur further research in generative modeling for inverse design.
</details>
<strong><a href="https://arxiv.org/abs/2510.23667">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-10-26<br>
<span class="conference-badge">NeurIPS 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2510.05825" target="_blank" rel="noopener">Mitigating Premature Exploitation in Particle-based Monte Carlo for Inference-Time Scaling</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=1qsJQhkAAAAJ&hl=en" target="_blank">Giorgio Giannone</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, Rohan Mahesh Awhad, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Inference-Time Scaling (ITS) improves language models by allocating more computation at generation time. Particle Filtering (PF) has emerged as a strong ITS method for complex mathematical reasoning tasks, but it is vulnerable when guided by process reward models, which often assign overconfident scores early in the reasoning process. This causes PF to suffer from premature exploitation: it myopically commits to locally promising trajectories, prunes potentially correct hypotheses, and converges to suboptimal solutions. This failure mode, known as particle impoverishment, is especially severe under constrained computational budgets. To address this, we analyze the problem and identify two root causes: a lack of diversity in the particle set due to overconfident resampling and consequent inability to assess the potential of a reasoning path. We introduce Entropic Particle Filtering (ePF), an algorithm that integrates two new techniques to solve these issues. The first technique, Entropic Annealing (EA), directly mitigates particle impoverishment by monitoring search diversity via entropy; when diversity drops, it intervenes by dynamically annealing the resampling distribution to preserve exploration. The second, an enhancement called Look-ahead Modulation (LaM), adds a predictive guide to evaluate a state's potential based on its successors. On several challenging math benchmarks, ePF significantly outperforms strong baselines and achieves up to a 50% relative improvement in task reward. Together, these methods improve PF's resilience by balancing the exploration of diverse solution spaces with the exploitation of high-reward regions, ultimately leading to higher-quality solutions.
</details>
<strong><a href="https://arxiv.org/abs/2510.05825">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-10-07<br>
<span class="conference-badge">ICML 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2509.22854" target="_blank" rel="noopener">Towards Generalizable Implicit In-Context Learning with Attention Routing</a></h3>
<strong>Authors:</strong> Jiaqian Li, Yanshu Li, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Ruixiang Tang, Wenya Wang<br>
<details>
  <summary>View Abstract</summary>
  Implicit in-context learning (ICL) has newly emerged as a promising paradigm that simulates ICL behaviors in the representation space of Large Language Models (LLMs), aiming to attain few-shot performance at zero-shot cost. However, existing approaches largely rely on injecting shift vectors into residual flows, which are typically constructed from labeled demonstrations or task-specific alignment. Such designs fall short of utilizing the structural mechanisms underlying ICL and suffer from limited generalizability. To address this, we propose In-Context Routing (ICR), a novel implicit ICL method that internalizes generalizable ICL patterns at the attention logits level. It extracts reusable structural directions that emerge during ICL and employs a learnable input-conditioned router to modulate attention logits accordingly, enabling a train-once-and-reuse framework. We evaluate ICR on 12 real-world datasets spanning diverse domains and multiple LLMs. The results show that ICR consistently outperforms prior implicit ICL methods that require task-specific retrieval or training, while demonstrating robust generalization to out-of-domain tasks where existing methods struggle. These findings position ICR to push the boundary of ICL's practical value.
</details>
<strong><a href="https://arxiv.org/abs/2509.22854">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-09-26<br>
<span class="conference-badge">ICML 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2508.07871" target="_blank" rel="noopener">CATP: Contextually Adaptive Token Pruning for Efficient and Enhanced Multimodal In-Context Learning</a></h3>
<strong>Authors:</strong> Yanshu Li, Jianjiang Yang, Zhennan Shen, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Haoyan Xu, Ruixiang Tang<br>
<details>
  <summary>View Abstract</summary>
  Modern large vision-language models (LVLMs) convert each input image into a large set of tokens that far outnumber the text tokens. Although this improves visual perception, it also introduces severe image token redundancy. Because image tokens contain sparse information, many contribute little to reasoning but greatly increase inference cost. Recent image token pruning methods address this issue by identifying important tokens and removing the rest. These methods improve efficiency with only small performance drops. However, most of them focus on single-image tasks and overlook multimodal in-context learning (ICL), where redundancy is higher and efficiency is more important. Redundant tokens weaken the advantage of multimodal ICL for rapid domain adaptation and lead to unstable performance. When existing pruning methods are applied in this setting, they cause large accuracy drops, which exposes a clear gap and the need for new approaches. To address this, we propose Contextually Adaptive Token Pruning (CATP), a training-free pruning method designed for multimodal ICL. CATP uses two stages of progressive pruning that fully reflect the complex cross-modal interactions in the input sequence. After removing 77.8% of the image tokens, CATP achieves an average performance gain of 0.6% over the vanilla model on four LVLMs and eight benchmarks, clearly outperforming all baselines. At the same time, it improves efficiency by reducing inference latency by an average of 10.78%. CATP strengthens the practical value of multimodal ICL and lays the foundation for future progress in interleaved image-text settings.
</details>
<strong><a href="https://arxiv.org/abs/2508.07871">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-08-11<br>
<span class="conference-badge">AAAI 2026 (Oral)</span>
</div>

<div class="publication-card">
<h3><a href="https://www.arxiv.org/abs/2506.09338" target="_blank" rel="noopener">Know What You Don't Know: Uncertainty Calibration of Process Reward Models</a></h3>
<strong>Authors:</strong> Young-Jin Park, Kristjan Greenewald, Kaveh Alim, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Navid Azizan<br>
<details>
  <summary>View Abstract</summary>
  Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs). However, we observe that even state-of-the-art PRMs can be poorly calibrated. Specifically, they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory. To address this, we present a calibration approach -- performed via quantile regression -- that adjusts PRM outputs to better align with true success probabilities. Leveraging these calibrated success estimates and their associated confidence bounds, we introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer. Unlike conventional methods that allocate a fixed number of reasoning trajectories per query, this approach adapts to each instance and reasoning step when using our calibrated PRMs. Experiments on mathematical reasoning benchmarks show that (i) our PRM calibration method achieves small calibration error, outperforming the baseline methods, (ii) calibration is crucial for enabling effective IAS, and (iii) the proposed IAS strategy reduces inference costs while maintaining final answer accuracy, utilizing less compute on more confident problems as desired.
</details>
<strong><a href="https://www.arxiv.org/abs/2506.09338">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-06-11<br>
<span class="conference-badge">NeurIPS 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2506.03303" target="_blank" rel="noopener">Hopscotch: Discovering and Skipping Redundancies in Language Models</a></h3>
<strong>Authors:</strong> Mustafa Eyceoz, <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Modern causal language models stack many attention blocks to improve performance, but not all blocks are necessary for every task. We propose Hopscotch, a simple yet effective method that identifies and skips attention blocks with least contributions to a task and adapts to preserve output quality. Hopscotch jointly optimizes which blocks to skip and how to scale the outputs of the remaining layers. By introducing lightweight, trainable scaling parameters to attention and MLP blocks, it mitigates distribution shifts in hidden states caused by removing attention blocks. Hopscotch does not modify model weights or require access to pretraining or instruction-tuning data, and is compatible with existing model compression techniques. When applied to 𝙻𝚕𝚊𝚖𝚊-𝟹.𝟷-𝟾𝙱 and 𝚀𝚠𝚎𝚗𝟸.𝟻-𝟽𝙱, Hopscotch achieves less than a 2% drop in performance even after skipping four attention blocks.
</details>
<strong><a href="https://arxiv.org/abs/2506.03303">📄 Arxiv</a> | <a href="https://youtube.com/live/1PGHYKqrE94?si=OkjefuYN7hK76NWU">🎥 Video</a></strong><br>
<strong>Date:</strong> 2025-06-03<br>
<span class="conference-badge">EMNLP 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2505.17097" target="_blank" rel="noopener">Make LVLMs Focus: Context-Aware Attention Modulation for Better Multimodal In-Context Learning</a></h3>
<strong>Authors:</strong> Yanshu Li, Jianjiang Yang, Ziteng Yang, Bozheng Li, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Hongyang He, Zhengtao Yao, Yingjie Victor Chen, Songlin Fei, Dongfang Liu, Ruixiang Tang<br>
<details>
  <summary>View Abstract</summary>
  Multimodal in-context learning (ICL) is becoming a key capability that allows large vision-language models (LVLMs) to adapt to novel tasks without parameter updates, which expands their usefulness in many real-world applications. However, ICL performance remains unstable even when the in-context demonstrations (ICDs) are well matched, showing that LVLMs still struggle to make full use of the provided context. While existing work mainly focuses on prompt engineering or post-hoc logit calibration, we study the attention mechanisms inside LVLMs to address their inherent limitations. We identify two important weaknesses in their self-attention that hinder effective ICL. To address these weaknesses, we propose Context-Aware Modulated Attention (CAMA), a training-free and plug-and-play method that dynamically adjusts attention logits based on the input in-context sequence. CAMA uses a two-stage modulation process that strengthens attention to semantically important tokens, especially visual ones. Across four LVLMs and seven benchmarks, CAMA consistently outperforms vanilla models and baselines, showing clear effectiveness and generalization. It can also activate the intended benefits of prompt engineering methods and remains robust across different sequence configurations. Therefore, CAMA opens up new directions for improving multimodal reasoning through a deeper understanding of attention dynamics.
</details>
<strong><a href="https://arxiv.org/abs/2505.17097">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-05-21<br>
<span class="conference-badge">AAAI 2026 (Oral)</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2505.11737" target="_blank" rel="noopener">TokUR: Token-Level Uncertainty Estimation for Large Language Model Reasoning</a></h3>
<strong>Authors:</strong> Tunyu Zhang, Haizhou Shi, Yibin Wang, Hengyi Wang, Xiaoxiao He, Zhuowei Li, Haoxian Chen, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, Huan Zhang, Dimitris Metaxas, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a><br>
<details>
  <summary>View Abstract</summary>
  While Large Language Models (LLMs) have demonstrated impressive capabilities, their output quality remains inconsistent across various application scenarios, making it difficult to identify trustworthy responses, especially in complex tasks requiring multi-step reasoning. In this paper, we propose a Token-level Uncertainty estimation framework for Reasoning (TokUR) that enables LLMs to self-assess and self-improve their responses in mathematical reasoning. Specifically, we introduce low-rank random weight perturbation during LLM decoding to generate predictive distributions for token-level uncertainty estimation, and we aggregate these uncertainty quantities to capture the semantic uncertainty of generated responses. Experiments on mathematical reasoning datasets of varying difficulty demonstrate that TokUR exhibits a strong correlation with answer correctness and model robustness, and the uncertainty signals produced by TokUR can be leveraged to enhance the model's reasoning performance at test time. These results highlight the effectiveness of TokUR as a principled and scalable approach for improving the reliability and interpretability of LLMs in challenging reasoning tasks.
</details>
<strong><a href="https://arxiv.org/abs/2505.11737">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-05-16<br>
<span class="conference-badge">ICLR 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://dl.acm.org/doi/abs/10.1145/3701716.3717574" target="_blank" rel="noopener">APEER: Automatic Prompt Engineering Enhances Large Language Model Reranking</a></h3>
<strong>Authors:</strong> Can Jin, Hongwu Peng, Shiyu Zhao, Zhenting Wang, Wujiang Xu, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Jiahui Zhao, Kai Zhong, Sanguthevar Rajasekaran, Dimitris N. Metaxas<br>
<details>
  <summary>View Abstract</summary>
  Large Language Models (LLMs) have significantly enhanced Information Retrieval (IR) across various modules, such as reranking. Despite impressive performance, current zero-shot relevance ranking with LLMs heavily relies on human prompt engineering. Existing automatic prompt engineering algorithms primarily focus on language modeling and classification tasks, leaving the domain of IR, particularly reranking, underexplored. Directly applying current prompt engineering algorithms to relevance ranking is challenging due to the integration of query and long passage pairs in the input, where the ranking complexity surpasses classification tasks. To reduce human effort and unlock the potential of prompt optimization in reranking, we introduce a novel automatic prompt engineering algorithm named APEER. APEER iteratively generates refined prompts through feedback and preference optimization. Extensive experiments with four LLMs and ten datasets demonstrate the substantial performance improvement of APEER over existing state-of-the-art (SoTA) manual prompts. Furthermore, we find that the prompts generated by APEER exhibit better transferability across diverse tasks and LLMs.
</details>
<strong><a href="https://dl.acm.org/doi/abs/10.1145/3701716.3717574">📄 Paper</a> | <a href="https://arxiv.org/abs/2406.14449">📄 Arxiv</a> | <a href="https://github.com/jincan333/APEER">💻 Code</a></strong><br>
<strong>Date:</strong> 2025-04-28<br>
<span class="conference-badge">WWW 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2504.07097" target="_blank" rel="noopener">Sculpting Subspaces: Constrained Full Fine-Tuning in LLMs for Continual Learning</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, Krishnateja Killamsetty, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en" target="_blank">Abhishek Bhandwaldar</a>, Prateek Chanda, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en" target="_blank">Aldo Pareja</a>, Oleg Silkin, Mustafa Eyceoz, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Continual learning in large language models (LLMs) is prone to catastrophic forgetting, where adapting to new tasks significantly degrades performance on previously learned ones. Existing methods typically rely on low-rank, parameter-efficient updates that limit the model's expressivity and introduce additional parameters per task, leading to scalability issues. To address these limitations, we propose a novel continual full fine-tuning approach leveraging adaptive singular value decomposition (SVD). Our method dynamically identifies task-specific low-rank parameter subspaces and constrains updates to be orthogonal to critical directions associated with prior tasks, thus effectively minimizing interference without additional parameter overhead or storing previous task gradients. We evaluate our approach extensively on standard continual learning benchmarks using both encoder-decoder (T5-Large) and decoder-only (LLaMA-2 7B) models, spanning diverse tasks including classification, generation, and reasoning. Empirically, our method achieves state-of-the-art results, up to 7% higher average accuracy than recent baselines like O-LoRA, and notably maintains the model's general linguistic capabilities, instruction-following accuracy, and safety throughout the continual learning process by reducing forgetting to near-negligible levels. Our adaptive SVD framework effectively balances model plasticity and knowledge retention, providing a practical, theoretically grounded, and computationally scalable solution for continual learning scenarios in large language models.
</details>
<strong><a href="https://arxiv.org/abs/2504.07097">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/orthogonal-subspace-learning">💻 Code</a> | <a href="https://ai-innovation.team/blog/orthogonal-subspace-learning">📝 Blog</a> | <a href="https://www.youtube.com/watch?v=A5Eg1RZK3oE">🎥 Video</a></strong><br>
<strong>Date:</strong> 2025-04-09<br>
<span class="conference-badge">ICLR 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2503.24358" target="_blank" rel="noopener">SQuat: Subspace-orthogonal KV Cache Quantization</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  The key-value (KV) cache accelerates LLMs decoding by storing KV tensors from previously generated tokens. It reduces redundant computation at the cost of increased memory usage. To mitigate this overhead, existing approaches compress KV tensors into lower-bit representations; however, quantization errors can accumulate as more tokens are generated, potentially resulting in undesired outputs. In this paper, we introduce SQuat (Subspace-orthogonal KV cache quantization). It first constructs a subspace spanned by query tensors to capture the most critical task-related information. During key tensor quantization, it enforces that the difference between the (de)quantized and original keys remains orthogonal to this subspace, minimizing the impact of quantization errors on the attention mechanism's outputs. SQuat requires no model fine-tuning, no additional calibration dataset for offline learning, and is grounded in a theoretical framework we develop. Through numerical experiments, we show that our method reduces peak memory by 2.17 to 2.82, improves throughput by 2.45 to 3.60, and achieves more favorable benchmark scores than existing KV cache quantization algorithms.
</details>
<strong><a href="https://arxiv.org/abs/2503.24358">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/SQuat">💻 Code</a> | <a href="https://ai-innovation.team/squat/">🌐 Website</a></strong><br>
<strong>Date:</strong> 2025-03-31<br>
<span class="conference-badge">COLM 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.02421" target="_blank" rel="noopener">Activation-Informed Merging of Large Language Models</a></h3>
<strong>Authors:</strong> Amin Heyrani Nobari, Kaveh Alimohammadi, Ali ArjomandBigdeli, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Faez Ahmed, Navid Azizan<br>
<details>
  <summary>View Abstract</summary>
  Model merging, a method that combines the parameters and embeddings of multiple fine-tuned large language models (LLMs), offers a promising approach to enhance model performance across various tasks while maintaining computational efficiency. This paper introduces Activation-Informed Merging (AIM), a technique that integrates the information from the activation space of LLMs into the merging process to improve performance and robustness. AIM is designed as a flexible, complementary solution that is applicable to any existing merging method. It aims to preserve critical weights from the base model, drawing on principles from continual learning (CL) and model compression. Utilizing a task-agnostic calibration set, AIM selectively prioritizes essential weights during merging. We empirically demonstrate that AIM significantly enhances the performance of merged models across multiple benchmarks. Our findings suggest that considering the activation-space information can provide substantial advancements in the model merging strategies for LLMs, with up to a 40% increase in benchmark performance.
</details>
<strong><a href="https://arxiv.org/abs/2502.02421">📄 Arxiv</a> | <a href="https://github.com/ahnobari/ActivationInformedMerging">💻 Code</a></strong><br>
<strong>Date:</strong> 2025-02-04<br>
<span class="conference-badge">NeurIPS 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.01618" target="_blank" rel="noopener">Rollout Roulette: A Probabilistic Inference Approach to Inference-Time Scaling of LLMs using Particle-Based Monte Carlo Methods</a></h3>
<strong>Authors:</strong> Isha Puri, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Large language models (LLMs) have achieved significant performance gains via scaling up model sizes and/or data. However, recent evidence suggests diminishing returns from such approaches, motivating scaling the computation spent at inference time. Existing inference-time scaling methods, usually with reward models, cast the task as a search problem, which tends to be vulnerable to reward hacking as a consequence of approximation errors in reward models. In this paper, we instead cast inference-time scaling as a probabilistic inference task and leverage sampling-based techniques to explore the typical set of the state distribution of a state-space model with an approximate likelihood, rather than optimize for its mode directly. We propose a novel inference-time scaling approach by adapting particle-based Monte Carlo methods to this task. Our empirical evaluation demonstrates that our methods have a 4-16x better scaling rate over our deterministic search counterparts on various challenging mathematical reasoning tasks. Using our approach, we show that Qwen2.5-Math-1.5B-Instruct can surpass GPT-4o accuracy in only 4 rollouts, while Qwen2.5-Math-7B-Instruct scales to o1 level accuracy in only 32 rollouts. Our work not only presents an effective method to inference-time scaling, but also connects the rich literature in probabilistic inference with inference-time scaling of LLMs to develop more robust algorithms in future work.
</details>
<strong><a href="https://arxiv.org/abs/2502.01618">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/its_hub">💻 Code</a> | <a href="https://probabilistic-inference-scaling.github.io/">🌐 Website</a></strong><br>
<strong>Date:</strong> 2025-02-03<br>
<span class="conference-badge">NeurIPS 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.18509" target="_blank" rel="noopener">Protecting Users From Themselves: Safeguarding Contextual Privacy in Interactions with Conversational Agents</a></h3>
<strong>Authors:</strong> Ivoline Ngong, Swanand Kadhe, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Keerthiram Murugesan, Justin D. Weisz, Amit Dhurandhar, Karthikeyan Natesan Ramamurthy<br>
<details>
  <summary>View Abstract</summary>
  Conversational agents are increasingly woven into individuals' personal lives, yet users often underestimate the privacy risks associated with them. The moment users share information with these agents—such as large language models (LLMs)—their private information becomes vulnerable to exposure. In this paper, we characterize the notion of contextual privacy for user interactions with LLM-based Conversational Agents (LCAs). It aims to minimize privacy risks by ensuring that users (sender) disclose only information that is both relevant and necessary for achieving their intended goals when interacting with LCAs (untrusted receivers). Through a formative design user study, we observe how even "privacy-conscious" users inadvertently reveal sensitive information through indirect disclosures. Based on insights from this study, we propose a locally deployable framework that operates between users and LCAs, identifying and reformulating out-of-context information in user prompts. Our evaluation using examples from ShareGPT shows that lightweight models can effectively implement this framework, achieving strong gains in contextual privacy while preserving the user's intended interaction goals. Notably, about 76% of participants in our human evaluation preferred the reformulated prompts over the original ones, validating the usability and effectiveness of contextual privacy in our proposed framework.
</details>
<strong><a href="https://arxiv.org/abs/2502.18509">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2025-02-22<br>
<span class="conference-badge">ACL 2026</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.00896" target="_blank" rel="noopener">LoR-VP: Low-Rank Visual Prompting for Efficient Vision Model Adaptation</a></h3>
<strong>Authors:</strong> Can Jin, Ying Li, Mingyu Zhao, Shiyu Zhao, Zhenting Wang, Xiaoxiao He, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Tong Che, Dimitris N. Metaxas<br>
<details>
  <summary>View Abstract</summary>
  Visual prompting has gained popularity as a method for adapting pre-trained models to specific tasks, particularly in the realm of parameter-efficient tuning. However, existing visual prompting techniques often pad the prompt parameters around the image, limiting the interaction between the visual prompts and the original image to a small set of patches while neglecting the inductive bias present in shared information across different patches. In this study, we conduct a thorough preliminary investigation to identify and address these limitations. We propose a novel visual prompt design, introducing Low-Rank matrix multiplication for Visual Prompting (LoR-VP), which enables shared and patch-specific information across rows and columns of image pixels. Extensive experiments across seven network architectures and four datasets demonstrate significant improvements in both performance and efficiency compared to state-of-the-art visual prompting methods, achieving up to 6 times faster training times, utilizing 18 times fewer visual prompt parameters, and delivering a 3.1% improvement in performance. The code is available as https://github.com/jincan333/LoR-VP.
</details>
<strong><a href="https://arxiv.org/abs/2502.00896">📄 Arxiv</a> | <a href="https://github.com/jincan333/LoR-VP">💻 Code</a></strong><br>
<strong>Date:</strong> 2025-02-02<br>
<span class="conference-badge">ICLR 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2501.00192" target="_blank" rel="noopener">MLLM-as-a-Judge for Image Safety without Human Labeling</a></h3>
<strong>Authors:</strong> Zhenting Wang, Shuming Hu, Shiyu Zhao, Xiaowen Lin, Felix Juefei-Xu, Zhuowei Li, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Harihar Subramanyam, Li Chen, Jianfa Chen, Nan Jiang, Lingjuan Lyu, Shiqing Ma, Dimitris N. Metaxas, Ankit Jain<br>
<details>
  <summary>View Abstract</summary>
  Image content safety has become a significant challenge with the rise of visual media on online platforms. Meanwhile, in the age of AI-generated content (AIGC), many image generation models are capable of producing harmful content, such as images containing sexual or violent material. Thus, it becomes crucial to identify such unsafe images based on established safety rules. Pre-trained Multimodal Large Language Models (MLLMs) offer potential in this regard, given their strong pattern recognition abilities. Existing approaches typically fine-tune MLLMs with human-labeled datasets, which however brings a series of drawbacks. First, relying on human annotators to label data following intricate and detailed guidelines is both expensive and labor-intensive. Furthermore, users of safety judgment systems may need to frequently update safety rules, making fine-tuning on human-based annotation more challenging. This raises the research question: Can we detect unsafe images by querying MLLMs in a zero-shot setting using a predefined safety constitution (a set of safety rules)? Our research showed that simply querying pre-trained MLLMs does not yield satisfactory results. This lack of effectiveness stems from factors such as the subjectivity of safety rules, the complexity of lengthy constitutions, and the inherent biases in the models. To address these challenges, we propose a MLLM-based method includes objectifying safety rules, assessing the relevance between rules and images, making quick judgments based on debiased token probabilities with logically complete yet simplified precondition chains for safety rules, and conducting more in-depth reasoning with cascaded chain-of-thought processes if necessary. Experiment results demonstrate that our method is highly effective for zero-shot image safety judgment tasks.
</details>
<strong><a href="https://arxiv.org/abs/2501.00192">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-12-31<br>
<span class="conference-badge">CVPR 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2412.13337" target="_blank" rel="noopener">Unveiling the Secret Recipe: A Guide For Supervised Fine-Tuning Small LLMs</a></h3>
<strong>Authors:</strong> <a href="https://scholar.google.com/citations?user=Qpl3KlIAAAAJ&hl=en" target="_blank">Aldo Pareja</a>, <a href="https://scholar.google.com/citations?user=3pLEmAwAAAAJ&hl=en" target="_blank">Nikhil Shivakumar Nayak</a>, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Krishnateja Killamsetty, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, Wenlong Zhao, Seungwook Han, <a href="https://scholar.google.com/citations?user=lV0gYnkAAAAJ&hl=en" target="_blank">Abhishek Bhandwaldar</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Luke Inglis, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  The rise of large language models (LLMs) has created a significant disparity: industrial research labs with their computational resources, expert teams, and advanced infrastructures, can effectively fine-tune LLMs, while individual developers and small organizations face barriers due to limited resources. In this paper, we aim to bridge this gap by presenting a comprehensive study on supervised fine-tuning of LLMs using instruction-tuning datasets spanning diverse knowledge domains and skills. We focus on small-sized LLMs (3B to 7B parameters) for their cost-efficiency and accessibility. We explore various training configurations and strategies across four open-source pre-trained models. We provide detailed documentation of these configurations, revealing findings that challenge several common training practices, including hyperparameter recommendations from TULU and phased training recommended by Orca. Key insights from our work include: (i) larger batch sizes paired with lower learning rates lead to improved model performance on benchmarks such as MMLU, MTBench, and Open LLM Leaderboard; (ii) early-stage training dynamics, such as lower gradient norms and higher loss values, are strong indicators of better final model performance, enabling early termination of sub-optimal runs and significant computational savings; (iii) through a thorough exploration of hyperparameters like warmup steps and learning rate schedules, we provide guidance for practitioners and find that certain simplifications do not compromise performance; and (iv) we observed no significant difference in performance between phased and stacked training strategies, but stacked training is simpler and more sample efficient. With these findings holding robustly across datasets and models, we hope this study serves as a guide for practitioners fine-tuning small LLMs and promotes a more inclusive environment for LLM research.
</details>
<strong><a href="https://arxiv.org/abs/2412.13337">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-12-17<br>
<span class="conference-badge">ICLR 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2412.05723" target="_blank" rel="noopener">Training-Free Bayesianization for Low-Rank Adapters of Large Language Models</a></h3>
<strong>Authors:</strong> Haizhou Shi, Yibin Wang, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Huan Zhang, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a><br>
<details>
  <summary>View Abstract</summary>
  Estimating the uncertainty of responses from Large Language Models (LLMs) remains a critical challenge. While recent Bayesian methods have demonstrated effectiveness in quantifying uncertainty through low-rank weight updates, they typically require complex fine-tuning or post-training procedures. In this paper, we propose Training-Free Bayesianization (TFB), a simple yet theoretically grounded framework that efficiently transforms trained low-rank adapters into Bayesian ones without additional training. TFB systematically searches for the maximally acceptable level of variance in the weight posterior, constrained within a family of low-rank isotropic Gaussian distributions. Our theoretical analysis shows that under mild conditions, this search process is equivalent to KL-regularized variational optimization, a generalized form of variational inference. Through comprehensive experiments, we show that TFB achieves superior uncertainty estimation and generalization compared to existing methods while eliminating the need for complex Bayesianization training procedures.
</details>
<strong><a href="https://arxiv.org/abs/2412.05723">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-12-07<br>
<span class="conference-badge">NeurIPS 2025</span>
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
<h3><a href="https://arxiv.org/abs/2410.08207" target="_blank" rel="noopener">DICE: Discrete Inversion Enabling Controllable Editing for Multinomial Diffusion and Masked Generative Models</a></h3>
<strong>Authors:</strong> Xiaoxiao He, Quan Dao, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Song Wen, Minhao Bai, Di Liu, Han Zhang, Martin Renqiang Min, Felix Juefei-Xu, Chaowei Tan, Bo Liu, Kang Li, Hongdong Li, Junzhou Huang, Faez Ahmed, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Dimitris Metaxas<br>
<details>
  <summary>View Abstract</summary>
  Discrete diffusion models have achieved success in tasks like image generation and masked language modeling but face limitations in controlled content editing. We introduce DICE (Discrete Inversion for Controllable Editing), the first approach to enable precise inversion for discrete diffusion models, including multinomial diffusion and masked generative models. By recording noise sequences and masking patterns during the reverse diffusion process, DICE enables accurate reconstruction and flexible editing of discrete data without the need for predefined masks or attention manipulation. We demonstrate the effectiveness of DICE across both image and text domains, evaluating it on models such as VQ-Diffusion, Paella, and RoBERTa. Our results show that DICE preserves high data fidelity while enhancing editing capabilities, offering new opportunities for fine-grained content manipulation in discrete spaces.
</details>
<strong><a href="https://arxiv.org/abs/2410.08207">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-10-10<br>
<span class="conference-badge">WACV 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2405.21050" target="_blank" rel="noopener">Spectrum-Aware Parameter Efficient Fine-Tuning for Diffusion Models</a></h3>
<strong>Authors:</strong> Xinxi Zhang, Song Wen, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Felix Juefei-Xu, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Junzhou Huang, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Molei Tao, Dimitris N. Metaxas<br>
<details>
  <summary>View Abstract</summary>
  Adapting large-scale pre-trained generative models in a parameter-efficient manner is gaining traction. Traditional methods like low rank adaptation achieve parameter efficiency by imposing constraints but may not be optimal for tasks requiring high representation capacity. We propose a novel spectrum-aware adaptation framework for generative models. Our method adjusts both singular values and their basis vectors of pretrained weights. Using the Kronecker product and efficient Stiefel optimizers, we achieve parameter-efficient adaptation of orthogonal matrices. We introduce Spectral Orthogonal Decomposition Adaptation (SODA), which balances computational efficiency and representation capacity. Extensive evaluations on text-to-image diffusion models demonstrate SODA's effectiveness, offering a spectrum-aware alternative to existing fine-tuning methods.
</details>
<strong><a href="https://arxiv.org/abs/2405.21050">📄 Arxiv</a></strong><br>
<strong>Date:</strong> 2024-05-31<br>
<span class="conference-badge">WACV 2025</span>
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2405.14660" target="_blank" rel="noopener">Implicit In-context Learning</a></h3>
<strong>Authors:</strong> Zhuowei Li, Zihao Xu, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Yunhe Gao, Song Wen, Di Liu, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Dimitris N. Metaxas<br>
<details>
  <summary>View Abstract</summary>
  In-context Learning (ICL) empowers large language models (LLMs) to swiftly adapt to unseen tasks at inference-time by prefixing a few demonstration examples before queries. Despite its versatility, ICL incurs substantial computational and memory overheads compared to zero-shot learning and is sensitive to the selection and order of demonstration examples. In this work, we introduce Implicit In-context Learning (I2CL), an innovative paradigm that reduces the inference cost of ICL to that of zero-shot learning with minimal information loss. I2CL operates by first generating a condensed vector representation, namely a context vector, extracted from the demonstration examples. It then conducts an inference-time intervention through injecting a linear combination of the context vector and query activations back into the model's residual streams. Empirical evaluation on nine real-world tasks across three model architectures demonstrates that I2CL achieves few-shot level performance at zero-shot inference cost, and it exhibits robustness against variations in demonstration examples. Furthermore, I2CL facilitates a novel representation of task-ids, enhancing task similarity detection and fostering effective transfer learning. We also perform a comprehensive analysis and ablation study on I2CL, offering deeper insights into its internal mechanisms. Code is available at https://github.com/LzVv123456/I2CL.
</details>
<strong><a href="https://arxiv.org/abs/2405.14660">📄 Arxiv</a> | <a href="https://github.com/LzVv123456/I2CL">💻 Code</a></strong><br>
<strong>Date:</strong> 2024-05-23<br>
<span class="conference-badge">ICLR 2025</span>
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
