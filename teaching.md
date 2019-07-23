---
layout: page
title: Teaching
image: "none"
---

{% for class in site.data.class.class %}

<h3> <img src="{{ class.icon }}" alt="logs" class="img-responsive"> <a href="{{ class.url }}"> {{class.title}} </a> </h3>
<i class="fa fa-location-arrow"></i> {{class.institution}}    
<i class="fa fa-calendar"></i> {{ class.start }}{% if class.end %} - {{ class.end }} {% endif %}  
<strong> Main Responsabilities: </strong>{{ class.tasks }}


---

{% endfor %}