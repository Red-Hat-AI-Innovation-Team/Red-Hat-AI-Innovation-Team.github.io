---
layout: page
title: ""
permalink: /squat/
---

<style>
/* Override theme container width for this page */
.container {
  max-width: none !important;
  width: 100% !important;
}

/* Override all responsive breakpoints */
@media only screen and (max-width: 1140px) {
  .container {
    max-width: none !important;
  }
}

@media only screen and (max-width: 1024px) {
  .container {
    max-width: none !important;
  }
}

@media only screen and (max-width: 768px) {
  .container {
    max-width: none !important;
  }
  
  .paper-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

@media only screen and (max-width: 576px) {
  .container {
    max-width: none !important;
  }
  
  .paper-container {
    max-width: 100% !important;
    padding: 10px !important;
  }
}

.paper-container {
  max-width: 2250px;
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
  color: #333;
}

.conference {
  text-align: center;
  font-size: 1.5em;
  color: #666;
  margin-bottom: 30px;
}

.authors {
  text-align: center;
  font-size: 1.2em;
  margin-bottom: 10px;
}

.author-link {
  color: #0066cc;
  text-decoration: none;
}

.author-link:hover {
  text-decoration: underline;
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
  background-color: #f0f0f0;
  border: 2px solid #ddd;
  border-radius: 5px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
  transition: all 0.3s ease;
}

.nav-links a:hover {
  background-color: #e0e0e0;
  border-color: #bbb;
}

.section-box {
  border: 2px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  margin: 30px 0;
  background-color: #fafafa;
}

.section-title {
  font-size: 1.8em;
  font-weight: bold;
  margin-bottom: 15px;
  color: #333;
  text-align: center;
}

.method-visual {
  text-align: center;
  margin: 20px 0;
}

.method-visual img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.results-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin: 20px 0;
}

.result-item img {
  max-width: 100%;
  height: auto;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.contributions-list {
  list-style: none;
  padding: 0;
}

.contributions-list li {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 15px;
  margin: 10px 0;
}

.citation-box {
  background-color: #f5f5f5;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 20px;
  margin: 20px 0;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
  overflow-x: auto;
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
  <h1 class="paper-title">SQuat: Subspace-orthogonal KV Cache Quantization</h1>
  
  <div class="conference">COLM 2025</div>
  
  <div class="authors">
    <a href="https://haowang94.github.io" target="_blank" class="author-link">Hao Wang</a><sup>*,1</sup>
    <a href="https://phymhan.github.io" target="_blank" class="author-link">Ligong Han</a><sup>*,1</sup>
    <a href="https://xuk.ai" target="_blank" class="author-link">Kai Xu</a><sup>1</sup>
    <a href="https://akashgit.github.io" target="_blank" class="author-link">Akash Srivastava</a><sup>1</sup>
  </div>
  
  <div class="affiliations">
    <sup>*</sup>Equal contribution <sup>1</sup>Red Hat AI Innovation
  </div>
  
  <div class="nav-links">
    <a href="https://arxiv.org/abs/2503.24358" target="_blank">Paper</a>
    <a href="https://github.com/Red-Hat-AI-Innovation-Team/SQuat" target="_blank">Code</a>
    <a href="#citation">BibTeX</a>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Abstract</h2>
    <p>We introduce a new KV cache quantization algorithm: SQuat (Subspace-orthogonal KV cache quantization). SQuat is training-free, requires no calibration data, runs on-the-fly, and is grounded in a theoretical framework we developed. Empirically, it reduces GPU peak memory by 2.17× to 2.82×, improves throughput by 2.45× to 3.60×, and achieves more favorable benchmark scores than existing KV cache quantization algorithms.</p>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Method</h2>
    <div class="method-visual">
      <img src="/images/squat/kvcache.png" alt="KV Cache Quantization Overview">
    </div>
    <p>SQuat first constructs a subspace that captures the most critical task-related information. During key tensor quantization, it ensures that the difference between the (de)quantized and original keys remains orthogonal to this subspace, thereby minimizing the impact of quantization errors on the attention mechanism's outputs.</p>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Results</h2>
    <div class="method-visual">
      <img src="/images/squat/results.png" alt="SQuat Method Overview">
    </div>
    <p>Our experimental evaluation demonstrates significant improvements across multiple dimensions:</p>
    <div class="results-grid">
      <div class="result-item">
        <img src="/images/squat/table1.png" alt="Performance Results">
      </div>
      <div class="result-item">
        <img src="/images/squat/table2.png" alt="Benchmark Comparison">
      </div>
    </div>
  </div>
  
  
  <div class="section-box" id="citation">
    <h2 class="section-title">Citation</h2>
    <pre><code>@inproceedings{wang2025squat,
    title={SQuat: Subspace-orthogonal KV Cache Quantization},
    author={Wang, Hao and Han, Ligong and Xu, Kai and Srivastava, Akash},
    booktitle={Conference on Language Modeling},
    year={2025}
}</code></pre>
  </div>
</div>