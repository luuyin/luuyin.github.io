---
layout: page_notitile
permalink: /beyond/
title: Beyond the Lab
nav: true
nav_order: 7

# ===== Photos =====
# Drop image files into  assets/img/beyond/  then add an entry below, e.g.:
#
#   - image: /assets/img/beyond/eindhoven-spring.jpg
#     location: "Eindhoven, Netherlands"
#     date: "March 2024"
#     caption: "Quiet streets"        # optional, a short poetic line
#
# Newest first reads best. Portrait and landscape photos both work.
photos:
  - image: /assets/photos/2026-guildford.jpg
    location: "Guildford, UK"
    date: "2026"
  - image: /assets/photos/2025-tuebingen.jpg
    location: "Tübingen, Germany"
    date: "2025"
  - image: /assets/photos/2025-paris-1.jpg
    location: "Paris, France"
    date: "2025"
  - image: /assets/photos/2025-paris-2.jpg
    location: "Paris, France"
    date: "2025"
  - image: /assets/photos/2025-denmark.jpg
    location: "Denmark"
    date: "2025"
  - image: /assets/photos/2024-london.jpg
    location: "London, UK"
    date: "2024"
    caption: "Still can’t believe I got to see Taylor Swift this close…"
  - image: /assets/photos/2024-istanbul-1.jpg
    location: "Istanbul, Türkiye"
    date: "2024"
  - image: /assets/photos/2024-istanbul-2.jpg
    location: "Istanbul, Türkiye"
    date: "2024"
  - image: /assets/photos/2023-aberdeen-1.jpg
    location: "Aberdeen, UK"
    date: "2023"
  - image: /assets/photos/2023-aberdeen-2.jpg
    location: "Aberdeen, UK"
    date: "2023"
  - image: /assets/photos/2023-hongkong.jpg
    location: "Hong Kong"
    date: "2023"
  - image: /assets/photos/2023-newyork.jpg
    location: "New York, USA"
    date: "2023"
  - image: /assets/photos/2019-sahara.jpg
    location: "Sahara Desert"
    date: "2019"
  - image: /assets/photos/2019-finland.jpg
    location: "Finland"
    date: "2019"
---

<p class="beyond-intro">Beyond the lab, I like to wander with a camera — chasing light, quiet streets, and the small moments that usually go unnoticed.</p>

{% if page.photos %}
<div class="beyond-gallery">
{% for photo in page.photos %}
  <figure class="beyond-item">
    <img src="{{ photo.image | relative_url }}" alt="{{ photo.caption | default: photo.location }}" loading="lazy">
    <figcaption>
      {% if photo.caption %}<span class="cap-title">{{ photo.caption }}</span>{% endif %}
      <span class="cap-meta">{{ photo.location }}{% if photo.location and photo.date %} · {% endif %}{{ photo.date }}</span>
    </figcaption>
  </figure>
{% endfor %}
</div>
{% else %}
<p class="beyond-empty">A few frames are on their way.</p>
{% endif %}
