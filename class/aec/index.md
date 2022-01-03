---
layout: default
title: AEC
subtitle: Aprendizagem e Extração de Conhecimento
image: "none"
---


<!--<h3 style="text-align:center;">Sistemas de Aprendizagem e Extração de Conhecimento</h3>-->

---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.aec.class %}

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

<h2>Links úteis</h2>
<p> <a href="https://en.wikipedia.org/wiki/Precision_and_recall" target="_blank"> DM - Métricas </a> </p>


<h2>Discord Server</h2>
<p> <i class="fa fa-comments" aria-hidden="true"></i> <a href="https://discord.gg/nx7QM7EG" target="_blank"> AEC - server </a> </p>

---

<h2> <i class="fa fa-hand-paper-o"></i> Trabalho Prático</h2>
<p> <a href="../../data/aec/aec_TPratico.pdf" target="_blank"><i class="fa fa-file-text-o"></i> Enunciado</a> <br>
<p> <i class="fa fa-calendar"></i> <strong> Datas: </strong> <br>
Entrega: <strong> 17 janeiro 2022</strong> (Partilha de ficheiros do grupo do Blackboard.)<br>
Apresentação: <strong> 19 janeiro 2022</strong> <br>
Apresentações de 20' com 5' para questões. </p>