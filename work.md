---
layout: default
title: Work
image: "none"
---

{% for job in site.data.work.jobs %}

<h3> <a href="{{ job.url }}"> {{job.title}} </a> </h3>
<i class="fa fa-map-marker"></i> {{job.institution}}   
<i class="fa fa-calendar"></i> {{ job.start }}{% if job.end %} - {{ job.end }} {% endif %}  
<br>
<strong> Main Responsibilities: </strong>{{ job.tasks }}

---

{% endfor %}
