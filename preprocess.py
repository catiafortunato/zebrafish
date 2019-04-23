import numpy as np 
import h5py
import os

def get_min_max(num,dir,path):
	minimum=1000
	maximum=0
	for i in range (num,len(dir),100):
		im=h5py.File(path+dir[i],'r+')
		img=list(im['d1'])
		new_min=np.min(img)
		new_max=np.max(img)
		if new_min<minimum:
			minimum=new_min
		if new_max>maximum:
			maximum=new_max
	return (minimum,maximum)

def load_data(num,dir,path):
	data=[]
	for i in range (selected_slice, len(dir),100):
		im=h5py.File('data/'+dir[i],'r+')
    	img=list(im['d1']) 
    	data.append(img)
    return data 

def normalise_data(data,minimum,maximum):
	# get the values between 0 and 1
	data=data-minimum
	data=data/(0.5*(maximum-minimum))
	data=data/data
	return data

def downsample_data(data,rows,cols):
	down_data=np.zeros((len(data),rows,cols))
	for i in range (0,len(down_data)):
		img=data[i,:,:]
		dimg=np.zeros((rows,cols))
		for j in range(0,rows):
			for k in range (0,cols):
				dimg[j,k]=np.mean(img[j*50:j*50+50,k*50:k*50+50])
		down_data[i,:,:]=dimg
	return down_data