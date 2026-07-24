---
layout: page
title: About
permalink: /about/
image: '/images/about/group.jpg'
description: Meet the AI Innovation Team - researchers and engineers from Red Hat, IBM, MIT, and UMass building open-source LLM tools and advancing generative AI.
---

## AI Innovation Team

We are an AI research team at Red Hat and IBM with collaborators from MIT, UMass, and IBM, dedicated to fostering an inclusive and accessible open-source AI community. 
Our goal is to empower individuals to collaborate in advancing the future of LLMs and generative models.

### Team Members

<div class="container">
  <div class="row">
    {% for member in site.data.team.members %}
    {% include team-member-card.html member=member %}
    {% endfor %}
  </div>
</div>

<div style="text-align: center; margin: 2rem 0;">
  <img src="/images/about/team.jpg" alt="AI Innovation Team Photo" style="max-width: 100%; height: auto; border-radius: 8px;">
</div>

### Collaborators

<div class="container">
  <div class="row">
    {% for member in site.data.team.collaborators %}
    {% include team-member-card.html member=member %}
    {% endfor %}
  </div>
</div>
