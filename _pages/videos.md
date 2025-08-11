---
layout: page
title: Videos
permalink: /videos/
---

## 🎥 Random Samples

Random Samples is a weekly seminar series that airs live on our Red Hat YouTube page.

<div class="video-grid">
  {% assign random_samples = site.data.videos | where: "category", "Random Samples" | sort: "date" | reverse %}
  {% for video in random_samples %}
  <div class="video-card">
    <iframe width="300" height="170" src="{{ video.embed_url }}" frameborder="0" allowfullscreen></iframe>
    <p><strong><a href="{{ video.youtube_url }}" target="_blank">📹 {{ video.title }}</a></strong><br>👤 Speaker: {{ video.speaker }}</p>
  </div>
  {% endfor %}
</div>

---

## 🎙️ No Math AI

No Math AI is a monthly podcast designed for the AI community and enthusiasts who want to better understand how AI research translates into real-world business impact—without the complex equations.

Hosted by Dr. Akash Srivastava (Red Hat) and Isha Puri (MIT), this series distills critical AI concepts into practical takeaways to help practitioners, businesses, and curious minds accelerate adoption with confidence.

<div class="video-grid">
  {% assign no_math_ai = site.data.videos | where: "category", "No Math AI" | sort: "date" | reverse %}
  {% for video in no_math_ai %}
  <div class="video-card">
    <iframe width="300" height="170" src="{{ video.embed_url }}" frameborder="0" allowfullscreen></iframe>
    <p><strong><a href="{{ video.youtube_url }}" target="_blank">📹 {{ video.title }}</a></strong><br>👤 Speaker: {{ video.speaker }}
    {% if video.spotify_url %}<br>🎧 <a href="{{ video.spotify_url }}" class="spotify-link" target="_blank">Listen on Spotify</a>{% endif %}</p>
  </div>
  {% endfor %}
</div>
