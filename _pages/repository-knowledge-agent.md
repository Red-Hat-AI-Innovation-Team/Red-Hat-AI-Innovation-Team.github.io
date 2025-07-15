---
layout: page
title: Repository Knowledge Agent
permalink: /repository-knowledge-agent/
---

<div class="paper-detail-container">
  <div class="paper-header">
    <h1 class="paper-title">Teaching LLMs to Understand Code Repositories Using Synthetic Knowledge Data</h1>
    <div class="paper-meta">
      <div class="paper-authors">Red Hat AI Innovation Team</div>
      <div class="paper-date">2025</div>
      <div class="paper-type">White Paper</div>
    </div>
  </div>

  <div class="paper-content">
    <div class="paper-abstract">
      <h2>Abstract</h2>
      <p>
        Large language models (LLMs) often struggle to answer questions grounded in complex, domain-specific codebases, especially when deployed in private environments using smaller, open-weight models. These limitations arise from insufficient context understanding, weak reasoning capabilities, and a lack of alignment with specialized terminology or architecture. In this work, we present a synthetic data-driven framework for knowledge infusion using sdg_hub, an open-source tool developed to generate high-quality, document-grounded training data.

        Our method transforms curated technical documentation, including annotated code, example notebooks, and code documentation, into synthetic question–answer pairs and reasoning traces using teacher LLMs. We fine-tune Qwen 3 family models on this data.

        This targeted fine-tuning approach significantly improves the model's factual accuracy and reasoning performance on repository-specific tasks. Our results demonstrate that small LLMs, when properly customized, can serve as capable domain experts, complementing RAG pipelines while operating in secure, cost-efficient deployments.
      </p>
    </div>

    <div class="paper-download">
      <a href="/papers/Repo_Knowledge_Agent_White_paper.pdf" class="download-button" target="_blank">
        <i class="ion ion-md-download"></i>
        Download PDF
      </a>
    </div>
    
  </div>
</div>

<style>
.paper-detail-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem 0;
}

.paper-header {
  text-align: center;
  margin-bottom: 3rem;
  padding-bottom: 2rem;
  border-bottom: 2px solid var(--border-color);
}

.paper-title {
  font-size: 2.2rem;
  line-height: 1.3;
  margin-bottom: 1rem;
  color: var(--title-color);
}

.paper-meta {
  display: flex;
  justify-content: center;
  gap: 2rem;
  flex-wrap: wrap;
  font-size: 0.9rem;
  color: var(--text-color);
  opacity: 0.8;
}

.paper-authors {
  font-style: italic;
}

.paper-type {
  background: var(--accent-color);
  color: white;
  padding: 0.2rem 0.8rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

.paper-content {
  line-height: 1.7;
}

.paper-abstract {
  margin-bottom: 3rem;
}

.paper-abstract h2 {
  color: var(--title-color);
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.paper-abstract p {
  font-size: 1.1rem;
  color: var(--text-color);
  opacity: 0.9;
}

.paper-download {
  text-align: center;
  margin: 3rem 0;
}

.download-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: #007bff;
  color: white !important;
  text-decoration: none;
  padding: 1rem 2rem;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: 500;
  transition: all 0.3s ease;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  border: none;
  cursor: pointer;
}

.download-button:hover {
  background: #0056b3;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
  color: white !important;
}

.download-button i {
  font-size: 1.2rem;
}

.paper-sections {
  margin-bottom: 3rem;
}

.paper-sections h2 {
  color: var(--title-color);
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
}

.paper-sections ul {
  list-style: none;
  padding: 0;
}

.paper-sections li {
  margin-bottom: 1rem;
  padding-left: 1.5rem;
  position: relative;
  color: var(--text-color);
  line-height: 1.6;
}

.paper-sections li:before {
  content: "•";
  color: var(--accent-color);
  font-weight: bold;
  position: absolute;
  left: 0;
}

.paper-impact {
  background: var(--background-color);
  border-left: 4px solid var(--accent-color);
  padding: 2rem;
  border-radius: 0 8px 8px 0;
}

.paper-impact h2 {
  color: var(--title-color);
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.paper-impact p {
  color: var(--text-color);
  line-height: 1.7;
  font-size: 1rem;
}

@media (max-width: 768px) {
  .paper-title {
    font-size: 1.8rem;
  }
  
  .paper-meta {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .paper-download {
    padding: 1.5rem;
  }
  
  .download-button {
    padding: 0.8rem 1.5rem;
    font-size: 1rem;
  }
}
</style> 