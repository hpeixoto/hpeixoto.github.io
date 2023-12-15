---
layout: page
title: About me
subtitle: Researcher at Centro Algoritmi, University of Minho
---

Currently working as Auxiliar Researcher at <a href="http://algoritmi.uminho.pt" target="_blank">Centro Algoritmi</a> in the <a href="https://www.uminho.pt/PT" target="_blank">University of Minho</a>.  Invited Assistant Professor, teaching Knowledge Discovery, noSQL Databases, Database Administration and Electronic Health Records. Previously worked as Information Systems Director at <a href="http://www.chedv.min-saude.pt/" target="_blank">Centro Hospitalar de Entre o Douro e Vouga E.P.E.</a>, also performed as Project Manager and IT Specialist at <a href="http://www.chts.min-saude.pt/" target="_blank">Centro Hospitalar do Tâmega e Sousa E.P.E.</a> during the early days! Long-held interests in Machine Learning, Data Mining, eHealth, Medical Information Systems, interoperability and integration in healthcare domain.

---

##  Interests

<div class="main-explain-area jumbotron">
    <strong><i class="fa fa-book"></i> Research:</strong><br> 
        Interoperability | Electronic Health Records | Multi-agent Systems | Knowledge Representation | Business Intelligence | Knowledge Extraction | Decision Support Systems | CRISP-DM | Data Mining<br><br><br>
    <strong><i class="fa fa-database"></i> Databases:</strong><br> 
        mySQL | Oracle | MongoDB | neo4j   <br><br><br>
    <strong><i class="fa fa-code"></i> Languages:</strong><br> 
        PHP | python | Javascript | .Net | Visual Basic | R   <br><br><br> 
    <strong><i class="fa fa-slack"></i> Others:</strong><br> 
        RapidMiner | Mirthconnect | Docker | Bootstrap | git | Joomla | WordPress <br>   
</div> 

---
## Lastest publications

#### Book chapters
{% assign counter = 1 %}
{% for pub in site.data.publications.papers %}
{% if pub.type == 'book' and counter < 4 %}
{% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {% if pub.volume %}{{ pub.volume }},{% endif %} {% if pub.booktitle %}{{ pub.booktitle }}{% endif %} {% if pub.conference %}{{ pub.conference }}{% endif %}. <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a> 
    {% endif %}
{% endfor %}

#### Journals
{% assign counter = 1 %}
{% for pub in site.data.publications.papers %}
{% if pub.type == 'journal' and counter < 4 %}
{% assign counter = counter | plus:1 %}
{{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {{pub.journal}}{% if pub.volume %}, {{ pub.volume }}{% endif %}{% if pub.publisher %}, {{ pub.publisher}}{% endif %}. <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
{% endif %}
{% endfor %}

#### Conf. Papers
{% assign counter = 1 %}
{% for pub in site.data.publications.papers %}
{% if pub.type == 'conference' and counter < 4 %}
 {% assign counter = counter | plus:1 %}
  {{ counter }}. {{ pub.authors }} ({{ pub.year }}). _**{{ pub.title }}**_. {{ pub.conference }} <a href="{{ pub.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a>  
    {% endif %}
{% endfor %}

<p><a href="/publications"><i class="fa fa-plus-square"></i> <strong>Show More</strong></a></p>

