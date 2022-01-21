---
layout: default
title: Editorial
image: "none"
---

<table class="table">
    <thead>
        <td> <strong> year </strong> </td>
        <td> <strong> type </strong> </td>
        <td> <strong> edition </strong> </td>
        <td> <strong> name </strong> </td>
        <td> <strong> role </strong> </td>
        <td> <strong> editor </strong> </td>
        <td> <strong> deadline </strong> </td>
        <td> <strong> cfp </strong> </td>
    </thead>
    <tbody>
        {% for eds in site.data.editions.editor %}
                <tr><td>{{ eds.year }}</td><td>{{ eds.type }}</td><td>{{ eds.edition }}</td><td>{{ eds.name }}</td><td>{{ eds.role }}</td><td>{{ eds.editor }}</td><td>{{ eds.deadline }}</td><td><a href="{{ eds.url }}" target="_blank"><i class="fa fa-external-link" aria-hidden="true"></i></a></td></tr>
        {% endfor %}
    </tbody>
</table>