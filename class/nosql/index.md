---
layout: default
title: noSQL
image: img/nosql.png
---


<!--<h3 style="text-align:center;">Sistemas de Aprendizagem e Extração de Conhecimento</h3>-->

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

<h2> Trabalho Prático </h2>
<!--<h2> <i class="fa fa-hand-paper-o"></i> Trabalho Prático</h2>-->
<p> 
    <a href="../../data/nosql/tp/NOSQL_Enunciado_TP2022.pdf" target="_blank"><i class="fa fa-file-text-o"></i> Enunciado Trabalho Prático</a> <br>
    <a href="../../data/nosql/tp/hr.zip" target="_blank"><i class="fa fa-file-text-o"></i> hr.zip</a> </p>
<p> 
    <i class="fa fa-calendar"></i> <strong> Data Entrega: </strong>  12 jun 2022 <br> 
    <i class="fa fa-calendar"></i> <strong> Apresentações: </strong>  a definir 
</p>

---
<h2> Material de Apoio </h2>
<!--<h2> <i class="fa fa-hand-paper-o"></i> Trabalho Prático</h2>-->
<p> <a href="https://mega.nz/file/w0szwY7L#2onFNpqZO1sdy-wS-XLYeq2OATPHCXwoiDRnQu7QPNU" target="_blank"><i class="fa fa-file-text-o"></i> Máquina Virtual com oracle</a> </p>
<p> <i class="fa fa-user"></i> <strong> user: </strong>  root <br> 
<i class="fa fa-lock"></i> <strong> senha: </strong>  uminho#2022! </p>