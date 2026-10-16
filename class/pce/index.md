---
layout: default
title: PCE
subtitle: Processo Clínico Eletrónico
image: "none"
---

---
<h2> <i class="fa fa-calendar"></i> 2024/25 </h2>
---

{% for class in site.data.pce_2425.class %}

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
