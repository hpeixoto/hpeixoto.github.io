---
layout: default
title: DC
subtitle: Descoberta do Conhecimento
image: "none"
---


---
<h2> <i class="fa fa-file-o"></i> Aulas </h2>
---
{% for class in site.data.dc.class %}

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
<p> <!--<a href="" target="_blank">--><i class="fa fa-file-text-o"></i> Enunciado <!--</a>--> <br>
<i class="fa fa-calendar"></i> <strong> Datas: </strong> <br>
Entrega no dia <strong> a definir...</strong> via Partilha de ficheiros do grupo do Blackboard. <br>
Apresentação no dia <strong> a definir...</strong> <br>
Apresentações de 15' com 5' para questões. </p>

---

<h2> <i class="fa fa-envelope"></i> Submissão de FE</h2>
<p> Submissão por grupo no Blackboard (Troca de Arquivos do Grupo). Submeter pdf com o nome da Ficha de Exercícios. </p>