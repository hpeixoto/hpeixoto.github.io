---
layout: default
title: noSQL
image: img/nosql.png
---

<h3 style="text-align:center;">Base de Dados noSQL</h3>

---

{% for class in site.data.nosql.class %}

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
<p> 
<i class="fa fa-file"></i> <a href="../../data/nosql/tp/tp.pdf">Enunciado do trabalho prático </a> <br>
<i class="fa fa-calendar"></i> Entrega a  13/01/2020 <br>
<i class="fa fa-laptop"></i> Apresentação de 15' com horário a definir no dia 15/01/2020. </p>

---

<h2>Teste</h2>
<p> 
<i class="fa fa-calendar"></i> A realizar no dia 18/12/2019 pelas 09h. </p>

---

<h2> Submissão de FE</h2>
<p> <i class="fa fa-envelope"></i>  Enviar email para <a href="mailto:hpeixoto@di.uminho.pt?subject=A12345/nosql/FEXX">hpeixoto@di.uminho.pt</a> <br>
Assunto: A12345/nosql/FEXX </p>