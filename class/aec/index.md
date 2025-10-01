---
layout: default
title: AEC
subtitle: Aprendizagem e Extração de Conhecimento
image: "none"
---

---
<h2> <i class="fa fa-file-o"></i> Aula </h2>
---
{% for class in site.data.aec.class %}

<h4> <span style="color: #048A81; text-decoration: none;">{{class.code}} - {{class.title}}</span></h4>
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