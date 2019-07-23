---
layout: page
title: Teaching
image: "none"
---



{% for class in site.data.class.class %}
---
<h3> {{class.name}} </h3>
<a href="{{ class.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i> webpage </a>   
<i class="fa fa-location-arrow"></i> {{class.institution}}    
<i class="fa fa-calendar"></i> {{ class.course }}   
<strong> topics: </strong> {{class.topics}} 

{% endfor %}