---
layout: default
title: Teaching
image: "none"
---



{% for class in site.data.class.class %}

<h3>  <a href="{{ class.url }}" target="_blank">{{class.name}} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>     
<i class="fa fa-location-arrow"></i> {{class.institution}}    
<i class="fa fa-calendar"></i> {{ class.course }}   
<strong> topics: </strong> {{class.topics}} 

---

{% endfor %}