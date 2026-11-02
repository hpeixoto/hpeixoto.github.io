---
layout: default
title: AEC
subtitle: Aprendizagem e Extração de Conhecimento
image: "none"
---

<style>
.year-accordion {
  border: 1px solid #e4e4e4;
  border-radius: 4px;
  margin-bottom: 12px;
  background: #fff;
}
.year-accordion > summary {
  cursor: pointer;
  padding: 12px 16px;
  font-size: 20px;
  font-weight: 700;
  color: #048A81;
  list-style: none;
  outline: none;
}
.year-accordion > summary::-webkit-details-marker { display: none; }
.year-accordion > summary:hover { background: #f7f7f7; }
.year-accordion > summary .year-chevron {
  float: right;
  margin-top: 4px;
  font-size: 15px;
  color: #999;
  transition: transform 0.15s ease-in-out;
}
.year-accordion[open] > summary {
  border-bottom: 1px solid #e4e4e4;
}
.year-accordion[open] > summary .year-chevron {
  transform: rotate(90deg);
}
.year-accordion-body { padding: 4px 16px 16px; }
.year-accordion-body hr { margin: 14px 0; }
.year-accordion-body h4 { margin-top: 18px; }
</style>

{% assign years = "2026/27,2025/26,2022/23" | split: "," %}
{% assign data_keys = "aec_2627,aec_2526,aec_2223" | split: "," %}

{% for key in data_keys %}
{% assign i = forloop.index0 %}
{% assign year = years[i] %}
{% assign dataset = site.data[key] %}

<details class="year-accordion" {% if forloop.first %}open{% endif %}>
<summary><i class="fa fa-calendar"></i> {{ year }}<i class="fa fa-chevron-right year-chevron"></i></summary>
<div class="year-accordion-body" markdown="1">

{% for class in dataset.class %}
<h4> <span style="color: #048A81; text-decoration: none;">{{class.code}} - {{class.title}}</span></h4>
{% if class.date %}<i class="fa fa-calendar"></i> {{ class.date }} {% endif %}
<ul>
    {% if class.plan %}
        <li> <a href="{{ class.plan }}" target='_blank'> Planeamento da Aula </a></li>
    {% endif %}
    {% if class.slides %}
        <li> <a href="{{ class.slides }}" target='_blank'> Slides </a> </li>
    {% endif %}
    {% if class.exercise %}
        <li> <a href="{{ class.exercise }}" target='_blank'> Ficha de Exercícios </a> </li>
    {% endif %}
    {% if class.material %}
        <li> <a href="{{ class.material }}" target='_blank'> Material de Apoio </a> </li>
    {% endif %}
</ul>
{% if class.topics %}<strong> tópicos: </strong> {{class.topics}} {% endif %}

{% unless forloop.last %}---{% endunless %}
{% endfor %}

</div>
</details>
{% endfor %}
