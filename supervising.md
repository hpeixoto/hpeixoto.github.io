---
layout: page
title: Supervising
image: "none"
---

{% for supervision in site.data.supervision.supervisions %}
<h3>  <a href="{{ jurie.url }}" target="_blank">{{supervision.title}} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>
<i class="fa fa-location-arrow"></i> {{supervision.institution}} | <i class="fa fa-calendar"></i> {{ supervision.date }}  
<strong> Candidate: </strong>{{ supervision.student }}

---

{% endfor %}