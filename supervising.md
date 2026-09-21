---
layout: default
title: Supervisions
image: "none"
---

<style>
.sup-outer {
  width: 100vw;
  position: relative;
  left: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  padding: 0 17rem;
  box-sizing: border-box;
}
.sup-filters {
  display: flex; gap: 8px; flex-wrap: wrap;
  align-items: center; margin-bottom: 1.25rem;
  padding-bottom: 1rem; border-bottom: 1px solid #e5e7eb;
}
.sup-filters select {
  font-family: inherit; font-size: inherit;
  padding: 4px 24px 4px 8px;
  border: 1px solid #d1d5db; border-radius: 6px;
  background: #fff; color: inherit; cursor: pointer;
  appearance: none; -webkit-appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6' viewBox='0 0 10 6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%23888'/%3E%3C/svg%3E");
  background-repeat: no-repeat; background-position: right 7px center;
}
.sup-filters select:focus { outline: none; border-color: #6b7280; }
.sup-cnt { color: #9ca3af; margin-left: auto; }

.sup-year-section { margin-bottom: 2rem; }
.sup-year-heading {
  font-size: 0.75em; font-weight: 600; color: #9ca3af;
  letter-spacing: 0.06em; text-transform: uppercase;
  margin-bottom: 0.5rem;
}
table.sup-table { width: 100%; border-collapse: collapse; }
table.sup-table thead th {
  font-size: 0.8em; font-weight: 600; color: #9ca3af;
  text-align: left; padding: 6px 12px;
  border-bottom: 1px solid #e5e7eb; white-space: nowrap;
}
table.sup-table tbody tr { border-bottom: 1px solid #f3f4f6; }
table.sup-table tbody tr:last-child { border-bottom: none; }
table.sup-table tbody tr:hover td { background: #f9fafb; }
table.sup-table td { padding: 10px 12px; vertical-align: top; }

.sup-col-title   { width: 40%; }
.sup-col-student { width: 15%; }
.sup-col-course  { width: 25%; }
.sup-col-grade   { width: 7%; text-align: center; }
.sup-col-date    { width: 8%; white-space: nowrap; }
.sup-col-link    { width: 5%; text-align: center; }

.sup-title-text { font-weight: 600; line-height: 1.4; color: #111827; }
.sup-student-text { color: #6b7280; }
.sup-course-text { font-size: 0.9em; color: #9ca3af; }
.sup-grade-text { font-weight: 600; text-align: center; color: #111827; }
.sup-date-text { font-size: 0.9em; color: #9ca3af; white-space: nowrap; }

.sup-badge {
  display: inline-block; font-size: 0.7em; font-weight: 600;
  padding: 1px 7px; border-radius: 20px;
  white-space: nowrap; margin-left: 6px; vertical-align: middle;
}
.sup-b-msc     { background: #eff6ff; color: #1d4ed8; }
.sup-b-phd     { background: #ede9fe; color: #5b21b6; }
.sup-b-closed  { background: #f0fdf4; color: #15803d; }
.sup-b-ongoing { background: #fff7ed; color: #c2410c; }
.sup-b-delayed { background: #fef2f2; color: #b91c1c; }

.sup-repo-link { color: #9ca3af; text-decoration: none; font-size: 1.1em; }
.sup-repo-link:hover { color: #111827; }

@media (max-width: 640px) {
  .sup-outer { padding: 0 1rem; }
  .sup-col-course, .sup-col-date { display: none; }
  .sup-col-title   { width: 55%; }
  .sup-col-student { width: 25%; }
  .sup-col-grade   { width: 12%; }
  .sup-col-link    { width: 8%; }
}
</style>

<div class="sup-outer">
  <div class="sup-filters">
    <select id="sup-fDeg">
      <option value="">All degrees</option>
      <option value="Msc">MSc</option>
      <option value="PhD">PhD</option>
    </select>
    <select id="sup-fSt">
      <option value="">All statuses</option>
      <option value="Closed">Closed</option>
      <option value="Undergoing">Undergoing</option>
      <option value="Delayed">Delayed</option>
    </select>
    <select id="sup-fCourse">
      <option value="">All courses</option>
      {% assign courses = site.data.supervisions.supervisions | map: "course" | uniq | sort %}
      {% for c in courses %}<option value="{{ c }}">{{ c }}</option>{% endfor %}
    </select>
    <span class="sup-cnt" id="sup-cnt"></span>
  </div>

  {% assign ongoing = site.data.supervisions.supervisions | where: "status", "Undergoing" %}
  {% assign delayed = site.data.supervisions.supervisions | where: "status", "Delayed" %}
  {% assign ongoing_size = ongoing | size %}
  {% assign delayed_size = delayed | size %}

  {% if ongoing_size > 0 or delayed_size > 0 %}
  <div class="sup-year-section" data-year="inprogress">
    <div class="sup-year-heading">In progress</div>
    <table class="sup-table">
      <thead>
        <tr>
          <th class="sup-col-title">Title</th>
          <th class="sup-col-student">Student</th>
          <th class="sup-col-course">Course</th>
          <th class="sup-col-grade">Grade</th>
          <th class="sup-col-date">Date</th>
          <th class="sup-col-link">Repo</th>
        </tr>
      </thead>
      <tbody>
        {% for sup in ongoing %}
        <tr data-degree="{{ sup.degree }}" data-status="{{ sup.status }}" data-course="{{ sup.course }}">
          <td class="sup-col-title">
            <span class="sup-title-text">{{ sup.title }}</span>
            <span class="sup-badge {% if sup.degree == 'PhD' %}sup-b-phd{% else %}sup-b-msc{% endif %}">{{ sup.degree }}</span>
            <span class="sup-badge sup-b-ongoing">Ongoing</span>
          </td>
          <td class="sup-col-student"><span class="sup-student-text">{{ sup.student }}</span></td>
          <td class="sup-col-course"><span class="sup-course-text">{{ sup.course }}</span></td>
          <td class="sup-col-grade"><span class="sup-grade-text">{% if sup.grade %}{{ sup.grade }}/20{% else %}—{% endif %}</span></td>
          <td class="sup-col-date"><span class="sup-date-text">—</span></td>
          <td class="sup-col-link">{% if sup.url and sup.url != "" %}<a class="sup-repo-link" href="{{ sup.url }}" target="_blank">↗</a>{% endif %}</td>
        </tr>
        {% endfor %}
        {% for sup in delayed %}
        <tr data-degree="{{ sup.degree }}" data-status="{{ sup.status }}" data-course="{{ sup.course }}">
          <td class="sup-col-title">
            <span class="sup-title-text">{{ sup.title }}</span>
            <span class="sup-badge {% if sup.degree == 'PhD' %}sup-b-phd{% else %}sup-b-msc{% endif %}">{{ sup.degree }}</span>
            <span class="sup-badge sup-b-delayed">Delayed</span>
          </td>
          <td class="sup-col-student"><span class="sup-student-text">{{ sup.student }}</span></td>
          <td class="sup-col-course"><span class="sup-course-text">{{ sup.course }}</span></td>
          <td class="sup-col-grade"><span class="sup-grade-text">{% if sup.grade %}{{ sup.grade }}/20{% else %}—{% endif %}</span></td>
          <td class="sup-col-date"><span class="sup-date-text">—</span></td>
          <td class="sup-col-link">{% if sup.url and sup.url != "" %}<a class="sup-repo-link" href="{{ sup.url }}" target="_blank">↗</a>{% endif %}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  {% endif %}

  {% assign all_years = site.data.supervisions.supervisions | where: "status", "Closed" | map: "year" | uniq | sort | reverse %}
  {% for yr in all_years %}
  {% assign yr_items = site.data.supervisions.supervisions | where: "year", yr | where: "status", "Closed" %}
  <div class="sup-year-section" data-year="{{ yr }}">
    <div class="sup-year-heading">Closed</div>
    <table class="sup-table">
      <thead>
        <tr>
          <th class="sup-col-title">Title</th>
          <th class="sup-col-student">Student</th>
          <th class="sup-col-course">Course</th>
          <th class="sup-col-grade">Grade</th>
          <th class="sup-col-date">Date</th>
          <th class="sup-col-link">Repo</th>
        </tr>
      </thead>
      <tbody>
        {% for sup in yr_items %}
        <tr data-degree="{{ sup.degree }}" data-status="{{ sup.status }}" data-course="{{ sup.course }}">
          <td class="sup-col-title">
            <span class="sup-title-text">{{ sup.title }}</span>
            <span class="sup-badge {% if sup.degree == 'PhD' %}sup-b-phd{% else %}sup-b-msc{% endif %}">{{ sup.degree }}</span>
            <span class="sup-badge sup-b-closed">Closed</span>
          </td>
          <td class="sup-col-student"><span class="sup-student-text">{{ sup.student }}</span></td>
          <td class="sup-col-course"><span class="sup-course-text">{{ sup.course }}</span></td>
          <td class="sup-col-grade"><span class="sup-grade-text">{% if sup.grade %}{{ sup.grade }}/20{% else %}—{% endif %}</span></td>
          <td class="sup-col-date"><span class="sup-date-text">{{ sup.date | default: "—" }}</span></td>
          <td class="sup-col-link">{% if sup.url and sup.url != "" %}<a class="sup-repo-link" href="{{ sup.url }}" target="_blank">↗</a>{% endif %}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
  {% endfor %}
</div>

<script>
(function(){
  var fDeg=document.getElementById('sup-fDeg'),
      fSt=document.getElementById('sup-fSt'),
      fCourse=document.getElementById('sup-fCourse'),
      cnt=document.getElementById('sup-cnt'),
      rows=Array.from(document.querySelectorAll('.sup-table tbody tr')),
      sections=Array.from(document.querySelectorAll('.sup-year-section'));

  function filter(){
    var d=fDeg.value, s=fSt.value, c=fCourse.value, total=0;
    rows.forEach(function(row){
      var show=(!d||row.dataset.degree===d)&&(!s||row.dataset.status===s)&&(!c||row.dataset.course===c);
      row.style.display=show?'':'none';
      if(show) total++;
    });
    sections.forEach(function(sec){
      var visible=sec.querySelectorAll('tbody tr:not([style*="display: none"])').length;
      sec.style.display=visible?'':'none';
    });
    cnt.textContent=total+' supervisions';
  }

  fDeg.onchange=fSt.onchange=fCourse.onchange=filter;
  filter();
})();
</script>