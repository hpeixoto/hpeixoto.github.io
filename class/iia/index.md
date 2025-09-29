---
layout: default
title: IIA
image: none
---

---
<h2> <i class="fa fa-file-o"></i> Aula </h2>
---
{% for class in site.data.iia.class %}

<h4> <span style="color: #048A81; text-decoration: none;">{{class.code}} - {{class.title}}</span></h4>
<i class="fa fa-calendar"></i> {{ class.date }} 
<ul>
    <li> <a href="{{ class.slides }}" target='_blank'> Slides </a> </li>
    <li> <a href="{{ class.exercise }}" target='_blank'> Ficha de Grupo </a> </li>
    <li> <a href="{{ class.material }}" target='_blank'> Material de Apoio </a> </li>
</ul>  
<strong> tópicos: </strong> {{class.topics}} 

---
{% endfor %}