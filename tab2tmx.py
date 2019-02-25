#program to convert tab seperated file to tmx (Transaltion Memory Exchange format)

import sys
import re

#open file using open file mode

fp = open(sys.argv[1]) # Open file on read mode
lines = fp.read().split("\n") # Create a list containing all lines
fp.close() # Close file

src_lang = sys.argv[2]
tgt_lang = sys.argv[3]

print ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<tmx version="1.4">\n<header adminlang="en-us" creationtool="PyTool" creationtoolversion="1.0" datatype="PlainText" o-tmf="ABCTransMem" segtype="sentence" srclang="en"/>\n<body>')

for line in lines:
	if(line != ""):
	        cols = line.split("\t")
	        src = cols[0]
	        tgt = cols[1]
	        if(src !="" or tgt != ""):
	            src = re.sub(r'&', "&amp;", src, flags=re.M)
	            src = re.sub(r'<', "&lt;", src, flags=re.M)
	            src = re.sub(r'>', "&gt;", src, flags=re.M)
	            src = re.sub(r'"', "&quot;", src, flags=re.M)
	            src = re.sub(r'\'', "&apos;", src, flags=re.M)
	            tgt = re.sub(r'&', "&amp;", tgt, flags=re.M)
	            tgt = re.sub(r'<', "&lt;", tgt, flags=re.M)
	            tgt = re.sub(r'>', "&gt;", tgt, flags=re.M)
	            tgt = re.sub(r'"', "&quot;", tgt, flags=re.M)
	            tgt = re.sub(r'\'', "&apos;", tgt, flags=re.M)
	            print ('<tu>\n<tuv xml:lang="',src_lang,'">\n',sep='')
	            print ('<seg>',src,'</seg>\n</tuv>\n',sep='')
	            print ('<tuv xml:lang="',tgt_lang,'">\n',sep='')
	            print ('<seg>',tgt,'</seg>\n</tuv>\n</tu>',sep='')

print ("</body></tmx>")
