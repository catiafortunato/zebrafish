import PIL
from PIL import Image
import numpy as np
import h5py
import os 
from os import listdir 

dir=os.listdir('/media/catia/Lucas/Polavieja01032018_HuC-H2B_longAcquisition2')
dir.sort()

for file in dir:
    if file.endswith('.tif'):    
        str1='/media/catia/Lucas/Polavieja01032018_HuC-H2B_longAcquisition2/'
        str2=file
        name=str1+str2
        img=Image.open(name)
        imarray=np.array(img)
        str3='data/'
        str2=str2.split('.')
        new_name=str3+str2[0]+'.h5'
        hf = h5py.File(new_name, 'w')
        hf.create_dataset('d1', data=imarray)
        hf.close()
        print(new_name)


