---
layout: default
title: Committees
image: "none"
---

<table class="table">
    <thead>
        <td> <strong> year </strong> </td>
        <td> <strong> name </strong> </td>
        <td> <strong> role </strong> </td>
        <td> <strong> type </strong> </td>
        <td> <strong> local </strong> </td>
    </thead>
    <tbody>
        {% for com in site.data.committees.committees %}
                <tr><td>{{ com.year }}</td><td>{{ com.name }}</td><td>{{ com.role }}</td><td>{{ com.type }}</td><td>{{ com.local }}</td></tr>
        {% endfor %}
    </tbody>
</table>