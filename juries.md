---
layout: default
title: Juries
image: "none"
---

<h2> Arguições Externas </h2>
{% for jurie in site.data.juries.juries %}

{% if jurie.external == 1 %}

<h3>  {% if jurie.type == 2 %}Msc. - {% endif %} {% if jurie.type == 3 %}PhD. - {% endif %} {% if jurie.type == 4 %}Pre-PhD. .- {% endif %} {{jurie.title}}</h3>
<i class="fa fa-location-arrow"><strong> Location: </strong> </i> {{jurie.institution}} <br> 
<i class="fa fa-calendar"><strong> Date: </strong></i> {{ jurie.date }} 
{% if jurie.url and jurie.url != "" %} <br> <i class="fa fa-external-link" aria-hidden="true"><strong> Source: </strong></i><a href="{{ jurie.url }}"> link</a> {% endif %} <br>
<i class="fa fa-user"><strong> Candidate: </strong></i> {{ jurie.student }}

---
{% endif %}

{% endfor %}


<h1> Arguições Internas </h1>
{% for jurie in site.data.juries.juries %}

{% if jurie.external == 0 %}
<h3>  {{jurie.type}} {{jurie.title}}</h3>
<i class="fa fa-location-arrow"><strong> Location: </strong> </i> {{jurie.institution}} <br> 
<i class="fa fa-calendar"><strong> Date: </strong></i> {{ jurie.date }} 
{% if jurie.url and jurie.url != "" %} <br> <i class="fa fa-external-link" aria-hidden="true"><strong> Source: </strong></i><a href="{{ jurie.url }}"> link</a> {% endif %} <br>
<i class="fa fa-user"><strong> Candidate: </strong></i> {{ jurie.student }}

---
{% endif %}

{% endfor %}