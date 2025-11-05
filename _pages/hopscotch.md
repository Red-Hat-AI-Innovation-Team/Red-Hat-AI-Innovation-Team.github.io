---
layout: page
title: ""
permalink: /hopscotch/
description: Hopscotch - Discovering and skipping redundant attention blocks in language models. Achieve model compression without modifying weights or requiring retraining data.
---

<style>
/* Hide the empty page title to remove extra margin */
.page__info {
  display: none !important;
}

/* Override theme container width for this page - target content area specifically */
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
  
  .paper-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

@media only screen and (max-width: 576px) {
  .content .container {
    max-width: none !important;
  }
  
  .paper-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

.paper-container {
  max-width: 65%;
  margin: 0 auto;
  padding: 20px;
  font-family: 'Times New Roman', serif;
  line-height: 1.6;
}

.paper-title {
  text-align: center;
  font-size: 2.5em;
  font-weight: bold;
  margin-bottom: 20px;
  color: var(--heading-font-color);
}

.conference {
  text-align: center;
  font-size: 1.5em;
  color: var(--text-alt-color);
  margin-bottom: 30px;
}

.authors {
  text-align: center;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.affiliations {
  text-align: center;
  font-size: 1.1em;
  margin-bottom: 30px;
}

.nav-links {
  text-align: center;
  margin: 30px 0;
}

.nav-links a {
  display: inline-block;
  margin: 0 15px;
  padding: 10px 20px;
  background-color: var(--background-alt-color);
  border: 2px solid var(--border-color);
  border-radius: 5px;
  text-decoration: none;
  color: var(--text-color);
  font-weight: bold;
  transition: all 0.3s ease;
}

.nav-links a:hover {
  background-color: var(--background-color);
  border-color: var(--border-color);
}

.section-box {
  border: 2px solid var(--border-color);
  border-radius: 10px;
  padding: 20px;
  margin: 30px 0;
  background-color: var(--background-alt-color);
}

.section-title {
  font-size: 1.8em;
  font-weight: bold;
  margin-bottom: 15px;
  color: var(--heading-font-color);
  text-align: center;
}

.method-visual {
  text-align: center;
  margin: 20px 0;
}

.method-visual img {
  max-width: 100%;
  height: auto;
  border: 1px solid var(--border-color);
  border-radius: 5px;
}

.citation-box {
  background-color: var(--article-background);
  border: 1px solid var(--border-color);
  border-radius: 5px;
  padding: 20px;
  margin: 20px 0;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  overflow-x: auto;
}

.citation-box pre,
.citation-box code {
  background-color: transparent;
  color: var(--text-color);
  margin: 0;
  padding: 0;
}

@media (max-width: 768px) {
  .paper-title {
    font-size: 2em;
  }
  
  .nav-links a {
    display: block;
    margin: 10px 0;
  }
}

</style>

<div class="paper-container">
  <h1 class="paper-title">Hopscotch: Discovering and Skipping Redundancies in Language Models</h1>
  
  <div class="conference">EMNLP 2025</div>
  
  <div class="authors">
    <span class="author-link">Mustafa Eyceoz</span><sup>1</sup>,
    <span class="author-link">Nikhil Shivakumar Nayak</span><sup>1</sup>,
    <a href="https://haowang94.github.io" target="_blank" class="author-link">Hao Wang</a><sup>1</sup>,
    <a href="https://phymhan.github.io" target="_blank" class="author-link">Ligong Han</a><sup>1</sup>,
    <a href="https://akashgit.github.io" target="_blank" class="author-link">Akash Srivastava</a><sup>2</sup>
  </div>
  
  <div class="affiliations">
    Red Hat AI Innovation<sup>1</sup> IBM Core AI<sup>2</sup>
  </div>
  
  <div class="nav-links">
    <a href="https://arxiv.org/abs/2506.03303" target="_blank">Paper</a>
    <a href="https://github.com/Red-Hat-AI-Innovation-Team/hopscotch" target="_blank">Code</a>
    <a href="#citation">BibTeX</a>
    <a href="https://youtube.com/live/1PGHYKqrE94?si=OkjefuYN7hK76NWU" target="_blank">Video</a>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Abstract</h2>
    <p>Modern causal language models stack many attention blocks to improve performance, but not all blocks are necessary for every task. We propose Hopscotch, a simple yet effective method that identifies and skips attention blocks with least contributions to a task and adapts to preserve output quality. Hopscotch jointly optimizes which blocks to skip and how to scale the outputs of the remaining layers. By introducing lightweight, trainable scaling parameters to attention and MLP blocks, it mitigates distribution shifts in hidden states caused by removing attention blocks. Hopscotch does not modify model weights or require access to pretraining or instruction-tuning data, and is compatible with existing model compression techniques. When applied to Llama-3.1-8B and Qwen2.5-7B, Hopscotch achieves less than a 2% drop in performance even after skipping four attention blocks.</p>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Method Overview</h2>
    <div class="method-visual">
      <img src="/images/hopscotch/Hopscotch Poster-1.png" alt="Hopscotch Method Overview">
    </div>
    <p>Hopscotch employs an iterative block selection process to identify redundant attention blocks. The method introduces lightweight scaling parameters to both attention and MLP components, enabling the model to adapt after block removal without modifying the original weights. This approach ensures compatibility with existing compression techniques and requires no access to original pretraining data.</p>
  </div>
  
  <div class="section-box" id="citation">
    <h2 class="section-title">Citation</h2>
    <pre><code>@misc{eyceoz2025hopscotchdiscoveringskippingredundancies,
    title={Hopscotch: Discovering and Skipping Redundancies in Language Models}, 
    author={Mustafa Eyceoz and Nikhil Shivakumar Nayak and Hao Wang and Ligong Han and Akash Srivastava},
    year={2025},
    eprint={2506.03303},
    archivePrefix={arXiv},
    primaryClass={cs.CL},
    url={https://arxiv.org/abs/2506.03303}
}</code></pre>
  </div>
</div>

