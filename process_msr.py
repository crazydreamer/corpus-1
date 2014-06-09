# -*- coding: utf-8 -*-

import os
with open('./msr_training.utf8') as f,open('./msr_training.txt','w') as fw:
	for line in f:
		line = line.strip()
		if line.startswith("“"):
			line = line[5:]	 # a quote and two spaces	
		fw.write(line+"\n")
fw.close()
