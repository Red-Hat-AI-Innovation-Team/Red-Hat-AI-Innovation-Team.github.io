---
layout: page
title: Papers
permalink: /papers/
---

<div class="papers-container">
  <div class="papers-intro">
    <p>Our research papers and technical publications on AI, machine learning, and large language models.</p>
  </div>

  <div class="papers-grid">
    <!-- Repository Knowledge Agent Paper -->
    <div class="paper-card">
      <div class="paper-header">
        <h3 class="paper-title">
          <a href="/papers/repository-knowledge-agent/" target="_blank">
            Repository Knowledge Agent: Intelligent Code Understanding and Generation
          </a>
        </h3>
        <div class="paper-authors">
          AI Innovation Team
        </div>
        <div class="paper-date">2025</div>
      </div>
      <div class="paper-abstract">
        A comprehensive white paper on intelligent code understanding and generation using repository knowledge agents for enhanced software development workflows.
      </div>
      <div class="paper-links">
        <a href="/papers/repository-knowledge-agent/" class="paper-link">Read Paper</a>
        <a href="/papers/Repo_Knowledge_Agent_White_paper.pdf" class="paper-link" target="_blank">PDF</a>
      </div>
    </div>
  </div>
</div>

<style>
.papers-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem 0;
}

.papers-intro {
  text-align: center;
  margin-bottom: 3rem;
  font-size: 1.1rem;
  color: var(--text-color);
  opacity: 0.8;
}

.papers-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.paper-card {
  background: var(--background-color);
  border: 1px solid var(--border-color);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.paper-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.paper-header {
  margin-bottom: 1rem;
}

.paper-title {
  margin: 0 0 0.5rem 0;
  font-size: 1.3rem;
  line-height: 1.4;
}

.paper-title a {
  color: var(--title-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

.paper-title a:hover {
  color: var(--accent-color);
}

.paper-authors {
  font-size: 0.9rem;
  color: var(--text-color);
  opacity: 0.8;
  margin-bottom: 0.5rem;
  font-style: italic;
}

.paper-date {
  font-size: 0.8rem;
  color: var(--text-color);
  opacity: 0.6;
  margin-bottom: 1rem;
}

.paper-abstract {
  font-size: 0.95rem;
  line-height: 1.6;
  color: var(--text-color);
  margin-bottom: 1.5rem;
  opacity: 0.9;
}

.paper-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.paper-link {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: var(--accent-color);
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-size: 0.9rem;
  transition: all 0.3s ease;
}

.paper-link:hover {
  background: var(--accent-color-hover);
  transform: translateY(-1px);
}

@media (max-width: 768px) {
  .papers-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
  
  .paper-card {
    padding: 1rem;
  }
  
  .paper-title {
    font-size: 1.1rem;
  }
}
</style> 