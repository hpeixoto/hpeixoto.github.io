---
layout: default
title: Publications
image: "none"
---
 
{% assign papers = site.data.publications.publications %}
 
{% assign total = papers | size %}
 
{% assign scop_count = 0 %}
{% for pub in papers %}
  {% if pub.scopus != nil and pub.scopus != "" %}
    {% assign scop_count = scop_count | plus: 1 %}
  {% endif %}
{% endfor %}
 
{% assign wos_count = 0 %}
{% for pub in papers %}
  {% if pub.wos != nil and pub.wos != "" %}
    {% assign wos_count = wos_count | plus: 1 %}
  {% endif %}
{% endfor %}
 
{% assign dblp_count = 0 %}
{% for pub in papers %}
  {% if pub.dblp != nil and pub.dblp != "" %}
    {% assign dblp_count = dblp_count | plus: 1 %}
  {% endif %}
{% endfor %}
 
Total: <strong>{{ total }}</strong> &nbsp;|&nbsp; ({{ scop_count }}) Scopus &nbsp;|&nbsp; ({{ wos_count }}) ISI/WoS &nbsp;|&nbsp; ({{ dblp_count }}) DBLP
 
---
 
## Journals
 
{% assign counter = 0 %}
{% for pub in papers %}
  {% if pub.type == "journal" %}
    {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {{ pub.venue }}.{% if pub.volume %} Vol. {{ pub.volume }}{% if pub.number %}({{ pub.number }}){% endif %},{% endif %}{% if pub.pages %} pp. {{ pub.pages }}.{% endif %}{% if pub.publisher %} {{ pub.publisher }}.{% endif %}{% if pub.doi %} DOI: [{{ pub.doi }}](https://doi.org/{{ pub.doi }}).{% endif %}{% if pub.url %} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %}{% if pub.scopus != nil and pub.scopus != "" %} <img src="../img/scopus.png" alt="scopus" height="13px"/>{% endif %}{% if pub.wos != nil and pub.wos != "" %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/>{% endif %}{% if pub.dblp != nil and pub.dblp != "" %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/>{% endif %}{% if pub.q != nil and pub.q != "" %} **(Q{{ pub.q }})**{% endif %}{% if pub.qdesc != nil and pub.qdesc != "" %} *({{ pub.qdesc }})*{% endif %}{% if pub.citations and pub.citations != 0 %} <span style='color: green; font-size: 12px;'>Nº de citações: {{ pub.citations }}</span>{% endif %}
 
  {% endif %}
{% endfor %}
 
---
 
## Book Chapters
 
{% assign counter = 0 %}
{% for pub in papers %}
  {% if pub.type == "book_chapter" %}
    {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_.{% if pub.venue %} In _{{ pub.venue }}_.{% endif %}{% if pub.volume %} Vol. {{ pub.volume }},{% endif %}{% if pub.pages %} pp. {{ pub.pages }}.{% endif %}{% if pub.publisher %} {{ pub.publisher }}.{% endif %}{% if pub.doi %} DOI: [{{ pub.doi }}](https://doi.org/{{ pub.doi }}).{% endif %}{% if pub.url %} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %}{% if pub.scopus != nil and pub.scopus != "" %} <img src="../img/scopus.png" alt="scopus" height="13px"/>{% endif %}{% if pub.wos != nil and pub.wos != "" %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/>{% endif %}{% if pub.dblp != nil and pub.dblp != "" %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/>{% endif %}{% if pub.citations and pub.citations != 0 %} <span style='color: green; font-size: 12px;'>Nº de citações: {{ pub.citations }}</span>{% endif %}
 
  {% endif %}
{% endfor %}
 
---
 
## Conference / Proceedings Papers
 
{% assign counter = 0 %}
{% for pub in papers %}
  {% if pub.type == "proceedings" %}
    {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_.{% if pub.venue %} In _{{ pub.venue }}_.{% endif %}{% if pub.series and pub.series != pub.venue %} ({{ pub.series }}){% endif %}{% if pub.volume %} Vol. {{ pub.volume }},{% endif %}{% if pub.pages %} pp. {{ pub.pages }}.{% endif %}{% if pub.publisher %} {{ pub.publisher }}.{% endif %}{% if pub.doi %} DOI: [{{ pub.doi }}](https://doi.org/{{ pub.doi }}).{% endif %}{% if pub.url %} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %}{% if pub.scopus != nil and pub.scopus != "" %} <img src="../img/scopus.png" alt="scopus" height="13px"/>{% endif %}{% if pub.wos != nil and pub.wos != "" %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/>{% endif %}{% if pub.dblp != nil and pub.dblp != "" %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/>{% endif %}{% if pub.citations and pub.citations != 0 %} <span style='color: green; font-size: 12px;'>Nº de citações: {{ pub.citations }}</span>{% endif %}
 
  {% endif %}
{% endfor %}
 
---
 
## Books & Edited Volumes
 
{% assign counter = 0 %}
{% for pub in papers %}
  {% if pub.type == "book" or pub.type == "proceedings_book" %}
    {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_.{% if pub.venue %} _{{ pub.venue }}_.{% endif %}{% if pub.volume %} Vol. {{ pub.volume }}.{% endif %}{% if pub.publisher %} {{ pub.publisher }}.{% endif %}{% if pub.isbn %} ISBN: {{ pub.isbn }}.{% endif %}{% if pub.doi %} DOI: [{{ pub.doi }}](https://doi.org/{{ pub.doi }}).{% endif %}{% if pub.url %} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %}
 
  {% endif %}
{% endfor %}
 
---
 
## Datasets & Other
 
{% assign counter = 0 %}
{% for pub in papers %}
  {% if pub.type == "dataset" or pub.type == "editorial" or pub.type == "other" %}
    {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_.{% if pub.venue %} {{ pub.venue }}.{% endif %}{% if pub.publisher %} {{ pub.publisher }}.{% endif %}{% if pub.url %} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %}
 
  {% endif %}
{% endfor %}
 
---
 
### Thesis
 
{% assign counter = 0 %}
{% for pub in site.data.publications.thesis %}
  {% assign counter = counter | plus: 1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. ({{ pub.degree }}) <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>
{% endfor %}