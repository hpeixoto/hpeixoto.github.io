---
layout: default
title: AIEB
image: img/nosql.png
---


<!--<h3 style="text-align:center;">Sistemas de Aprendizagem e Extração de Conhecimento</h3>-->

---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.aieb.class %}

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
<h2> Material de Apoio </h2>
<h2> <i class="fa fa-hand-paper-o"></i> Trabalho Prático</h2>
<p> <i class="fa fa-calendar"></i> <strong> Datas: </strong> <br>
Apresentação Grupo: <strong> 09 Junho - 09h </strong> <br>
Entrega Relatório Individual: <strong> 19 Junho - 23h59 </strong> <br>