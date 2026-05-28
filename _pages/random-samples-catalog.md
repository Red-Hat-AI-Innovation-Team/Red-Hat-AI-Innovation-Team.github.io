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

<div class="catalog-wrap">
  <table class="catalog-table">
    <thead>
      <tr>
        <th>Date</th>
        <th>Talk</th>
        <th>Speaker</th>
      </tr>
    </thead>
    <tbody>
      {% assign random_samples = site.data.videos | where: "category", "Random Samples" | sort: "date" | reverse %}
      {% for video in random_samples %}
      <tr>
        <td class="ct-date">{{ video.date | date: "%b %d, %Y" }}</td>
        <td class="ct-title">
          <a href="{{ video.youtube_url }}" target="_blank">{{ video.title }}</a>
          {% if video.abstract %}
          <details class="ct-abstract">
            <summary>Abstract</summary>
            <p>{{ video.abstract }}</p>
          </details>
          {% endif %}
        </td>
        <td class="ct-speaker">{{ video.speaker }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>

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

.catalog-wrap {
  overflow-x: auto;
}

.catalog-table {
  width: 100% !important;
  border-collapse: collapse !important;
  font-size: 0.95em;
  line-height: 1.5;
  table-layout: fixed;
}

.catalog-table thead tr {
  border-bottom: 2px solid var(--heading-font-color, #1d1d1f) !important;
}

.catalog-table th {
  text-align: left !important;
  padding: 0.6rem 0.75rem !important;
  font-weight: 600 !important;
  font-size: 0.75em;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--text-alt-color, #666);
  background: none !important;
  border: none !important;
}

.catalog-table td {
  padding: 0.75rem !important;
  border: none !important;
  border-bottom: 1px solid var(--border-color, #eee) !important;
  vertical-align: top;
}

.catalog-table tbody tr:hover {
  background: var(--background-alt-color, rgba(0, 0, 0, 0.02));
}

.catalog-table th:first-child,
.catalog-table .ct-date {
  width: 110px;
}

.catalog-table th:last-child,
.catalog-table .ct-speaker {
  width: 220px;
}

.ct-date {
  white-space: nowrap;
  color: var(--text-alt-color, #666);
  font-size: 0.88em;
  font-variant-numeric: tabular-nums;
}

.ct-title a {
  text-decoration: none;
  font-weight: 500;
  color: var(--heading-font-color, #1d1d1f);
  transition: color 0.15s;
}

.ct-title a:hover {
  color: var(--link-color, #0066cc);
}

.ct-speaker {
  color: var(--text-alt-color, #666);
  font-size: 0.88em;
}

.ct-abstract {
  margin-top: 0.4rem;
}

.ct-abstract summary {
  cursor: pointer;
  color: var(--link-color, #0066cc);
  font-size: 0.82em;
  user-select: none;
  list-style: none;
  display: inline-block;
}

.ct-abstract summary::-webkit-details-marker {
  display: none;
}

.ct-abstract summary::before {
  content: "\25B8\00a0";
  font-size: 0.75em;
}

.ct-abstract[open] summary::before {
  content: "\25BE\00a0";
}

.ct-abstract summary:hover {
  text-decoration: underline;
}

.ct-abstract p {
  margin: 0.5rem 0 0.25rem;
  font-size: 0.85em;
  line-height: 1.65;
  color: var(--text-alt-color, #666);
}

@media (max-width: 768px) {
  .catalog-table {
    table-layout: auto;
  }

  .catalog-table thead {
    display: none;
  }

  .catalog-table,
  .catalog-table tbody,
  .catalog-table tr,
  .catalog-table td {
    display: block !important;
    width: 100% !important;
  }

  .catalog-table tr {
    padding: 0.75rem 0;
    border-bottom: 1px solid var(--border-color, #eee) !important;
  }

  .catalog-table td {
    padding: 0.15rem 0 !important;
    border-bottom: none !important;
  }

  .ct-date {
    font-size: 0.78em;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    margin-bottom: 0.15rem;
  }

  .ct-title a {
    font-size: 1.02em;
  }

  .ct-speaker {
    white-space: normal;
    margin-top: 0.15rem;
  }
}
</style>
