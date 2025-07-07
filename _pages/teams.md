---
layout: page
title:  "LUMI Lab"
nav_title: "LUMI Lab"
nav_order: 3
nav: true
permalink: /teams/

#=========== 数据区域 ===========#
members:
  - name: Adarsh Kappiyath
    group: PhD Students 
    avatar: /assets/img/team/Adarsh Kappiyath.jpg
    intro:  "PhD 2024 -"
    link:   "https://kadarsh22.github.io/"


  - name: Mingyu Cao
    group: PhD Students 
    avatar: /assets/img/team/Mingyu Cao.jpeg
    intro:  "PhD 2025 -"
    link:   "https://scholar.google.com/citations?user=nq7uHwQAAAAJ&hl"

  - name: Handa Li
    group: PhD Students 
    avatar: /assets/img/team/Handa Li.jpg
    intro:  "PhD 2025 -"
    link:   ""


  - name: Xiaolong Han
    group: PhD Students
    avatar: /assets/img/team/Xiaolong Han.jpeg
    intro: PhD 2025 –<br/>
      Co-supervised with <a href="https://www.surrey.ac.uk/people/ferrante-neri" target="_blank">Ferrante Neri</a>  
    link:   "https://scholar.google.com/citations?user=5oaBR_0AAAAJ&hl"



  - name: Vishal Thengane
    group: PhD Students 
    avatar: /assets/img/team/Vishal Thengane.jpg
    intro: PhD 2024 –<br/>
      Co-supervised with <a href="https://x-up-lab.github.io/" target="_blank">Xiatianzhu</a>  
    link: "https://vgthengane.github.io/"


  - name: Jiaxi Li
    group: PhD Students 
    avatar: /assets/img/team/Jiaxi Li.jpeg
    intro: |
      PhD 2024 –<br/>
      Co-supervised with <a href="https://scholar.google.com/citations?user=Xmlr1xQAAAAJ&hl=en" target="_blank">Xilu Wang</a>  
    link: "https://scholar.google.com/citations?user=RqzHZVIAAAAJ&hl"


  - name: Shaojie Zhuang
    group: Visiting Scholar  
    avatar: /assets/img/team/Handa Li.png
    intro:  "Visiting PhD from Shandong University"
    link:   ""




---

{% comment %}
  分组渲染：先把成员按 group 排序，再 group_by。
{% endcomment %}

{% assign sorted = page.members | sort: "group" %}
{% assign groups  = sorted | group_by: "group" %}

{% for g in groups %}
<!-- ### {{ g.name }} -->
<div class="row justify-content-center mt-3 mb-5">
  {% for p in g.items %}
  <div class="col-lg-4 col-md-6 col-sm-10 mb-5 text-center">
    <img src="{{ p.avatar | relative_url }}" alt="{{ p.name }}" class="team-avatar mb-3">
    <h5 class="font-weight-bold mb-1">{{ p.name }}</h5>
    <p class="small text-muted">{{ p.intro }}</p>
    <a href="{{ p.link }}" target="_blank" class="btn btn-sm team-btn">Homepage</a>
  </div>
  {% endfor %}
</div>
{% endfor %}
