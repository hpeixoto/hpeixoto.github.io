---
layout: default
title: Experience
image: "none"
---

{% for exp in site.data.experience.experience %}

### <a> {{exp.name}} </a> <small> ({{exp.role}}) </small>
<i class="fa fa-map-marker"></i> {{exp.local}}   
<i class="fa fa-clock-o"></i> {{ exp.start }}-{{ exp.end }}   
<br>
<strong> Main Responsabilities: </strong>{{ exp.topics }}

---

{% endfor %}

