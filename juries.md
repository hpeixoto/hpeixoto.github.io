---
layout: page
title: Juries
subtitle: "&nbsp;&nbsp;&nbsp;"
---

{% for jurie in site.data.juries.juries %}

<h4> <a href="{{ jurie.url }}"> {{jurie.title}} </a> </h4>
<i class="fa fa-location-arrow"></i> {{jurie.institution}} | <i class="fa fa-calendar"></i> {{ jurie.date }}  
<strong> Candidate: </strong>{{ jurie.student }}

---

{% endfor %}