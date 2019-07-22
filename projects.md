---
layout: default
title: Projects
subtitle: "&nbsp;&nbsp;&nbsp;"
---



{% for proj in site.data.projects.projects %}

<h3> {{ proj.name }} </h3>   
{{ proj.type }} <a href="{{ proj.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>   
<i class="fa fa-code"></i> - {{proj.languages}}   
<strong> Topics: </strong> {{ proj.topics }}   

---

{% endfor %}