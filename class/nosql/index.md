---
layout: default
title: noSQL
image: img/nosql.png
---

<h3 style="text-align:center;">Base de Dados noSQL</h3>

---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.nosql.class %}

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
<h2> <i class="fa fa-hand-paper-o"></i> Trabalho Prático</h2>
<p> Em construção... </p>

---

<h2> <i class="fa fa-file-text-o"></i> Teste</h2>
<p> 06 janeiro 2021 - 09h </p>

---

<h2> <i class="fa fa-envelope"></i> Submissão de FE</h2>
<p> Submissão por grupo no Blackboard (Troca de Arquivos do Grupo). Submeter pdf com o nome da Ficha de Exercícios. </p>