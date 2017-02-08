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
    "studies" :
      {
        "Bc." :
          {
            "start_year" : 2010,
            "semesters" :
              [
                {
                  "scholarship" :         0,
                  "place" :               [64,72,266],
                  "courses" :
                    [
                      {
                        "abbr": "IAS",    "name cs": "Asemblery",                             "name en": "Assembly Languages",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [17,20], "labs" : [20,20], "other" : [0,0],   "exam" : [36,60] }
                      },
                      {
                        "abbr": "IDA",    "name cs": "Diskrétní matematika",                  "name en": "Discrete Mathematics",
                        "credits" : 7,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [83,100],"exam" : [0,0]   }
                      },
                      {
                        "abbr": "ITO",    "name cs": "Teorie obvodů",                         "name en": "Circuit Theory",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[12.5,15]                 ],   "midterm" : [12,20], "labs" : [0,0],   "other" : [0,0],   "exam" : [34,65] }
                      },
                      {
                        "abbr": "IUS",    "name cs": "Úvod do softwarového inženýrství",      "name en": "Introduction to Software Engineering",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[5,5],[6,10],[20,20]      ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [0,0],   "exam" : [43,65] }
                      },
                      {
                        "abbr": "IZP",    "name cs": "Základy programování",                  "name en": "Introduction to Programming Systems",
                        "credits" : 7,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[2,5],[7,10],[9.5,10],[7,8]],  "midterm" : [7,12],  "labs" : [0,0],   "other" : [1,100], "exam" : [38,55] }
                      },
                    ],
                },
                {
                  "scholarship" :         7174,
                  "place" :               [25,25,184],
                  "courses" :
                    [
                      {
                        "abbr": "IFY",    "name cs": "Fyzika",                                "name en": "Physics",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [17,20], "labs" : [18,20], "other" : [0,0],   "exam" : [55,60] }
                      },
                      {
                        "abbr": "IMA",    "name cs": "Matematická analýza",                   "name en": "Mathematical Analysis",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [83,100],"exam" : [0,0]   }
                      },
                      {
                        "abbr": "INC",    "name cs": "Návrh číslicových systémů",             "name en": "Digital Systems Design",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[20,20]                   ],   "midterm" : [18,25], "labs" : [0,0],   "other" : [0,0],   "exam" : [49,55] }
                      },
                      {
                        "abbr": "IOS",    "name cs": "Operační systémy",                      "name en": "Operating Systems",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[5,15],[15,15]            ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [0,0],   "exam" : [51,70] }
                      },
                      {
                        "abbr": "IPR",    "name cs": "Prvky počítačů",                        "name en": "Computer Hardware",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],  "midterm" : [7.5,15], "labs" : [30,30], "other" : [0,0],   "exam" : [30,55] }
                      },
                      {
                        "abbr": "BAN4",   "name cs": "Angličtina 4: středně pokročilí 2",     "name en": "New Headway Intermediate 2",
                        "credits" : 6,    "type": "PVA",            "classified": True,
                        "pts":
                          { "projects" : [                          ],  "midterm" : [39,40],  "labs" : [0,0],   "other" : [0,0],   "exam" : [59,60] }
                      },
                      {
                        "abbr": "ITW",    "name cs": "Tvorba webových stránek",               "name en": "Web Design",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [[18,20],[29,30]           ],  "midterm" : [12,20],  "labs" : [10,10], "other" : [0,0],   "exam" : [17,20] }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [78,78,275],
                  "courses" :
                    [
                      {
                        "abbr": "IAL",    "name cs": "Algoritmy",                             "name en": "Algorithms",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[10,10],[9,10],[4.4,5],[9,10]],"midterm" : [14,14], "labs" : [0,0],   "other" : [1,100], "exam" : [28,51] }
                      },
                      {
                        "abbr": "IFJ",    "name cs": "Formální jazyky a překladače",          "name en": "Formal Languages and Compilers",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[19,20],[4.4,5]           ],   "midterm" : [16,20], "labs" : [0,0],   "other" : [0,0],   "exam" : [38.2,55]}
                      },
                      {
                        "abbr": "INM",    "name cs": "Numerická matematika a pravděpodobnost","name en": "Numerical Methods and Probability",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [79,100],"exam" : [0,0]   }
                      },
                      {
                        "abbr": "INP",    "name cs": "	Návrh počítačových systémů",          "name en": "Design of Computer Systems",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[12,12],[6,16]            ],   "midterm" : [20,20], "labs" : [0,0],   "other" : [0,0],   "exam" : [32,52] }
                      },
                      {
                        "abbr": "ISS",    "name cs": "Signály a systémy",                     "name en": "Signals and Systems",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[12,12]                   ],   "midterm" : [17.5,25],"labs" : [12,12],"other" : [0,0],   "exam" : [42.8,51]}
                      },
                      {
                        "abbr": "IPSO",   "name cs": "Pedagogická psychologie",               "name en": "Educational Psychology",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],   "labs" : [0,0],   "other" : [65,100],"exam" : [0,0]   }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [64,65,164],
                  "courses" :
                    [
                      {
                        "abbr": "IDS",    "name cs": "Databázové systémy",                    "name en": "Database Systems",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[5,5],[5,5],[5,5],[13,20]],    "midterm" : [12.5,14],"labs" : [0,0],   "other" : [0,0],   "exam" : [32.5,51]}
                      },
                      {
                        "abbr": "IPK",    "name cs": "Počítačové komunikace a sítě",          "name en": "Computer Communications and Networks",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[3.5,4],[6,6],[8,10]      ],   "midterm" : [5.4,9], "labs" : [6,6],    "other" : [0,0],   "exam" : [44,65] }
                      },
                      {
                        "abbr": "IPP",    "name cs": "Principy programovacích jazyků a OOP",  "name en": "Principles of Programming Languages",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[8.6,10],[3.9,10]         ],   "midterm" : [18,20], "labs" : [0,0],    "other" : [0,0],   "exam" : [26,60] }
                      },
                      {
                        "abbr": "IZG",    "name cs": "Základy počítačové grafiky",            "name en": "Computer Graphics Principles",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[6,18]                    ],   "midterm" : [9,12],  "labs" : [18,18],  "other" : [0,0],   "exam" : [50,52] }
                      },
                      {
                        "abbr": "IZU",    "name cs": "Základy umělé inteligence",             "name en": "Fundamentals of Artificial Intelligence",
                        "credits" : 4,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [8,20],  "labs" : [17.75,20],"other" : [0,0],  "exam" : [51,60] }
                      },
                      {
                        "abbr": "IJA",    "name cs": "Seminář Java",                          "name en": "Java Programming Language",
                        "credits" : 4,    "type": "PVT",            "classified": False,
                        "pts":
                          { "projects" : [[20,20],[64,80]           ],   "midterm" : [0,0],   "labs" : [0,0],    "other" : [0,0],   "exam" : [0,0]   }
                      },
                      {
                        "abbr": "PRM",    "name cs": "Právní minimum",                        "name en": "Fundamentals of Law",
                        "credits" : 3,    "type": "PVH",            "classified": False,
                        "pts":
                          { "projects" : [                          ],   "midterm" : [0,0],   "labs" : [0,0],    "other" : [0,0],   "exam" : [0,0]   }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [96,98,240],
                  "courses" :
                    [
                      {
                        "abbr": "IIS",    "name cs": "Informační systémy",                    "name en": "Information Systems",
                        "credits" : 4,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[30,30]                   ],    "midterm" : [15,19],"labs" : [0,0],   "other" : [0,0],   "exam" : [24,51]}
                      },
                      {
                        "abbr": "IMP",    "name cs": "Mikroprocesorové a vestavěné systémy",  "name en": "Microprocessors and Embedded Systems",
                        "credits" : 6,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[14.6,19]                 ],    "midterm" : [14,14],"labs" : [16,16], "other" : [0,0],   "exam" : [23.3,51]}
                      },
                      {
                        "abbr": "IMS",    "name cs": "Modelování a simulace",                 "name en": "Modelling and Simulation",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[20,20]                   ],    "midterm" : [8,10], "labs" : [0,0],   "other" : [0,0],   "exam" : [44,70] }
                      },
                      {
                        "abbr": "IPZ",    "name cs": "Periferní zařízení",                    "name en": "Peripheral Devices",
                        "credits" : 4,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                          ],    "midterm" : [26,30],"labs" : [3.8,4], "other" : [0,0],   "exam" : [63.3,66]}
                      },
                      {
                        "abbr": "ISA",    "name cs": "Síťové aplikace a správa sítí",         "name en": "Network Applications and Network Administration",
                        "credits" : 5,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[16,21]                   ],    "midterm" : [0,0],  "labs" : [16,24], "other" : [0,0],   "exam" : [33,55] }
                      },
                      {
                        "abbr": "ISP",    "name cs": "Semestrální projekt",                    "name en": "Term Project",
                        "credits" : 2,    "type": "P",              "classified": False,
                        "pts":
                          { "projects" : [                          ],    "midterm" : [0,0],  "labs" : [0,0],   "other" : [100,100],"exam" : [0,0]  }
                      },
                      {
                        "abbr": "ITU",    "name cs": "Tvorba uživatelských rozhraní",         "name en": "User Interface Programming",
                        "credits" : 4,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[43,55]                   ],    "midterm" : [18,20],"labs" : [24,25], "other" : [0,0],   "exam" : [0,0]   }
                      },
                      {
                        "abbr": "JS1",    "name cs": "Španělština: začátečníci 1/2",          "name en": "Spanish for Beginners 1/2",
                        "credits" : 3,    "type": "V",              "classified": False,
                        "pts":
                          { "projects" : [                          ],    "midterm" : [0,0],  "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [59,84,369],
                  "courses" :
                    [
                      {
                        "abbr": "ITY",    "name cs": "Typografie a publikování",              "name en": "Typography and Publishing",
                        "credits" : 4,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [[6,10],[12,15],[13,15],[10,15],[15,15]],"midterm" : [0,0],"labs" : [0,0],"other" : [0,0],"exam" : [30,30]}
                      },
                      {
                        "abbr": "JS1",    "name cs": "Španělština: začátečníci 2/2",          "name en": "Spanish for Beginners 2/2",
                        "credits" : 3,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [                         ],    "midterm" : [0,0],   "labs" : [0,0],   "other" : [85,100],"exam" : [0,0]  }
                      },
                    ],
                },
                
                {
                  "scholarship" :         0,
                  "place" :               [125,138,160],
                  "courses" :
                    [
                      {
                        "abbr": "IPA",    "name cs": "Pokročilé asemblery",                   "name en": "Advanced Assembly Languages",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                          { "projects" : [[20,26]                  ],    "midterm" : [0,0],   "labs" : [14,14],  "other" : [0,0],"exam" : [23,60]}
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [59,84,369],
                  "courses" :
                    [
                      {
                        "abbr": "IBP",    "name cs": "Bakalářská práce",                      "name en": "Bachelor's Thesis",
                        "credits" : 9,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [[95,100]                 ],   "midterm" : [0,0],"labs" : [0,0],"other" : [0,0],"exam" : [0,0]}
                      },
                      {
                        "abbr": "ISZ",    "name cs": "Státní závěrečná zkouška",              "name en": "Final State Examination",
                        "credits" : 9,    "type": "P",              "classified": True,
                        "pts":
                          { "projects" : [                         ],   "midterm" : [0,0],"labs" : [0,0],"other" : [85,100],"exam" : [0,0]}
                      },
                    ],
                },
              ]
          },
      
        "Ing." :
          {
            "start_year" : 2014,
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
                           { "projects" : [[60,60]                  ],   "midterm" : [30,40],   "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [110,115,198],
                  "courses" :
                    [
                      {
                        "abbr": "ARC",    "name cs": "Architektura a programování paralelních systémů", "name en": "Parallel System Architecture and Programming",
                        "credits" : 5,    "type": "PVC",             "classified": True,
                        "pts":
                          { "projects" : [[10,15],[3,15]             ],   "midterm" : [7,10],    "labs" : [0,0],   "other" : [0,0],   "exam" : [38,60] }
                      },
                      {
                        "abbr": "VNV",    "name cs": "Vysoce náročné výpočty",                   "name en": "High Performance Computations",
                        "credits" : 5,    "type": "PVM",             "classified": True,
                        "pts":
                           { "projects" : [                          ],   "midterm" : [18,20],   "labs" : [19,20], "other" : [0,0],   "exam" : [36,60] }
                      },
                      {
                        "abbr": "VIZ",    "name cs": "Vizualizace a CAD",                        "name en": "Visualization and CAD",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                           { "projects" : [[60,60]                   ],   "midterm" : [28,40],   "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [13,19,88],
                  "courses" :
                    [
                      {
                        "abbr": "SEP",    "name cs": "Semestrální projekt",                      "name en": "Term Project",
                        "credits" : 5,    "type": "P",               "classified": True,
                        "pts":
                          { "projects" : [[90,100]                   ],   "midterm" : [0,0],     "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                      {
                        "abbr": "GUX",    "name cs": "Grafická uživatelská rozhraní v X Window", "name en": "Graphical User Interfaces in X Window System",
                        "credits" : 5,    "type": "V",               "classified": True,
                        "pts":
                           { "projects" : [[7,8],[9,12]              ],   "midterm" : [14,20],   "labs" : [0,0],   "other" : [0,0],   "exam" : [35,60] }
                      },
                      {
                        "abbr": "POV",    "name cs": "Počítačové vidění",                        "name en": "Computer Vision",
                        "credits" : 5,    "type": "V",              "classified": True,
                        "pts":
                           { "projects" : [[8.1,10],[27,30]          ],   "midterm" : [9,9],     "labs" : [0,0],   "other" : [0,0],   "exam" : [46,51] }
                      },
                    ],
                },
                {
                  "scholarship" :         0,
                  "place" :               [0,0,0],
                  "courses" :
                    [
                      {
                        "abbr": "SIP",    "name cs": "Diplomová práce",                          "name en": "Master's Thesis",
                        "credits" : 13,   "type": "P",               "classified": True,
                        "pts":
                          { "projects" : [[0,0]                      ],   "midterm" : [0,0],     "labs" : [0,0],   "other" : [0,0],   "exam" : [0,0]   }
                      },
                      {
                        "abbr": "SZZ",    "name cs": "Státní závěrečná zkouška",                 "name en": "Final state examination",
                        "credits" : 0,    "type": "P",               "classified": True,
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


<table class="study-table">

{% set semester_type_cycler = cycler("Z","L") %}
{% for study_type in study_data.studies %}
  {% set calendar_year_cycler = cycler(*range(study_data.studies[study_type].start_year,100000)) %}

  {% for semester in study_data.studies[study_type].semesters %}
    {% set number_of_courses = semester.courses|length %}
  
    {% set semester_number = loop.index %}
  
    {% if loop.last %}
      {% set next_2_semester_courses = number_of_courses %}
    {% else %}
      {% set next_2_semester_courses = number_of_courses + ((study_data.studies[study_type].semesters[loop.index].courses)|length) %}
    {% endif %}
  
    {% set current_school_year = loop.index // 2 + 1 %}
    
    {% for course in semester.courses %}

      <tr>
        {% if loop.first %}                                                     {# new semester #}
          <td rowspan="{{ number_of_courses }}"> {{ semester_type_cycler.next() }} </td>
          
          
          {% if semester_number == 1 or semester_type_cycler.current == "Z" %}                        {# new calendar year #}
            <td rowspan="{% if semester_number == 1 %} {{ number_of_courses }} {% else %} {{ next_2_semester_courses }} {% endif %}"> {{ calendar_year_cycler.next() }} </td>
          {% endif %}
          
          {% if semester_type_cycler.current == "L" %}                          {# new school year #}
            <td rowspan="{{ next_2_semester_courses }}"> {{ current_school_year }} </td>
          {% endif %}
            
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

TODO: statistiky ohledně studia spočítané z tabulky