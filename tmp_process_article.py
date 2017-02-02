import sys
import re

lines = ""

header_added = False

for line in sys.stdin:
  if not header_added and len(line.lstrip().rstrip()) == 0:
    line = "\n{% import 'macros.html' as m %}\n\n"
    header_added = True
  
  lines += line
    
lines = re.sub('\\\\\[:cs\\\]','',lines)
lines = re.sub('\\\\\[:\\\]','',lines)


lines = re.sub('\\\\\[caption[^!]*!\[([^ ]*) [^0123456789]*([0123456789])[^)]*\.com\/([^.]*)\.[^)]*\)[^\[]*\][^\]]*\]','{{ m.fit_but_cheatsheet(\'\\1\',\'\\2\',\'\\3\') }}',lines)
 

#lines = re.sub('\\\\\[caption[^!]*![^)]*\)[^\[]*\][^\]]*\]','',lines)
    
#\\\[caption[^!]*!\[([^ ]*) [^0123456789]*([0123456789])[^)]*\.com\/([^.]*)\.[^)]*\)[^\[]*\][^\]]*\]
    
#\\\[caption[^!]*!\[([^ ]*) [^)]*\.com\/([^.]*)\.[^)]*\)[^\[]*\][^\]]*\]
    
    # ','',lines)
#lines = re.sub('\\\\\[caption(.|\n)*caption\\\]','',lines)
# ','',lines)
# line = re.sub('\\\\\[caption','',line)
print(lines)