---
layout: page
title: "LUMI Lab"     # 页面顶部大标题
nav_title: "Teams"    # 导航栏显示
nav_order: 3
nav: true
permalink: /teams/

#=========== 分组显示顺序 & 标题 ===========#
group_sections:
  - key: "PI"
    title: "Principal Investigator"

  - key: "PhD Students"
    title: "Current PhD Students"

  - key: "Research Intern"
    title: "Research Interns"

  - key: "Visiting Scholar"
    title: "Visiting Scholars"

#=========== 数据区域 ===========#
members:
  # ===== PI =====
  - name: Lu Yin
    group: "PI"
    avatar: /assets/img/team/Lu Yin.jpg
    intro: "Assistant Professor"

  # ===== Current PhD Students =====
  - name: Adarsh Kappiyath
    group: "PhD Students"
    avatar: /assets/img/team/Adarsh Kappiyath.jpg
    intro: "PhD 2024 -"
    link: "https://kadarsh22.github.io/"

  - name: Mingyu Cao
    group: "PhD Students"
    avatar: /assets/img/team/Mingyu Cao.jpeg
    intro: "PhD 2025 -"
    link: "https://scholar.google.com/citations?user=nq7uHwQAAAAJ&hl"

  - name: Handa Li
    group: "PhD Students"
    avatar: /assets/img/team/Handa Li.jpg
    intro: "PhD 2025 -"
    link: ""

  - name: Xiaolong Han
    group: "PhD Students"
    avatar: /assets/img/team/Xiaolong Han.jpeg
    intro: |
      PhD 2025 –<br/>
      Co-supervised with <a href="https://www.surrey.ac.uk/people/ferrante-neri" target="_blank" rel="noopener noreferrer">Ferrante Neri</a>
    link: "https://scholar.google.com/citations?user=5oaBR_0AAAAJ&hl"

  - name: Vishal Thengane
    group: "PhD Students"
    avatar: /assets/img/team/Vishal Thengane.jpg
    intro: |
      PhD 2024 –<br/>
      Co-supervised with <a href="https://x-up-lab.github.io/" target="_blank" rel="noopener noreferrer">Xiatianzhu</a>
    link: "https://vgthengane.github.io/"

  - name: Jiaxi Li
    group: "PhD Students"
    avatar: /assets/img/team/Jiaxi Li.jpeg
    intro: |
      PhD 2024 –<br/>
      Co-supervised with <a href="https://scholar.google.com/citations?user=Xmlr1xQAAAAJ&hl=en" target="_blank" rel="noopener noreferrer">Xilu Wang</a>
    link: "https://scholar.google.com/citations?user=RqzHZVIAAAAJ&hl"

  # ===== Visiting Scholars =====
  - name: Shaojie Zhuang
    group: "Visiting Scholar"
    avatar: /assets/img/team/Anonymous.png
    intro: "PhD candidate at Shandong University"
    link: ""

  # ===== Research Interns =====
  - name: Pengxiang Li
    group: "Research Intern"
    avatar: /assets/img/team/Pengxiang Li.jpeg
    intro: "PhD candidate at Hong Kong Polytechnic University"
    link: "https://scholar.google.com/citations?user=rUp_4RgAAAAJ&hl=en"

  - name: Xin Xu
    group: "Research Intern"
    avatar: /assets/img/team/Anonymous.png
    intro: "PhD candidate at The Hong Kong University of Science and Technology"
    link: "https://xinxu-ustc.github.io/"
    
  - name: Tianhao Chen
    group: "Research Intern"
    avatar: /assets/img/team/Anonymous.png
    intro: "PhD candidate at The Hong Kong University of Science and Technology"
    link: "https://openreview.net/profile?id=~Tianhao_Chen3"
---

<style>
/* ===== 高级简约：轻量审美升级，不改变布局结构 ===== */
.team-page{
  --accent: var(--global-theme-color, #159957);
  --title: rgba(17,17,17,.88);
  --text: rgba(17,17,17,.62);
  --line: rgba(0,0,0,.10);
}

/* 分组标题：书卷气 + 细线分隔（保留原来清爽感） */
.team-page .team-section-title{
  font-family: "Roboto Slab", "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-weight: 400;
  font-size: 1.30rem;
  letter-spacing: .2px;
  color: var(--title);
  margin: 2.0rem 0 1.05rem;
}
.team-page .team-section-title::after{
  content:"";
  display:block;
  margin-top: .55rem;
  height: 1px;
  width: 100%;
  background: var(--line);
}

/* 名字：去掉粗黑（更优雅） */
.team-page .team-name{
  font-family: "Roboto Slab", "Roboto", -apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif;
  font-weight: 500;
  color: rgba(17,17,17,.84);
  font-size: 1.12rem;
  letter-spacing: .12px;
}

/* intro：更轻更干净 */
.team-page .team-intro{
  color: var(--text);
  font-size: .93rem;
  line-height: 1.45;
  margin-bottom: .65rem;
}

/* 头像：轻边框 + 轻阴影 */
.team-page .team-avatar{
  border: 2px solid rgba(0,0,0,.08);
  box-shadow: 0 6px 18px rgba(0,0,0,.06);
  transition: transform .15s ease, box-shadow .15s ease;
}
.team-page .team-avatar:hover{
  transform: translateY(-2px);
  box-shadow: 0 10px 28px rgba(0,0,0,.08);
}

/* ================================
   关键：高级按钮（不再用 Bootstrap 的 btn）
   ================================ */
.team-page a.team-btn{
  display: inline-flex;
  align-items: center;
  justify-content: center;

  padding: .52rem 1.10rem;
  min-width: 136px;

  border-radius: 12px;

  background: #fff;
  border: 1px solid rgba(0,0,0,.06);
  box-shadow: 0 10px 22px rgba(0,0,0,.06);

  color: rgba(17,17,17,.70);
  font-size: .74rem;
  font-weight: 600;
  letter-spacing: .10em;
  text-transform: uppercase;
  text-decoration: none;

  transition: transform .12s ease, box-shadow .12s ease, border-color .12s ease, color .12s ease, background-color .12s ease;
  -webkit-tap-highlight-color: transparent;
}

.team-page a.team-btn:hover{
  transform: translateY(-1px);
  border-color: rgba(21,153,87,.22);
  color: var(--accent);
  background: rgba(21,153,87,.06);
  box-shadow: 0 14px 28px rgba(0,0,0,.08);
}

.team-page a.team-btn:active{
  transform: translateY(0);
  box-shadow: 0 10px 22px rgba(0,0,0,.06);
}

.team-page a.team-btn:focus-visible{
  outline: none;
  box-shadow: 0 0 0 .18rem rgba(21,153,87,.18), 0 10px 22px rgba(0,0,0,.06);
}

/* 深色系统：只调颜色，风格不变 */
@media (prefers-color-scheme: dark){
  .team-page{
    --title: rgba(230,237,243,.92);
    --text: rgba(230,237,243,.65);
    --line: rgba(255,255,255,.12);
  }
  .team-page .team-name{ color: rgba(230,237,243,.88); }
  .team-page .team-avatar{
    border-color: rgba(255,255,255,.10);
    box-shadow: 0 8px 24px rgba(0,0,0,.35);
  }
  .team-page a.team-btn{
    background: rgba(15,17,20,.92);
    border-color: rgba(255,255,255,.10);
    color: rgba(230,237,243,.72);
    box-shadow: 0 12px 26px rgba(0,0,0,.40);
  }
  .team-page a.team-btn:hover{
    background: rgba(21,153,87,.12);
    border-color: rgba(155,231,196,.22);
    color: rgba(155,231,196,.95);
  }
}
</style>

<div class="team-page">

{% comment %}
  按 group_sections 的顺序输出（不会按字母排序）
  保留原始布局：row + col + 圆头像 + 名字 + intro + 按钮
{% endcomment %}

{% for sec in page.group_sections %}
{% assign items = page.members | where: "group", sec.key %}

{% if items.size > 0 %}
<h2 class="team-section-title">{{ sec.title }}</h2>

{% if items.size == 1 %}
<div class="row justify-content-start mt-3 mb-5">
{% else %}
<div class="row justify-content-center mt-3 mb-5">
{% endif %}

  {% for p in items %}
  <div class="col-lg-4 col-md-6 col-sm-10 mb-5 text-center">
    <img src="{{ p.avatar | relative_url }}" alt="{{ p.name }}" class="team-avatar mb-3">
    <h5 class="team-name mb-1">{{ p.name }}</h5>

    {% if p.intro and p.intro != "" %}
    <p class="team-intro">
      {{ p.intro | markdownify | strip | remove: "<p>" | remove: "</p>" }}
    </p>
    {% endif %}

    {% if p.link and p.link != "" %}
    <a href="{{ p.link }}" target="_blank" rel="noopener noreferrer" class="team-btn">Homepage</a>
    {% endif %}
  </div>
  {% endfor %}
</div>


{% endif %}

{% endfor %}

</div>
