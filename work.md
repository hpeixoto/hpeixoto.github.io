---
layout: default
title: Work
subtitle: "&nbsp;&nbsp;&nbsp;" 
---



{% for job in site.data.work.jobs %}

<h3> <img src="{{ job.icon }}" alt="logs" class="img-responsive"> <a href="{{ job.url }}"> {{job.title}} </a> </h3>
<i class="fa fa-location-arrow"></i> {{job.institution}}    
<i class="fa fa-calendar"></i> {{ job.start }}-{{ job.end }}   
<strong> Main Responsabilities: </strong>{{ job.tasks }}


---

{% endfor %}
