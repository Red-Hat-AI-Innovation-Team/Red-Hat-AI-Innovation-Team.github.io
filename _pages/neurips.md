---
layout: page
title: ""
permalink: /neurips/
description: AI Innovation Team at NeurIPS 2025 - Meet us and learn about our latest research on LLMs, inference-time scaling, and AI optimization.
---

<style>
/* Hide the empty page title to remove extra margin */
.page__info {
  display: none !important;
}

/* Override theme container width for this page */
.content .container {
  max-width: none !important;
  width: 100% !important;
}

.page__content {
  max-width: none !important;
  width: 100% !important;
}

.page {
  max-width: none !important;
  width: 100% !important;
}

/* Override all responsive breakpoints for content containers */
@media only screen and (max-width: 1140px) {
  .content .container {
    max-width: none !important;
  }
}

@media only screen and (max-width: 1024px) {
  .content .container {
    max-width: none !important;
  }
}

@media only screen and (max-width: 768px) {
  .content .container {
    max-width: none !important;
  }
  
  .neurips-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

@media only screen and (max-width: 576px) {
  .content .container {
    max-width: none !important;
  }
  
  .neurips-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

.neurips-container {
  max-width: 740px;
  margin: 0 auto;
  padding: 20px;
  line-height: 1.6;
}

.hero-section {
  text-align: center;
  padding: 40px 20px;
  background: linear-gradient(135deg, var(--background-alt-color) 0%, var(--article-background) 100%);
  border-radius: 15px;
  margin-bottom: 40px;
  border: 2px solid var(--border-color);
}

.main-title {
  font-size: 3em;
  font-weight: bold;
  margin-bottom: 10px;
  color: var(--heading-font-color);
}

.conference-info {
  font-size: 1.5em;
  color: var(--text-alt-color);
  margin-bottom: 20px;
}

.team-name {
  font-size: 1.3em;
  font-weight: bold;
  color: var(--text-color);
  margin-top: 20px;
}

.intro-text {
  font-size: 1.1em;
  color: var(--text-color);
  max-width: 800px;
  margin: 20px auto;
  line-height: 1.8;
}

.papers-section {
  margin: 40px 0;
}

.section-header {
  font-size: 2em;
  font-weight: bold;
  text-align: center;
  margin-bottom: 30px;
  color: var(--heading-font-color);
}

.team-section {
  margin: 50px 0;
  padding: 40px 20px;
  background-color: var(--background-alt-color);
  border-radius: 15px;
  border: 2px solid var(--border-color);
}

.team-section h2 {
  text-align: center;
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 30px;
  color: var(--heading-font-color);
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
  gap: 20px;
  max-width: 800px;
  margin: 0 auto;
}

.team-member {
  text-align: center;
}

.team-member img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--border-color);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-member img:hover {
  transform: scale(1.1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.team-member-name {
  margin-top: 10px;
  font-size: 0.9em;
  font-weight: 500;
  color: var(--text-color);
}

@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}

.contact-section {
  text-align: center;
  padding: 40px 20px;
  background-color: var(--background-alt-color);
  border-radius: 15px;
  margin-top: 50px;
  border: 2px solid var(--border-color);
}

.contact-title {
  font-size: 2em;
  font-weight: bold;
  margin-bottom: 20px;
  color: var(--heading-font-color);
}

.qr-code-container {
  margin: 30px auto;
  max-width: 300px;
}

.qr-placeholder {
  width: 300px;
  height: 300px;
  background-color: var(--article-background);
  border: 2px dashed var(--border-color);
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  font-size: 1.2em;
  color: var(--text-alt-color);
  margin: 0 auto;
}

.contact-info {
  margin-top: 20px;
  font-size: 1.1em;
}

.contact-links {
  margin-top: 20px;
}

.contact-links a {
  display: inline-block;
  margin: 0 15px;
  padding: 12px 25px;
  background-color: var(--background-color);
  border: 2px solid var(--border-color);
  border-radius: 5px;
  text-decoration: none;
  color: var(--text-color);
  font-weight: bold;
  transition: all 0.3s ease;
}

.contact-links a:hover {
  background-color: var(--background-alt-color);
  transform: translateY(-2px);
}

@media (max-width: 768px) {
  .main-title {
    font-size: 2em;
  }
  
  .conference-info {
    font-size: 1.2em;
  }
  
  .contact-links a {
    display: block;
    margin: 10px 0;
  }
}

</style>

<div class="neurips-container">
  <!-- Hero Section -->
  <div class="hero-section">
    <h1 class="main-title">AI Innovation at NeurIPS 2025</h1>
    <div class="conference-info">December 2-7, 2025 | San Diego Convention Center</div>
    <div class="team-name">Red Hat AI Innovation Team</div>
    <p class="intro-text">
      We're excited to present our latest research on large language models, inference-time scaling, 
      and AI optimization. Come visit us to learn about our work and discuss opportunities for collaboration!
    </p>
  </div>

  <!-- Papers Section -->
  <div class="papers-section">
    <h2 class="section-header">Our NeurIPS 2025 Papers</h2>
    
<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2412.05723" target="_blank" rel="noopener">Training-Free Bayesianization for Low-Rank Adapters of Large Language Models</a></h3>
<strong>Authors:</strong> Haizhou Shi, Yibin Wang, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Huan Zhang, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a><br>
<details>
  <summary>View Abstract</summary>
  Estimating the uncertainty of responses from Large Language Models (LLMs) remains a critical challenge. While recent Bayesian methods have demonstrated effectiveness in quantifying uncertainty through low-rank weight updates, they typically require complex fine-tuning or post-training procedures. In this paper, we propose Training-Free Bayesianization (TFB), a simple yet theoretically grounded framework that efficiently transforms trained low-rank adapters into Bayesian ones without additional training. TFB systematically searches for the maximally acceptable level of variance in the weight posterior, constrained within a family of low-rank isotropic Gaussian distributions. Our theoretical analysis shows that under mild conditions, this search process is equivalent to KL-regularized variational optimization, a generalized form of variational inference. Through comprehensive experiments, we show that TFB achieves superior uncertainty estimation and generalization compared to existing methods while eliminating the need for complex Bayesianization training procedures.
</details>
<strong><a href="https://arxiv.org/abs/2412.05723">📄 Arxiv</a></strong><br>
<strong>Presentation:</strong> Thursday, December 4, 2025<br>
<strong>Time:</strong> 11:00 AM - 2:00 PM (PST)<br>
<strong>Location:</strong> Exhibit Hall C, D, E
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.02421" target="_blank" rel="noopener">Activation-Informed Merging of Large Language Models</a></h3>
<strong>Authors:</strong> Amin Heyrani Nobari, Kaveh Alim, Ali ArjomandBigdeli, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a>, Faez Ahmed, Navid Azizan<br>
<details>
  <summary>View Abstract</summary>
  Model merging, a method that combines the parameters and embeddings of multiple fine-tuned large language models (LLMs), offers a promising approach to enhance model performance across various tasks while maintaining computational efficiency. This paper introduces Activation-Informed Merging (AIM), a technique that integrates the information from the activation space of LLMs into the merging process to improve performance and robustness. AIM is designed as a flexible, complementary solution that is applicable to any existing merging method. It aims to preserve critical weights from the base model, drawing on principles from continual learning (CL) and model compression. Utilizing a task-agnostic calibration set, AIM selectively prioritizes essential weights during merging. We empirically demonstrate that AIM significantly enhances the performance of merged models across multiple benchmarks. Our findings suggest that considering the activation-space information can provide substantial advancements in the model merging strategies for LLMs, with up to a 40% increase in benchmark performance.
</details>
<strong><a href="https://arxiv.org/abs/2502.02421">📄 Arxiv</a> | <a href="https://github.com/ahnobari/ActivationInformedMerging">💻 Code</a></strong><br>
<strong>Presentation:</strong> Friday, December 5, 2025<br>
<strong>Time:</strong> 11:00 AM - 2:00 PM (PST)<br>
<strong>Location:</strong> Exhibit Hall C, D, E
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2502.01618" target="_blank" rel="noopener">Rollout Roulette: A Probabilistic Inference Approach to Inference-Time Scaling of LLMs using Particle-Based Monte Carlo Methods</a></h3>
<strong>Authors:</strong> Isha Puri, <a href="https://scholar.google.com/citations?user=O71amfMAAAAJ&hl=en" target="_blank">Shivchander Sudalairaj</a>, <a href="https://scholar.google.com/citations?user=ohsEWqsAAAAJ&hl=en" target="_blank">Guangxuan Xu</a>, <a href="https://scholar.google.com/citations?user=kf3C60wAAAAJ" target="_blank">Kai Xu</a>, <a href="https://scholar.google.com/citations?user=2h6SZeEAAAAJ&hl=en" target="_blank">Akash Srivastava</a><br>
<details>
  <summary>View Abstract</summary>
  Large language models (LLMs) have achieved significant performance gains via scaling up model sizes and/or data. However, recent evidence suggests diminishing returns from such approaches, motivating scaling the computation spent at inference time. Existing inference-time scaling methods, usually with reward models, cast the task as a search problem, which tends to be vulnerable to reward hacking as a consequence of approximation errors in reward models. In this paper, we instead cast inference-time scaling as a probabilistic inference task and leverage sampling-based techniques to explore the typical set of the state distribution of a state-space model with an approximate likelihood, rather than optimize for its mode directly. We propose a novel inference-time scaling approach by adapting particle-based Monte Carlo methods to this task. Our empirical evaluation demonstrates that our methods have a 4-16x better scaling rate over our deterministic search counterparts on various challenging mathematical reasoning tasks. Using our approach, we show that Qwen2.5-Math-1.5B-Instruct can surpass GPT-4o accuracy in only 4 rollouts, while Qwen2.5-Math-7B-Instruct scales to o1 level accuracy in only 32 rollouts. Our work not only presents an effective method to inference-time scaling, but also connects the rich literature in probabilistic inference with inference-time scaling of LLMs to develop more robust algorithms in future work.
</details>
<strong><a href="https://arxiv.org/abs/2502.01618">📄 Arxiv</a> | <a href="https://github.com/Red-Hat-AI-Innovation-Team/its_hub">💻 Code</a> | <a href="https://probabilistic-inference-scaling.github.io/">🌐 Website</a></strong><br>
<strong>Presentation:</strong> Friday, December 5, 2025<br>
<strong>Time:</strong> 11:00 AM - 2:00 PM (PST)<br>
<strong>Location:</strong> Exhibit Hall C, D, E
</div>

<div class="publication-card">
<h3><a href="https://www.arxiv.org/abs/2506.09338" target="_blank" rel="noopener">Know What You Don't Know: Uncertainty Calibration of Process Reward Models</a></h3>
<strong>Authors:</strong> Young-Jin Park, Kristjan Greenewald, Kaveh Alim, <a href="https://scholar.google.com/citations?hl=en&user=A3WtYhAAAAAJ" target="_blank">Hao Wang</a>, Navid Azizan<br>
<details>
  <summary>View Abstract</summary>
  Process reward models (PRMs) play a central role in guiding inference-time scaling algorithms for large language models (LLMs). However, we observe that even state-of-the-art PRMs can be poorly calibrated. Specifically, they tend to overestimate the success probability that a partial reasoning step will lead to a correct final answer, particularly when smaller LLMs are used to complete the reasoning trajectory. To address this, we present a calibration approach -- performed via quantile regression -- that adjusts PRM outputs to better align with true success probabilities. Leveraging these calibrated success estimates and their associated confidence bounds, we introduce an instance-adaptive scaling (IAS) framework that dynamically adjusts the compute budget based on the estimated likelihood that a partial reasoning trajectory will yield a correct final answer. Unlike conventional methods that allocate a fixed number of reasoning trajectories per query, this approach adapts to each instance and reasoning step when using our calibrated PRMs. Experiments on mathematical reasoning benchmarks show that (i) our PRM calibration method achieves small calibration error, outperforming the baseline methods, (ii) calibration is crucial for enabling effective IAS, and (iii) the proposed IAS strategy reduces inference costs while maintaining final answer accuracy, utilizing less compute on more confident problems as desired.
</details>
<strong><a href="https://www.arxiv.org/abs/2506.09338">📄 Arxiv</a></strong><br>
<strong>Presentation:</strong> Friday, December 5, 2025<br>
<strong>Time:</strong> 4:30 PM - 7:30 PM (PST)<br>
<strong>Location:</strong> Exhibit Hall C, D, E
</div>

<div class="publication-card">
<h3><a href="https://arxiv.org/abs/2510.23667" target="_blank" rel="noopener">Optimize Any Topology: A Foundation Model for Shape- and Resolution-Free Topology Optimization</a></h3>
<strong>Authors:</strong> Amin Heyrani Nobari, Lyle Regenwetter, Cyril Picard, <a href="https://scholar.google.com/citations?user=n2v43R4AAAAJ&hl=en" target="_blank">Ligong Han</a>, Faez Ahmed<br>
<details>
  <summary>View Abstract</summary>
  Structural topology optimization (TO) is central to engineering design but remains computationally intensive due to complex physics and hard constraints. Existing deep-learning methods are limited to fixed square grids, a few hand-coded boundary conditions, and post-hoc optimization, preventing general deployment. We introduce Optimize Any Topology (OAT), a foundation-model framework that directly predicts minimum-compliance layouts for arbitrary aspect ratios, resolutions, volume fractions, loads, and fixtures. OAT combines a resolution- and shape-agnostic autoencoder with an implicit neural-field decoder and a conditional latent-diffusion model trained on OpenTO, a new corpus of 2.2 million optimized structures covering 2 million unique boundary-condition configurations. On four public benchmarks and two challenging unseen tests, OAT lowers mean compliance up to 90% relative to the best prior models and delivers sub-1 second inference on a single GPU across resolutions from 64 x 64 to 256 x 256 and aspect ratios as high as 10:1. These results establish OAT as a general, fast, and resolution-free framework for physics-aware topology optimization and provide a large-scale dataset to spur further research in generative modeling for inverse design.
</details>
<strong><a href="https://arxiv.org/abs/2510.23667">📄 Arxiv</a></strong><br>
<strong>Presentation:</strong> Friday, December 5, 2025<br>
<strong>Time:</strong> 4:30 PM - 7:30 PM (PST)<br>
<strong>Location:</strong> Exhibit Hall C, D, E
</div>
  </div>

  <!-- Team Section -->
  <div class="team-section">
    <h2>Who Will Be There</h2>
    <div class="team-grid">
      <div class="team-member">
        <img src="/images/about/Headshots/akash.jpg" alt="Akash Srivastava">
        <div class="team-member-name">Akash Srivastava</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/Cole.png" alt="Cole Hurwitz">
        <div class="team-member-name">Cole Hurwitz</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/giorgio.jpg" alt="Giorgio Giannone">
        <div class="team-member-name">Giorgio Giannone</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/gx.jpg" alt="Guangxuan Xu">
        <div class="team-member-name">Guangxuan Xu</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/hao.jpg" alt="Hao Wang">
        <div class="team-member-name">Hao Wang</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/kai.png" alt="Kai Xu">
        <div class="team-member-name">Kai Xu</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/ligong.jpg" alt="Ligong Han">
        <div class="team-member-name">Ligong Han</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/mustafa.jpg" alt="Mustafa Eyceoz">
        <div class="team-member-name">Mustafa Eyceoz</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/nikhil.jpeg" alt="Nikhil Nayak">
        <div class="team-member-name">Nikhil Nayak</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/oleg.jpeg" alt="Oleg Silkin">
        <div class="team-member-name">Oleg Silkin</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/rohan.jpg" alt="Rohan Awhad">
        <div class="team-member-name">Rohan Awhad</div>
      </div>
      <div class="team-member">
        <img src="/images/about/Headshots/shiv.png" alt="Shivchander Sudalairaj">
        <div class="team-member-name">Shivchander Sudalairaj</div>
      </div>
    </div>
  </div>

  <!-- Contact Section -->
  <div class="contact-section">
    <h2 class="contact-title">Connect With Us</h2>
    <p class="intro-text">
      Interested in learning more about our research or exploring collaboration opportunities? 
      Scan the QR code below or reach out to us directly!
    </p>
    
    <div class="qr-code-container">
      <div class="qr-placeholder">
        [QR CODE PLACEHOLDER]
      </div>
    </div>
    
    <div class="contact-info">
      <p>Scan to connect with the Red Hat AI Innovation Team</p>
    </div>
    
    <div class="contact-links">
      <a href="/contact/">📧 Contact Us</a>
      <a href="/publications/">📚 All Publications</a>
      <a href="https://github.com/Red-Hat-AI-Innovation-Team" target="_blank">💻 GitHub</a>
      <a href="/">🏠 Team Website</a>
    </div>
  </div>
</div>

