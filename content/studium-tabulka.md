Title: Studium na FIT VUT - tabulka
Date: 2016-04-26 21:23
Author: tastyfish
Category: Articles
Status: published
Tags: study

{% import "macros.html" as m %}

{%
set study_data =
  {
    "start_year" : 2010,
    
    "studies" :
      {
        "Ing." :
          {
            "semesters" :
              [
                {
                  "scholarship" :         9913,
                  "place" :               [10,10,110],
                  "courses" :
                    [
                      {
                        "abbr": "HSC",    "name cs": "Hardware/Software Codesign",              "name en": "Hardware/Software Codesign",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[5,25]                    ],   "midterm" : [16,20],   "labs" : [0,0],   "other" : [0,0],   "exam" : [45,55] }
                      },
                      {
                        "abbr": "MAT",    "name cs": "Matematické struktury v informatice",     "name en": "Mathematical Structures in Computer Science",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [14,20],   "labs" : [0,0],   "other" : [0,0],   "exam" : [68,80] }
                      },
                      {
                        "abbr": "PDB",    "name cs": "Pokročilé databázové systémy",            "name en": "Advanced Database Systems",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[17,20]                   ],   "midterm" : [14,20],   "labs" : [0,0],   "other" : [0,0],   "exam" : [39,60] }
                      },
                      {
                        "abbr": "PGR",    "name cs": "Počítačová grafika",                      "name en": "Computer Graphics",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[30,30]                   ],   "midterm" : [7,7],     "labs" : [12,12], "other" : [0,0],   "exam" : [41,51] }
                      },
                      {
                        "abbr": "TIN",    "name cs": "Teoretická informatika",                  "name en": "Theoretical Computer Science",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[5,5],[4,5],[4.2,5],[5,5] ],   "midterm" : [19,20],   "labs" : [0,0],   "other" : [0,0],   "exam" : [49,60] }
                      },
                      {
                        "abbr": "FIT",    "name cs": "Dějiny a filozofie techniky",             "name en": "History and Philosophy of Technology",
                        "credits" : 3,    "type": "PVH",            "classified": False,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],     "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                      {
                        "abbr": "PGP",    "name cs": "Pokročilá počítačová grafika",            "name en": "Advanced Computer Graphics",
                        "credits" : 5,    "type": "PVG",            "classified": True,
                        "pts":
                          { "projects" : [[10,10],[30,30]           ],   "midterm" : [7,9],     "labs" : [0,0],   "other" : [0,0],   "exam" : [43,51] }
                      },
                      {
                        "abbr": "STI",    "name cs": "Seminář teoretické informatiky",          "name en": "Theoretical Computer Science Seminar",
                        "credits" : 2,    "type": "V",              "classified": False,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],     "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                    ],
                },
              ],
          },
      },
  }
%}

{% macro write_points(points_tuple) %}
{% if points_tuple[1] > 0 %}
{{ points_tuple[0] }}/{{ points_tuple[1] }}
{% endif %}
{% endmacro %}

{% macro course_total_points(course_obj) -%}
{%+ set projects_total = course_obj.pts.projects|map(attribute="0")|sum %}
{{ projects_total + course_obj.pts.midterm[0] + course_obj.pts.labs[0] + course_obj.pts.other[0] + course_obj.pts.exam[0]}}
{%- endmacro %}

{% macro semester_total_credits(semester_obj) -%}
{{ semester_obj.courses|map(attribute="credits")|sum }}
{%- endmacro %}

{% macro course_mark(total_points) %}
{% if total_points|int >= 90 %}A{% else %}
{% if total_points|int >= 80 %}B{% else %}
{% if total_points|int >= 70 %}C{% else %}
{% if total_points|int >= 60 %}D{% else %}
{% if total_points|int >= 50 %}E{% else %}F{% endif %}{% endif %}{% endif %}{% endif %}{% endif %}
{% endmacro %}

{% macro course_mark_to_number(mark) %}
{% if mark == "A" %}1{% else %}
{% if mark == "B" %}1.5{% else %}
{% if mark == "C" %}2{% else %}
{% if mark == "D" %}2.5{% else %}
{% if mark == "E" %}3{% else %}3.5{% endif %}{% endif %}{% endif %}{% endif %}{% endif %}
{% endmacro %}


{% macro semester_weighted_mean(semester_obj) -%}
5
{%- endmacro %}

<table>

{% set semester_type_cycler = cycler("Z","L") %}
{% for study_type in study_data.studies %}

  {% for semester in study_data.studies[study_type].semesters %}

    {% set number_of_courses = semester.courses|length %}
  
    {% for course in semester.courses %}

      <tr>
  
        {% if loop.first %}
          <td rowspan="{{ number_of_courses }}"> {{ semester_type_cycler.next() }} </td>
        {% endif %}
  
        <td> {{ course.abbr }} </td>
        <td> {{ course["name cs"] }} </td>
        <td> {{ course.credits }} </td>
        <td> {{ course.type }} </td>
       
        <td> {{ write_points(course.pts.midterm) }} </td>

        <td>
       
        {% for project_points in course.pts.projects %}
          {{ write_points(project_points) }}
        {% endfor %}
       
        </td>

        <td> {{ write_points(course.pts.labs) }} </td>
        <td> {{ write_points(course.pts.other) }} </td>
        <td> {{ write_points(course.pts.exam) }} </td>

        <td>
          {% if course.classified %}
            {% set points_total = course_total_points(course) %}
            {{ points_total }}&nbsp;{{ course_mark(points_total) }}
          {% else %}
            ✓
          {% endif %}
        </td>
       
        {% if loop.first %}
          <td rowspan="{{ number_of_courses }}"> {{ semester_total_credits(semester) }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ semester_weighted_mean(semester) }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ semester.place[0] }}-{{ semester.place[1] }}/{{ semester.place[2] }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ semester.scholarship }} </td>
        {% endif %}
       
      </tr>

    {% endfor %}
  {% endfor %}
{% endfor %}

</table>