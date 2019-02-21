import os
from os import listdir


dir=os.listdir('/media/catia/Lucas/Polavieja01032018_HuC-H2B_longAcquisition2')

dir.sort()

for file in dir:
	if file.endswith('.tif'):
		print file 