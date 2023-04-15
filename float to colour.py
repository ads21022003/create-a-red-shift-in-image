from PIL import Image
from numpy import array
import numpy as np
import math
import colorsys
def rgb_to_hsv(r, g, b):

	# R, G, B values are divided by 255
	# to change the range from 0..255 to 0..1:
	r, g, b = r / 255.0, g / 255.0, b / 255.0

	# h, s, v = hue, saturation, value
	cmax = max(r, g, b) # maximum of r, g, b
	cmin = min(r, g, b) # minimum of r, g, b
	diff = cmax-cmin	 # diff of cmax and cmin.

	# if cmax and cmax are equal then h = 0
	if cmax == cmin:
		h = 0
	# if cmax equal r then compute h
	elif cmax == r:
		h = (60 * ((g - b) / diff) + 360) % 360

	# if cmax equal g then compute h
	elif cmax == g:
		h = (60 * ((b - r) / diff) + 120) % 360

	# if cmax equal b then compute h
	elif cmax == b:
		h = (60 * ((r - g) / diff) + 240) % 360

	# if cmax equal zero
	if cmax == 0:
		s = 0
	else:
		s = (diff / cmax) 

	# compute v
	v = cmax 
	return [h, s, v]

# image address
im_1 = Image.open(r"C:\Users\Aditya Singh\Downloads\bokeh-313996_1280.jpg")
#im_1 = Image.open(r"C:\Users\Aditya Singh\Downloads\Card6_564766791.jpg")
ar = array(im_1)
print(ar.shape)
out_im= np.zeros((ar.shape[0], ar.shape[1], ar.shape[2]), np.uint8)

for i in range(0,ar.shape[0]):
   for j in range(0,ar.shape[1]) :
      D= rgb_to_hsv(ar[i,j,0],ar[i,j,1], ar[i,j,1])
      nm =(650 - 250 / 270 * D[0])
      C = 299792458
      ratio =0.27
      shift_nm = nm * (math.sqrt(1+ratio)/math.sqrt(1-ratio))
      if( shift_nm <650 and shift_nm>380):
        D[0]= (650-shift_nm)*(270/250)
        D = colorsys.hsv_to_rgb(D[0]/360.0, D[1], D[2])
        out_im[i,j,0],out_im[i,j,1],out_im[i,j,2]=(int(255*D[0]),int(255*D[1]),int(255*D[2]))
img = Image.fromarray(out_im, 'RGB')
img.save("my03.png")
img.show()      

