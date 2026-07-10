# Factory Configuration

## Project

- **name**: Red Hat AI Innovation Team Website
- **language**: ruby
- **project_type**: website
- **description**: Official website for the Red Hat AI Innovation Team, built with Jekyll and deployed via GitHub Pages.

### Goal
Improve site quality: ensure clean builds, valid HTML, fresh content, and a well-structured Jekyll architecture.

### Build

```bash
bundle exec jekyll b -d _site
```

### Test

```bash
bundle exec htmlproofer _site --disable-external --ignore-urls '/^http:\/\/127.0.0.1/,/^http:\/\/0.0.0.0/,/^http:\/\/localhost/' --ignore-empty-alt --ignore-missing-alt
```

### CI

- GitHub Actions: `.github/workflows/pages-deploy.yml`

## Target Branch

main

## Modifiable Files

These are the files and directories the factory is allowed to modify:

### Site Configuration
- `_config.yml`
- `index.html`
- `404.html`
- `feed.xml`
- `robots.txt`

### Layouts
- `_layouts/*.html`

### Includes (partials and components)
- `_includes/*.html`
- `_includes/*.scss`

### Content Pages
- `_pages/*.html`
- `_pages/*.md`

### Blog Posts
- `_posts/*.md`
- `_posts/*.html`
- `blog/index.html`

### Data Files
- `_data/*.yml`

### Styles
- `_sass/**/*.scss`

### JavaScript
- `js/*.js`

### Static Assets
- `images/**/*`
- `papers/**/*`

## Fixed Files

These files must NOT be modified by the factory:

- `eval/score.py`
- `.factory/**/*`
- `.github/workflows/pages-deploy.yml`
- `Gemfile`
- `Gemfile.lock`
- `CNAME`
- `README.md`

## Project Eval

```bash
python eval/score.py
```

Threshold: 0.40

## Eval Weights

| Component | Weight |
|-----------|--------|
| hygiene   | 0.20   |
| growth    | 0.10   |
| project   | 0.70   |
