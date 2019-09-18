---
layout: default
title: Publications
image: "none"
---

### Book Chapters
{% assign counter = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.bookchaps %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {% if pub.volume %}{{ pub.volume }},{% endif %} {% if pub.booktitle %}{{ pub.booktitle }}{% endif %} (pp {{ pub.pages }}), {{ pub.publisher }}. <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a> 
{% endfor %}

---
### Journal Articles
{% assign counter = 0 %}
{% for pub in site.data.publications.journals %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {{pub.journal}}{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.publisher %}, {{ pub.publisher}}{% endif %}. <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
{% endfor %}

---

### Conference Papers
{% assign counter = 0 %}
{% for pub in site.data.publications.confs %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {{ pub.conference }} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
{% endfor %}

---

### Thesis
{% assign counter = 0 %}
{% for pub in site.data.publications.thesis %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. ({{ pub.degree }}) <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
{% endfor %}