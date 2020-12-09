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
<p> <a href="../../data/nosql/tp/NOSQL_TP2020.pdf" target="_blank"><i class="fa fa-file-text-o"></i> Enunciado </a> <br>
<a href="../../data/nosql/tp/hr.zip" ><i class="fa fa-file-text-o"></i> Material </a>  <br> 
<i class="fa fa-calendar"></i> <strong> Entrega no dia </strong> 27/01/2021 <br>
<i class="fa fa-calendar"></i> <strong> Apresentações no dia </strong> ??/01/2021 <br>
A apresentação do trabalho será feita aos docentes da disciplina e consistirá numa apresentação do trabalho realizado e uma demonstração das bases de dados implementadas, bem como das queries definidas e criadas. Todos os elementos do grupo deverão estar presentes durante a apresentação do trabalho. </p>

---

<h2> <i class="fa fa-file-text-o"></i> Teste</h2>
<p> 06 janeiro 2021 - 09h </p>

---

<h2> <i class="fa fa-envelope"></i> Submissão de FE</h2>
<p> Submissão por grupo no Blackboard (Troca de Arquivos do Grupo). Submeter pdf com o nome da Ficha de Exercícios. </p>