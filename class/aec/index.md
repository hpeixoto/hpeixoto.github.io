---
layout: default
title: AEC
subtitle: Aprendizagem e Extração de Conhecimento
image: "none"
---

{% assign years = "2026/27,2025/26,2022/23" | split: "," %}
{% assign data_keys = "aec_2627,aec_2526,aec_2223" | split: "," %}

{% for key in data_keys %}
{% assign i = forloop.index0 %}
{% assign year = years[i] %}

---
<h2> <i class="fa fa-calendar"></i> {{ year }} </h2>
---

{% assign dataset = site.data[key] %}
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

---
{% endfor %}
{% endfor %}
