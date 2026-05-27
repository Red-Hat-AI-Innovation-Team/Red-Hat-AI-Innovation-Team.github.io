---
layout: page
title: Random Samples Catalog
permalink: /random-samples-catalog/
description: Complete catalog of all Random Samples seminar episodes from the AI Innovation Team.
---

<div class="catalog-header">
  <p>Complete catalog of all <strong>Random Samples</strong> episodes, our weekly AI research seminar series.</p>
  <p><a href="/videos/#random-samples">&larr; Back to Videos</a></p>
</div>

<div class="catalog-list">
  {% assign random_samples = site.data.videos | where: "category", "Random Samples" | sort: "date" | reverse %}
  {% for video in random_samples %}
  <div class="catalog-entry">
    <div class="catalog-row">
      <span class="catalog-date">{{ video.date | date: "%b %d, %Y" }}</span>
      <span class="catalog-title"><a href="{{ video.youtube_url }}" target="_blank">{{ video.title }}</a></span>
      <span class="catalog-speaker">{{ video.speaker }}</span>
    </div>
    {% if video.abstract %}
    <details class="catalog-abstract">
      <summary>Abstract</summary>
      <p>{{ video.abstract }}</p>
    </details>
    {% endif %}
  </div>
  {% endfor %}
</div>

<style>
.catalog-header {
  margin-bottom: 2rem;
}

.catalog-entry {
  border-bottom: 1px solid var(--border-color, #eee);
  padding: 0.75rem 0;
}

.catalog-entry:first-child {
  border-top: 2px solid var(--border-color, #ddd);
}

.catalog-row {
  display: flex;
  align-items: baseline;
  gap: 1rem;
}

.catalog-date {
  white-space: nowrap;
  color: var(--text-alt-color, #666);
  min-width: 100px;
  font-size: 0.9em;
}

.catalog-title {
  flex: 1;
}

.catalog-title a {
  text-decoration: none;
}

.catalog-title a:hover {
  text-decoration: underline;
}

.catalog-speaker {
  white-space: nowrap;
  color: var(--text-alt-color, #666);
  font-size: 0.9em;
}

.catalog-abstract {
  margin: 0.5rem 0 0 calc(100px + 1rem);
}

.catalog-abstract summary {
  cursor: pointer;
  color: var(--link-color, #0066cc);
  font-size: 0.85em;
  user-select: none;
}

.catalog-abstract summary:hover {
  text-decoration: underline;
}

.catalog-abstract p {
  margin: 0.5rem 0 0;
  font-size: 0.9em;
  line-height: 1.5;
  color: var(--text-alt-color, #666);
}

@media (max-width: 768px) {
  .catalog-row {
    flex-direction: column;
    gap: 0.25rem;
  }

  .catalog-abstract {
    margin-left: 0;
  }
}
</style>
