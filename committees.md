---
layout: default
title: Committees
image: "none"
---

<style>
.com-outer {
  width: 100vw;
  position: relative;
  left: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 0 17rem;
  box-sizing: border-box;
}
.com-filters {
  display: flex; gap: 8px; flex-wrap: wrap;
  align-items: center; margin-bottom: 1.25rem;
  padding-bottom: 1rem; border-bottom: 1px solid #e5e7eb;
}
.com-filters select {
  font-family: inherit; font-size: inherit;
  padding: 4px 24px 4px 8px;
  border: 1px solid #d1d5db; border-radius: 6px;
  background: #fff; color: inherit; cursor: pointer;
  appearance: none; -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23888'/%3E%3C/svg%3E");
  background-repeat: no-repeat; background-position: right 7px center;
}
.com-filters select:focus { outline: none; border-color: #6b7280; }
.com-cnt { color: #9ca3af; margin-left: auto; }

.com-year-section { margin-bottom: 2rem; }
.com-year-heading {
  font-size: 0.75em; font-weight: 600; color: #9ca3af;
  letter-spacing: 0.06em; text-transform: uppercase;
  margin-bottom: 0.5rem;
}
table.com-table { width: 100%; border-collapse: collapse; }
table.com-table thead th {
  font-size: 0.8em; font-weight: 600; color: #9ca3af;
  text-align: left; padding: 6px 12px;
  border-bottom: 1px solid #e5e7eb; white-space: nowrap;
}
table.com-table tbody tr { border-bottom: 1px solid #f3f4f6; }
table.com-table tbody tr:last-child { border-bottom: none; }
table.com-table tbody tr:hover td { background: #f9fafb; }
table.com-table td { padding: 10px 12px; vertical-align: top; }

.com-col-nick   { width: 12%; white-space: nowrap; }
.com-col-name   { width: 48%; }
.com-col-role   { width: 20%; }
.com-col-local  { width: 15%; }
.com-col-link   { width: 5%; text-align: center; }

.com-nick-text  { font-weight: 600; color: #111827; }
.com-name-text  { line-height: 1.4; color: #111827; }
.com-pub-text   { font-size: 0.85em; color: #9ca3af; margin-top: 2px; }
.com-role-text  { color: #6b7280; }
.com-local-text { font-size: 0.9em; color: #9ca3af; }

.com-badge {
  display: inline-block; font-size: 0.7em; font-weight: 600;
  padding: 1px 7px; border-radius: 20px;
  white-space: nowrap; margin-left: 6px; vertical-align: middle;
}
.com-b-conf { background: #eff6ff; color: #1d4ed8; }
.com-b-jour { background: #f0fdf4; color: #15803d; }

.com-repo-link { color: #9ca3af; text-decoration: none; font-size: 1.1em; }
.com-repo-link:hover { color: #111827; }

@media (max-width: 640px) {
  .com-outer { padding: 0 1rem; }
  .com-col-role, .com-col-local { display: none; }
  .com-col-nick { width: 20%; }
  .com-col-name { width: 72%; }
  .com-col-link { width: 8%; }
}
</style>

<div class="com-outer">
  <div class="com-filters">
    <select id="com-fT">
      <option value="">All types</option>
      <option value="Conference">Conference</option>
      <option value="Journal">Journal</option>
    </select>
    <select id="com-fR">
      <option value="">All roles</option>
      {% assign roles = site.data.committees.committees | map: "role" | uniq | sort %}
      {% for r in roles %}<option value="{{ r }}">{{ r }}</option>{% endfor %}
    </select>
    <span class="com-cnt" id="com-cnt"></span>
  </div>

  {% assign all_years = site.data.committees.committees | map: "year" | uniq | sort | reverse %}
  {% for yr in all_years %}
  {% assign yr_items = site.data.committees.committees | where: "year", yr %}
  <div class="com-year-section" data-year="{{ yr }}">
    <div class="com-year-heading">{{ yr }}</div>
    <table class="com-table">
      <thead>
        <tr>
          <th class="com-col-nick">Acronym</th>
          <th class="com-col-name">Name</th>
          <th class="com-col-role">Role</th>
          <th class="com-col-local">Location</th>
        </tr>
      </thead>
      <tbody>
        {% for com in yr_items %}
        <tr data-type="{{ com.type }}" data-role="{{ com.role }}">
          <td class="com-col-nick"><span class="com-nick-text">{% if com.nick and com.nick != "" %}{{ com.nick }}{% else %}—{% endif %}</span></td>
          <td class="com-col-name">
            <span class="com-name-text">{{ com.name }} {% if com.publisher and com.publisher != "" %}<span class="com-pub-text"> - {{ com.publisher }} </span>{% endif %}</span>
            <span class="com-badge {% if com.type == 'Journal' %}com-b-jour{% else %}com-b-conf{% endif %}">{{ com.type }} </span>
           
          </td>
          <td class="com-col-role"><span class="com-role-text">{{ com.role }}</span></td>
          <td class="com-col-local"><span class="com-local-text">{% if com.local and com.local != "" %}{{ com.local }}{% else %}—{% endif %}</span></td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  {% endfor %}
</div>

<script>
(function(){
  var fT=document.getElementById('com-fT'),
      fR=document.getElementById('com-fR'),
      cnt=document.getElementById('com-cnt'),
      rows=Array.from(document.querySelectorAll('.com-table tbody tr')),
      sections=Array.from(document.querySelectorAll('.com-year-section'));

  function filter(){
    var t=fT.value, r=fR.value, total=0;
    rows.forEach(function(row){
      var show=(!t||row.dataset.type===t)&&(!r||row.dataset.role===r);
      row.style.display=show?'':'none';
      if(show) total++;
    });
    sections.forEach(function(sec){
      var visible=sec.querySelectorAll('tbody tr:not([style*="display: none"])').length;
      sec.style.display=visible?'':'none';
    });
    cnt.textContent=total+' entries';
  }

  fT.onchange=fR.onchange=filter;
  filter();
})();
</script>