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
                {
                  "scholarship" :         0,
                  "place" :               [20,22,127],
                  "courses" :
                    [
                      {
                        "abbr": "FYO",    "name cs": "Fyzikální optika",                        "name en": "Physical Optics",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[21,30]                   ],   "midterm" : [8,10],    "labs" : [0,0],   "other" : [0,0],   "exam" : [29,60] }
                      },
                      {
                        "abbr": "MUL",    "name cs": "Multimédia",                              "name en": "Multimedia",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[23,24]                   ],   "midterm" : [8,10],    "labs" : [15,15], "other" : [0,0],   "exam" : [46,51] }
                      },
                      {
                        "abbr": "PDS",    "name cs": "Přenos dat, počítačové sítě a protokoly", "name en": "Data Communications, Computer Networks and Protocols",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[9,25]                    ],   "midterm" : [9,15],    "labs" : [0,0],   "other" : [0,0],   "exam" : [36,60] }
                      },
                      {
                        "abbr": "ZPO",    "name cs": "Zpracování obrazu",                       "name en": "Image Processing",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[24,29]                   ],   "midterm" : [10,10],   "labs" : [10,10], "other" : [0,0],   "exam" : [42,51] }
                      },
                      {
                        "abbr": "ZRE",    "name cs": "Zpracování řečových signálů",             "name en": "Speech Signal Processing",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[14,15],[14,14]           ],   "midterm" : [10.5,14], "labs" : [6,6],   "other" : [0,0],   "exam" : [40.8,51] }
                      },
                      {
                        "abbr": "WAP",    "name cs": "Internetové aplikace",                    "name en": "Internet Applications",
                        "credits" : 5,    "type": "PVI",            "classified": True,
                        "pts":
                          { "projects" : [[30,30]                   ],   "midterm" : [16,19],   "labs" : [0,0],   "other" : [0,0],   "exam" : [48,51] }
                      },
                      {
                        "abbr": "VIN",    "name cs": "Výtvarná informatika",                    "name en": "Computer Art",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [[49,49],[51,51]           ],   "midterm" : [0,0],     "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0] }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [10,10,198],
                  "courses" :
                    [
                      {
                        "abbr": "GZN",    "name cs": "Grafická a zvuková rozhraní a normy",     "name en": "Graphical and Sound Interfaces and Standards",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[39,40]                   ],   "midterm" : [8,9],     "labs" : [0,0],   "other" : [0,0],   "exam" : [38,51] }
                      },
                      {
                        "abbr": "KRG",    "name cs": "Kreativní grafika",                       "name en": "Creative Art",
                        "credits" : 4,    "type": "V",              "classified": True,
                        "pts":
                           { "projects" : [[60,60]                   ],   "midterm" : [30,40],   "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
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

{% macro course_mark(course_obj) %}
{% set total_points = course_total_points(course_obj)%}
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

{% macro weighted_mean_numerator(courses) %}
{% if courses|length > 0 %}
  {{ courses[0].credits|float * course_mark_to_number(course_mark(courses[0]))|float + (weighted_mean_numerator(courses[1:])|float) }}
{% else %}
  0
{% endif %}
{% endmacro %}

{% macro courses_weighted_mean(courses) -%}
{% set valid_courses = (courses|groupby("classified"))[-1][1] %} {# reject/select filters don't work somehow #}
{% set valid_credits = valid_courses|sum(attribute="credits") %}
{{ (weighted_mean_numerator(valid_courses)|float / valid_credits|float)|string|truncate(5,true,"") }}
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
            {{ points_total }}&nbsp;{{ course_mark(course) }}
          {% else %}
            ✓
          {% endif %}
        </td>
       
        {% if loop.first %}
          <td rowspan="{{ number_of_courses }}"> {{ semester_total_credits(semester) }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ courses_weighted_mean(semester.courses) }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ semester.place[0] }}-{{ semester.place[1] }}/{{ semester.place[2] }} </td>
          <td rowspan="{{ number_of_courses }}"> {{ semester.scholarship }} </td>
        {% endif %}
       
      </tr>

    {% endfor %}
  {% endfor %}
{% endfor %}

</table>