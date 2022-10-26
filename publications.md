---
layout: default
title: Publications
image: "none"
---

{% assign counter = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
 {% assign counter = counter | plus:1 %}
{% endfor %}

{% assign scop = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
  {% if pub.scopus %}
    {% assign scop = scop | plus:1 %}
  {% endif %}
{% endfor %}

{% assign isi = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
  {% if pub.isi %}
    {% assign isi = isi | plus:1 %}
  {% endif %}
{% endfor %}

{% assign dblp = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
  {% if pub.isi %}
    {% assign dblp = dblp | plus:1 %}
  {% endif %}
{% endfor %}


Total: <strong>{{counter}}</strong> | ({{scop}}) Scopus&nbsp;&nbsp; | &nbsp;&nbsp;({{isi}}) ISI&nbsp;&nbsp;|&nbsp;&nbsp;({{dblp}}) DBLP

## Journals

{% assign counter = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
 {% assign counter = counter | plus:1 %}
 {% if pub.type == "journal" %} {{counter}}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_, {{ pub.journal }}. {% if pub.volume %}{{ pub.volume }},{% endif %} {% if pub.booktitle %} {{ pub.booktitle }} {% endif %} {% if pub.pages %} (pp {{ pub.pages }}),{% endif %} {% if pub.publisher %} {{ pub.publisher }}. {% endif %} {% if pub.url %}<a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %} {% if pub.scopus %} <img src="../img/scopus.png" name="scopus" alt="scopus" height="13px"/> {% endif %}{% if pub.isi %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/> {% endif %}{% if pub.dblp %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/> {% endif %} {% if pub.q %} <strong> (Q{{pub.q}}) </strong> {% endif %} {% if pub.citations %} <span style='color: green; font-size: 12px;'> Nº de citações: {{ pub.citations }} </span> {% endif %}  {% endif %}
{% endfor %}

## Book Chapters
{% assign counter = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
 {% assign counter = counter | plus:1 %}
  {% if pub.type == "book" %} {{counter}}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {% if pub.volume %}{{ pub.volume }},{% endif %} {% if pub.booktitle %} {{ pub.booktitle }} {% endif %} {% if pub.pages %} (pp {{ pub.pages }}),{% endif %} {% if pub.publisher %} {{ pub.publisher }}. {% endif %} {% if pub.url %}<a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %} {% if pub.scopus %} <img src="../img/scopus.png" alt="scopus" name="scopus" height="13px"/> {% endif %}{% if pub.isi %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/> {% endif %}{% if pub.dblp %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/> {% endif %} {% if pub.q %} <strong> (Q{{pub.q}}) </strong> {% endif %}{% if pub.citations %} <span style='color: green; font-size: 12px;'> Nº de citações: {{ pub.citations }} </span> {% endif %} {% endif %}
{% endfor %}

## Conference Papers
{% assign counter = 0 %}
{% assign pub = "" %}
{% for pub in site.data.publications.papers %}
 {% assign counter = counter | plus:1 %}
  {% if pub.type == "conference" %} {{counter}}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {% if pub.volume %}{{ pub.volume }},{% endif %} {% if pub.booktitle %} {{ pub.booktitle }} {% endif %} {% if pub.pages %} (pp {{ pub.pages }}),{% endif %} {% if pub.publisher %} {{ pub.publisher }}. {% endif %} {% if pub.url %}<a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>{% endif %} {% if pub.scopus %} <img src="../img/scopus.png" alt="scopus" name="scopus" height="13px"/> {% endif %}{% if pub.isi %} <img src="../img/isi.png" alt="isiwebofknowledge" height="13px"/> {% endif %}{% if pub.dblp %} <img src="../img/dblp.jpeg" alt="dblp" height="13px"/> {% endif %} {% if pub.q %} <strong> (Q{{pub.q}}) </strong> {% endif %} {% if pub.citations %} <span style='color: green; font-size: 12px;'> Nº de citações: {{ pub.citations }} </span> {% endif %}  {% endif %}
{% endfor %}

---

### Thesis
{% assign counter = 0 %}
{% for pub in site.data.publications.thesis %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. ({{ pub.degree }}) <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
{% endfor %}