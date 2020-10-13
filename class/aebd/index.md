---
layout: default
title: AEBD
image: img/aebd.png
---

<h3 style="text-align:center;">Administração e Exploração de Base de Dados</h3>

---

{% for class in site.data.aebd.class %}

<h4> <a href="" target="_blank">{{class.code}} - {{class.title}}</a></h4>   
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
<h2>Trabalho Prático</h2>
<p> Em construção... </p>

---

<h2>Teste</h2>
<p> Em construção... </p>

---

<h2> Submissão de FE</h2>
<p> <i class="fa fa-envelope"></i>  Enviar email para <a href="mailto:hpeixoto@di.uminho.pt?subject=aebd/FEXX/GXX">hpeixoto@di.uminho.pt</a> <br>
Assunto: aebd/FEXX/GXX </p>