---
layout: default
title: Material
image: "none"
---


{% for sebenta in site.data.sebentas.sebenta %}

<h3>  <a href="{{ sebenta.url }}" target="_blank">{{sebenta.title}} <i class="fa fa-external-link" aria-hidden="true"></i></a></h3>     
<i class="fa fa-calendar"></i> {{ sebenta.date }}    

---

{% endfor %}