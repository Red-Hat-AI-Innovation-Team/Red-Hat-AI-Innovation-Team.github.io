---
layout: page
title: "SpecBench"
permalink: /specbench/
description: SpecBench - A benchmark for evaluating AI agents' ability to translate vague user intent into structured specifications through collaborative interaction.
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

.results-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin: 20px 0;
}

.result-item {
  text-align: center;
}

.result-item img {
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
  <h1 class="paper-title">Turning Intent into Specifications: A Benchmark and an Interactive User-Assistant Agent</h1>
  
  <div class="authors">
    <a href="https://haowang94.github.io" target="_blank" class="author-link">Hao Wang</a><sup>1,2</sup>,
    <a href="https://phymhan.github.io" target="_blank" class="author-link">Ligong Han</a><sup>1,2</sup>,
    <a href="https://xuk.ai" target="_blank" class="author-link">Kai Xu</a><sup>1,2</sup>,
    <a href="https://akashgit.github.io" target="_blank" class="author-link">Akash Srivastava</a><sup>2,3</sup>
  </div>
  
  <div class="affiliations">
    <sup>1</sup>Red Hat AI Innovation <sup>2</sup>MIT-IBM Watson AI Lab <sup>3</sup>IBM Core AI
  </div>
  
  <div class="nav-links">
    <a href="https://haowang94.github.io/files/specbench.pdf" target="_blank">Paper</a>
    <a href="https://github.com/haowang94/intent2spec" target="_blank">Code</a>
    <a href="https://huggingface.co/datasets/haowang94/specbench" target="_blank">Data</a>
    <a href="https://haowang94.github.io/blog/specbench/" target="_blank">Blog</a>
    <a href="#citation">BibTeX</a>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Abstract</h2>
    <p>Today's agents are highly effective at implementing well-scoped software design plans, but user intent is often vague and admits multiple equally valid solutions. In this paper, we introduce SpecBench, a new benchmark for evaluating an agent's ability to translate user intent into a structured, executable specification that aligns with user preferences. The agent is given access to past user conversations and may interact with the user for a fixed number of rounds to ask clarifying questions. We find that existing agents exhibit two extreme behaviors: they either (i) struggle to collaborate proactively with users, entering implementation mode too quickly while overestimating their understanding of user preferences, or (ii) exhaust their question budget by asking about every ambiguous design choice. To address this limitation, we introduce a user-assistant agent: Buddy. It follows a workflow inspired by classical morphological analysis, decomposing user intent into a structured space of design dimensions and candidate choices. It then creates simulated users to evaluate these choices, before engaging the real user to resolve remaining ambiguities and finalize the specification. By shifting the focus from execution to specification, SpecBench and Buddy emphasize agent-user collaboration (not just code generation) as a key frontier in future agent design.</p>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">SpecBench Pipeline</h2>
    <div class="method-visual">
      <img src="/images/specbench/specbench_overview.jpg" alt="SpecBench Pipeline Overview">
    </div>
    <p>SpecBench consists of 50 software design tasks across diverse domains with 48 simulated user personas. It evaluates agents on two complementary tasks: (1) preference elicitation, where agents predict user design choices after asking clarification queries, and (2) collaborative spec drafting, where agents work with users to produce structured specification documents rated on coverage, precision, consistency, insight, and readability.</p>
  </div>
  
  <div class="section-box">
    <h2 class="section-title">Buddy Agent</h2>
    <div class="method-visual">
      <img src="/images/specbench/buddy_method.jpg" alt="Buddy Agent Architecture">
    </div>
    <p>Buddy decomposes a spec sheet into independent design dimensions using morphological analysis, then explores alternatives along each axis. It constructs a user profile and conversation summary from prior interactions, deploys simulated users to resolve predictable decisions, and strategically queries the real user only on uncertain choices. The result is higher quality specs with fewer user queries than existing agents.</p>
  </div>

  <div class="section-box">
    <h2 class="section-title">Results</h2>
    <div class="results-grid">
      <div class="result-item">
        <img src="/images/specbench/results_elicitation.png" alt="Preference Elicitation Results">
      </div>
      <div class="result-item">
        <img src="/images/specbench/results_spec_quality.png" alt="Spec Sheet Quality Comparison">
      </div>
    </div>
    <p>Buddy achieves higher quality specifications while querying users significantly fewer times than Claude Code, Gemini CLI, and Cursor CLI. Existing agents either ask too few questions (Gemini CLI) or too many without effective prioritization (Claude Code, Cursor CLI).</p>
  </div>
  
  <div class="section-box" id="citation">
    <h2 class="section-title">Citation</h2>
    <pre><code>@article{wang2026specbench,
    title={Turning Intent into Specifications: A Benchmark and an Interactive User-Assistant Agent},
    author={Wang, Hao and Han, Ligong and Xu, Kai and Srivastava, Akash},
    year={2026}
}</code></pre>
  </div>
</div>
