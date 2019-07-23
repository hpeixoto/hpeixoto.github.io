---
layout: default
title: Juries
image: "none"
---

{% for jurie in site.data.juries.juries %}
<h3>  <a href="{{ jurie.url }}" target="_blank">{{jurie.title}} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>
<i class="fa fa-location-arrow"></i> {{jurie.institution}} | <i class="fa fa-calendar"></i> {{ jurie.date }}  
<strong> Candidate: </strong>{{ jurie.student }}

---

{% endfor %}