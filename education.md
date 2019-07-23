---
layout: default
title: Education
image: "none"
---

{% for ed in site.data.education.education %}

<h3> <a href="{{ ed.url }}"> {{ed.course}} </a> <small> ({{ed.degree}}) </small> </h3>
<i class="fa fa-graduation-cap"></i> {{ed.school}} - {{ed.local}}   
<i class="fa fa-clock-o"></i> {{ ed.start }}-{{ ed.end }}   
GPA: {{ ed.grade }}      
<strong> Topics: </strong>{{ ed.topics }}

---

{% endfor %}
