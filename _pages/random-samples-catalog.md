---
layout: page
title: Random Samples Catalog
permalink: /random-samples-catalog/
description: Complete catalog of all Random Samples seminar episodes from the AI Innovation Team.
---

<div class="catalog-header">
  <p>Complete catalog of all <strong>Random Samples</strong> episodes, our weekly AI research seminar series.</p>
  <p class="catalog-meta">{{ site.data.videos | where: "category", "Random Samples" | size }} episodes &middot; <a href="/videos/#random-samples">&larr; Back to Videos</a></p>
</div>

<table class="catalog-table">
  <thead>
    <tr>
      <th class="col-date">Date</th>
      <th class="col-title">Talk</th>
      <th class="col-speaker">Speaker</th>
    </tr>
  </thead>
  <tbody>
    {% assign random_samples = site.data.videos | where: "category", "Random Samples" | sort: "date" | reverse %}
    {% for video in random_samples %}
    <tr>
      <td class="col-date">{{ video.date | date: "%b %d, %Y" }}</td>
      <td class="col-title">
        <a href="{{ video.youtube_url }}" target="_blank">{{ video.title }}</a>
        {% if video.abstract %}
        <details class="catalog-abstract">
          <summary>Abstract</summary>
          <p>{{ video.abstract }}</p>
        </details>
        {% endif %}
      </td>
      <td class="col-speaker">{{ video.speaker }}</td>
    </tr>
    {% endfor %}
  </tbody>
</table>

<style>
.catalog-header {
  margin-bottom: 2rem;
}

.catalog-meta {
  font-size: 0.9em;
  color: var(--text-alt-color, #666);
}

.catalog-meta a {
  color: var(--link-color, #0066cc);
  text-decoration: none;
}

.catalog-meta a:hover {
  text-decoration: underline;
}

.catalog-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95em;
  line-height: 1.5;
}

.catalog-table thead {
  border-bottom: 2px solid var(--heading-font-color, #1d1d1f);
}

.catalog-table th {
  text-align: left;
  padding: 0.6rem 0.75rem;
  font-weight: 600;
  font-size: 0.8em;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-alt-color, #666);
}

.catalog-table td {
  padding: 0.75rem;
  border-bottom: 1px solid var(--border-color, #eee);
  vertical-align: top;
}

.catalog-table tbody tr:hover {
  background: var(--background-alt-color, rgba(0, 0, 0, 0.02));
}

.col-date {
  white-space: nowrap;
  width: 120px;
  color: var(--text-alt-color, #666);
  font-size: 0.9em;
  font-variant-numeric: tabular-nums;
}

.col-title a {
  text-decoration: none;
  font-weight: 500;
  color: var(--heading-font-color, #1d1d1f);
}

.col-title a:hover {
  color: var(--link-color, #0066cc);
}

.col-speaker {
  white-space: nowrap;
  color: var(--text-alt-color, #666);
  font-size: 0.9em;
  width: 200px;
}

.catalog-abstract {
  margin-top: 0.4rem;
}

.catalog-abstract summary {
  cursor: pointer;
  color: var(--link-color, #0066cc);
  font-size: 0.82em;
  user-select: none;
  list-style: none;
}

.catalog-abstract summary::-webkit-details-marker {
  display: none;
}

.catalog-abstract summary::before {
  content: "\25B8 ";
  font-size: 0.8em;
}

.catalog-abstract[open] summary::before {
  content: "\25BE ";
}

.catalog-abstract summary:hover {
  text-decoration: underline;
}

.catalog-abstract p {
  margin: 0.4rem 0 0;
  font-size: 0.85em;
  line-height: 1.6;
  color: var(--text-alt-color, #666);
  max-width: 600px;
}

@media (max-width: 768px) {
  .catalog-table thead {
    display: none;
  }

  .catalog-table,
  .catalog-table tbody,
  .catalog-table tr,
  .catalog-table td {
    display: block;
  }

  .catalog-table tr {
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--border-color, #eee);
  }

  .catalog-table td {
    padding: 0.15rem 0;
    border-bottom: none;
  }

  .col-date {
    font-size: 0.8em;
    text-transform: uppercase;
    letter-spacing: 0.03em;
  }

  .col-title a {
    font-size: 1.05em;
  }

  .col-speaker {
    white-space: normal;
  }
}
</style>
