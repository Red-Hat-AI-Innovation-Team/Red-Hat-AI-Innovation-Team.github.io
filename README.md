# AI Innovation Team Website

Official website for the AI Innovation Team at Red Hat and IBM, showcasing our open-source AI research, tools, and publications.

🌐 **Live Site**: [https://ai-innovation.team](https://ai-innovation.team)

## About

We are an AI research team at Red Hat and IBM with collaborators from MIT, UMass, and other leading institutions, dedicated to fostering an inclusive and accessible open-source AI community. Our mission is to empower individuals to collaborate in advancing the future of LLMs and generative models.

## Featured Projects

### LLM Hubs
- **[its_hub](https://github.com/Red-Hat-AI-Innovation-Team/its_hub)** - Inference-time scaling for LLMs
- **[sdg_hub](https://github.com/Red-Hat-AI-Innovation-Team/sdg_hub)** - Synthetic data generation pipelines
- **[training_hub](https://github.com/Red-Hat-AI-Innovation-Team/training_hub)** - Post-training algorithms for LLMs

### LLM Tools
- **[async-grpo](https://github.com/Red-Hat-AI-Innovation-Team/async-grpo)** - Asynchronous GRPO for scalable reinforcement learning
- **[hopscotch](https://github.com/Red-Hat-AI-Innovation-Team/hopscotch)** - A method for skipping redundant attention blocks in language models
- **[mini_trainer](https://github.com/Red-Hat-AI-Innovation-Team/mini_trainer)** - Efficient training library for LLMs up to 70B parameters on a single node
- **[orthogonal-subspace-learning](https://github.com/Red-Hat-AI-Innovation-Team/orthogonal-subspace-learning)** - Adaptive SVD-based continual learning
- **[probabilistic-inference-scaling](https://github.com/probabilistic-inference-scaling/probabilistic-inference-scaling)** - Inference-time scaling with particle filtering
- **[reward_hub](https://github.com/Red-Hat-AI-Innovation-Team/reward_hub)** - State-of-the-art reward models
- **[SQuat](https://github.com/Red-Hat-AI-Innovation-Team/SQuat)** - KV cache quantization for scaling inference time
- **[training](https://github.com/instructlab/training)** - Efficient messages-format SFT library

## Development

This website is built with [Jekyll](https://jekyllrb.com/) and hosted on GitHub Pages.

### Prerequisites

- Ruby (version 2.7 or higher)
- Bundler
- Jekyll

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/Red-Hat-AI-Innovation-Team/Red-Hat-AI-Innovation-Team.github.io.git
cd Red-Hat-AI-Innovation-Team.github.io
```

2. Install dependencies:
```bash
bundle install
```

3. Run the development server:
```bash
bundle exec jekyll serve
```

4. Open your browser to `http://localhost:4000`

### Project Structure

```
.
├── _config.yml           # Site configuration
├── _data/
│   ├── settings.yml      # Site settings, menus, projects
│   └── videos.yml        # Video content catalog
├── _includes/            # Reusable HTML components
├── _layouts/             # Page layouts
├── _pages/               # Static pages (About, Publications, etc.)
├── _posts/               # Blog posts
├── _sass/                # Stylesheets
├── images/               # Image assets
├── js/                   # JavaScript files
└── index.html            # Homepage
```

## Contributing

### Adding a Blog Post

Create a new file in `_posts/` with the format `YYYY-MM-DD-title.md`:

```markdown
---
layout: post
title: Your Post Title
date: YYYY-MM-DD
image: '/images/posts/your-image.jpg'
tags: [tag1, tag2]
---

Your content here...
```

### Adding a Publication

Edit `_pages/publications.md` and add a new publication card:

```html
<div class="publication-card">
<h3><a href="ARXIV_URL" target="_blank">Paper Title</a></h3>
<strong>Authors:</strong> Author 1, Author 2<br>
<details>
  <summary>View Abstract</summary>
  Abstract text here...
</details>
<strong><a href="ARXIV_URL">📄 Arxiv</a> | <a href="GITHUB_URL">💻 Code</a></strong><br>
<strong>Date:</strong> YYYY-MM-DD
</div>
```

### Adding a Video

Edit `_data/videos.yml`:

```yaml
- title: "Talk Title"
  speaker: "Speaker Name"
  youtube_id: "VIDEO_ID"
  youtube_url: "https://www.youtube.com/watch?v=VIDEO_ID"
  embed_url: "https://www.youtube.com/embed/VIDEO_ID"
  date: "YYYY-MM-DD"
  category: "Random Samples"
```

### Adding a Team Member

Edit `_pages/about.md` and add to the appropriate section (Team Members or Collaborators):

```html
<div class="col col-3 col-d-6 col-t-12">
  <div>
    <a href="/images/about/Headshots/name.jpg" class="portfolio__link glightbox"
       data-glightbox='title: Full Name; description: ; descPosition: bottom;'>
      <span class="portfolio__icon"><i class="ion ion-ios-eye"></i></span>
      <img src="/images/about/Headshots/name.jpg" data-src="/images/about/Headshots/name.jpg"
           class="portfolio__image lazy" alt="Picture of Full Name">
    </a>
    <a href="PERSONAL_URL" target="_blank">Full Name</a>
  </div>
</div>
```

## Site Features

- ✅ Responsive design with dark/light mode
- ✅ Blog with pagination
- ✅ Publication showcase with expandable abstracts
- ✅ Video catalog with categories
- ✅ Project portfolio
- ✅ Team member profiles
- ✅ Google Analytics integration
- ✅ SEO optimized
- ✅ Fast performance with lazy loading
- ✅ Math support via KaTeX

## Theme

This site uses a customized version of the [Clancy](https://jekyllthemes.io/theme/clancy-portfolio-jekyll-theme) Jekyll theme, optimized for research team presentation.

## License

Content on this site is the property of the AI Innovation Team and respective authors. Check individual repositories for software licenses.

## Contact

For questions or collaboration opportunities, please reach out through our [GitHub organization](https://github.com/Red-Hat-AI-Innovation-Team).

---

**Maintained by the AI Innovation Team** | Red Hat & IBM | [ai-innovation.team](https://ai-innovation.team)
