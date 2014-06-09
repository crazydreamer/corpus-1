# -*- coding: utf-8 -*-

import os
with open('./pku_training.utf8') as f,open('./pku_training.txt','w') as fw:
	for line in f:
		line = line.strip()
		if line:
			line = line.replace("。  ","。\n")
			fw.write(line+"\n")
fw.close()
