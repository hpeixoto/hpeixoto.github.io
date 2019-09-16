---
layout: default
title: noSQL
image: img/nosql.png
---



{% for class in site.data.nosql.class %}

<h3>  <a href="{{ class.url }}" target="_blank">{{class.code}} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>     
<i class="fa fa-location-arrow"></i> {{class.institution}}    
<i class="fa fa-calendar"></i> {{ class.course }}   
<strong> topics: </strong> {{class.topics}} 

---

{% endfor %}