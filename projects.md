---
layout: default
title: Projects
image: "none"
---

{% for proj in site.data.projects.projects %}

<h3>  <a href="{{ proj.url }}" target="_blank">{{ proj.name }} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>   
<i class="fa fa-eye"></i> {{ proj.type }}    
<i class="fa fa-code"></i> {{proj.languages}}   
<strong> Topics: </strong> {{ proj.topics }}   

---

{% endfor %}