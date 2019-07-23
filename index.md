---
layout: page
title: About me
subtitle: Post-Doctoral researcher at University of Minho
---

Currently working as Integrated Researcher at <a href="http://algoritmi.uminho.pt" target="_blank">Algoritmi Research Center</a> at the <a href="https://www.uminho.pt/PT" target="_blank">University of Minho</a>. Invited Asssintant Professor, teaching Knowledge Discovery, noSQL Databases, Database Administration and Electronic Health Records.    
Previously worked as Information Systems Director at <a href="http://www.chedv.min-saude.pt/" target="_blank">Centro Hospitalar de Entre o Douro e Vouga E.P.E.</a>, also performed as Project Manager and IT Specialist at  <a href="http://www.chts.min-saude.pt/" target="_blank">Centro Hospitalar do Tâmega e Sousa E.P.E.</a> during the early days!
Long-held interests in Machine Learning, Data Mining, eHealth, Medical Information Systems, interoperability and integration in healthcare arena.

---

<h2> Interests </h2>
<div class="main-explain-area jumbotron">
    <strong><i class="fa fa-book"></i> Research:</strong><br> 
        Data Mining | Electronic Health Record | Multi-agent Systems | Interoperability | Business Intelligence  <br><br><br>
    <strong><i class="fa fa-database"></i> Databases:</strong><br> 
        mySQL | Oracle | MongoDB | neo4j   <br><br><br>
    <strong><i class="fa fa-code"></i> Languages:</strong><br> 
        PHP | python | Javascript | .Net | Visual Basic | R   <br><br><br> 
    <strong><i class="fa fa-slack"></i> Others:</strong><br> 
        Mirthconnect | Docker | Bootstrap | git | Joomla | WordPress <br>   
</div> 

---

{% for post in site.posts limit:1 %}
<article class="post-preview">
    <a href="{{ post.url | relative_url }}">
        <h5 class="post-title">{{ post.title }}</h5>
        {% if post.subtitle %}
        <h5 class="post-subtitle">
        {{ post.subtitle }}
        </h5>
        {% endif %}
    </a>
    <p class="post-meta">
        Posted on {{ post.date | date: "%B %-d, %Y" }}
    </p>
    <div class="post-entry-container">
        {% if post.image %}
        <div class="post-image">
        <a href="{{ post.url | relative_url }}">
            <img src="{{ post.image | relative_url }}">
        </a>
        </div>
        {% endif %}
        <div class="post-entry">
        {{ post.excerpt | strip_html | xml_escape | truncatewords: site.excerpt_length }}
        {% assign excerpt_word_count = post.excerpt | number_of_words %}
        {% if post.content != post.excerpt or excerpt_word_count > site.excerpt_length %}
            <a href="{{ post.url | relative_url }}" class="post-read-more">[Read&nbsp;More]</a>
        {% endif %}
        </div>
    </div>
    {% if post.tags.size > 0 %}
    <div class="blog-tags">
        Tags:
        {% if site.link-tags %}
        {% for tag in post.tags %}
        <a href="{{ '/tags' | relative_url }}#{{- tag -}}">{{- tag -}}</a>
        {% endfor %}
        {% else %}
        {{ post.tags | join: ", " }}
        {% endif %}
    </div>
    {% endif %}
</article>{% endfor %}