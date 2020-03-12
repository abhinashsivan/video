import cv2

#path to the video to be converted
vidcap = cv2.VideoCapture('video.mp4')
success,image = vidcap.read()

count = 0

while success:
  # save frame as JPEG file  
	cv2.imwrite("frame%d.jpg" % count, image)        
	success,image = vidcap.read()
	print('Read a new frame: %d'%count, success)
	count += 1
