import cv2
import sys,time

if len(sys.argv)>1:
  bgimg = sys.argv[1]
else:
  bgimg="bgimg.jpg"

bgimg=cv2.imread(bgimg)/2

ht,wt,nch=bgimg.shape


"""cv2.imshow('image',bgimg)
k = cv2.waitKey(0)"""

#cap = cv2.VideoCapture("output.avi")

# Define the codec and create VideoWriter object
fourcc = cv2.cv.CV_FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (wt,ht))



print ht,wt


#PARAMETERS
rec_ht,rec_wt=ht-1,30
rec_init_x=0
rec_init_y=0
rec_color=(255,255,255) #(200,0,180)
rec_delta=10


rec_init_x_backup=rec_init_x

while 1:
	#time.sleep(0.01)
	tempimg=bgimg.copy()
	rec_init_x+=rec_delta
	
	pt1= (rec_init_x,rec_init_y)
	pt2= [(rec_init_x+rec_wt),(rec_init_y+rec_ht)]
	if pt2[0]>wt-1:
		pt2[0]=wt-1

	if rec_init_x>=wt:
		rec_init_x=rec_init_x_backup

	pt2=tuple(pt2)
	#print pt1,pt2
	cv2.rectangle(tempimg, pt1, pt2,rec_color,thickness=-1)
	cv2.imshow("frame",tempimg)
	out.write(tempimg)
	if cv2.waitKey(1) & 0xff ==ord('q'):
		break
	



out.release()
cv2.destroyAllWindows()
