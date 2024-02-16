---
layout: default
title: BDCGH
subtitle: Bases de Dados Clínicas e de Gestão Hospitalar
image: "none"
---


<!--<h3 style="text-align:center;">Sistemas de Aprendizagem e Extração de Conhecimento</h3>-->

---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.bdcgh.class %}

<h4> <span style="color: #048A81; text-decoration: underline;">{{class.code}} - {{class.title}}</span></h4>
<i class="fa fa-calendar"></i> {{ class.date }} 
<ul>
    <li> <a href="{{ class.plan }}" target='_blank'> Planeamento da Aula </a></li>
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
<strong> tópicos: </strong> {{class.topics}} 

---
{% endfor %}