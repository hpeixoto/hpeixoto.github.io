---
layout: publications
title: Education
subtitle:
---
{% for ed in site.data.education.education %}

<div class="row">
    <div class="three columns">
        <a href="http://uminho.pt">
            <img class="u-max-full-width" src="{{ ed.icon }}" alt="Escola de Engenharia da Universidade do Minho">
        </a>
        <br>
        <i class="fa fa-clock-o"></i> {{ ed.start }}-{{ ed.end }}</div>
    <div class="eight columns">
        <a href="http://www.biomedica.eng.uminho.pt/">
            <strong>{{ed.degree}}</strong>
        </a>(GPA: {{ ed.grade }} out of 20)
        <br>
        <p>{{ ed.topics }}</p>
    </div>
</div>     

{% endfor %}
