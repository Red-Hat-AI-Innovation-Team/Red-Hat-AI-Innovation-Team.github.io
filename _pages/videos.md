---
layout: page
title: Videos
permalink: /videos/
description: Watch our AI research talks, tutorials, and discussions on LLMs, machine learning, and generative AI. Featuring Random Samples seminars and No Math AI podcast.
---

<div class="section-nav">
  <div class="nav-grid">
    <a href="#random-samples" class="nav-card">
      <div class="nav-image">
        <img src="/images/videos/Random Samples.png" alt="Random Samples - Weekly live seminar series">
      </div>
    </a>
    
    <a href="#no-math-ai" class="nav-card">
      <div class="nav-image">
        <img src="/images/videos/No Math AI.png" alt="No Math AI - Monthly AI podcast">
      </div>
    </a>
    
    <a href="#other-select-talks" class="nav-card">
      <div class="nav-image">
        <img src="/images/videos/Other Select Talks.png" alt="Other Select Talks - Featured presentations">
      </div>
    </a>
  </div>
</div>

---

## 🎥 Random Samples {#random-samples}

Random Samples is a weekly seminar series that airs live on our Red Hat YouTube page.

<div class="video-grid">
  {% assign random_samples = site.data.videos | where: "category", "Random Samples" | sort: "date" | reverse %}
  {% for video in random_samples %}
  <div class="video-card">
    {% include video-card.html width="300" height="170" %}
  </div>
  {% endfor %}
</div>

---

## 🎙️ No Math AI {#no-math-ai}

No Math AI is a monthly podcast designed for the AI community and enthusiasts who want to better understand how AI research translates into real-world business impact—without the complex equations.

Hosted by Dr. Akash Srivastava (Red Hat) and Isha Puri (MIT), this series distills critical AI concepts into practical takeaways to help practitioners, businesses, and curious minds accelerate adoption with confidence.

<div class="video-grid">
  {% assign no_math_ai = site.data.videos | where: "category", "No Math AI" | sort: "date" | reverse %}
  {% for video in no_math_ai %}
  <div class="video-card">
    {% include video-card.html width="300" height="170" %}
  </div>
  {% endfor %}
</div>

---

## 🎬 Other Select Talks {#other-select-talks}

<div class="video-grid">
  {% assign other_talks = site.data.videos | where: "category", "Other Select Talks" | sort: "date" | reverse %}
  {% for video in other_talks %}
  <div class="video-card">
    {% include video-card.html width="300" height="170" %}
  </div>
  {% endfor %}
</div>

