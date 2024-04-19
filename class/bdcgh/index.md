---
layout: default
title: BDCGH
subtitle: Bases de Dados Clínicas e de Gestão Hospitalar
image: "none"
---

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

---
<h2> Trabalho Prático </h2>
<h2> <i class="fa fa-hand-paper-o"></i> <a href="../../data/bdcgh/bdcgh_trabPrat.pdf" target="_blank"> Trabalho Prático </a></h2> 
<p> <i class="fa fa-calendar"></i> <strong> Datas: </strong> <br>
Entrega Trabalho (elearning) Grupo: <strong> 29 maio 2024 </strong> <br>
Apresentações: <strong> 05 junho 2024 </strong> <br>