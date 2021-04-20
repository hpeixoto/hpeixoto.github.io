---
layout: default
title: SAEC
subtitle: Sistemas de Aprendizagem e Extração de Conhecimento
image: "none"
---


<!--<h3 style="text-align:center;">Sistemas de Aprendizagem e Extração de Conhecimento</h3>-->

---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.saec.class %}

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
<p> <a href="../../data/saec/tpraticoSAEC.pdf" target="_blank"><i class="fa fa-file-text-o"></i> Enunciado</a> <br>
<p> <i class="fa fa-calendar"></i> <strong> Datas: </strong> <br>
Entrega: <strong> 13 junho 2021</strong> (Partilha de ficheiros do grupo do Blackboard.)<br>
Apresentação: <strong> 15 junho 2021</strong> <br>
Apresentações de 15' com 5' para questões. </p>

---

<h2> <i class="fa fa-envelope"></i> Submissão de FE</h2>
<p> Submissão por grupo no Blackboard (Troca de Arquivos do Grupo). Colocando pastas para cada uma das FE, e um PDF para cada elemento do grupo.</p>