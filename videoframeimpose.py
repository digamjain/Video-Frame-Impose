import cv2
import os
import magic
from PIL import Image

#Check if the file provided is in the correct media format
def check(name):

	if magic.Magic(mime=True).from_file(name).split('/')[0] == 'video':
		return True
	else:
		print('Incorrect codec foramt!')
		quit()

#Make directories for the frames of video
def mkdir(name,num):

	name = name+num
	dir_name = ""
	if not os.path.exists(f'frames-{name}'):
		os.makedirs(f'frames-{name}')
		dir_name = f'frames-{name}'
	else:
		if num=="":
			return mkdir(name,"1")
		else:
			return mkdir(name[:-len(num)],str(int(num)+1))
	return dir_name

#Input the name and skipping frames from user
def file():

	name = input("Enter file name: ").strip()
	if name == "":
		print("File name can't be empty..Quitting!")
		quit()
	elif os.path.exists(name) == False:
		print('File not found in the current directory!')
		quit()
	check(name)
	
	skip_frame = input("Enter number of frames to skip while imposing(Press enter to impose all frames): ")
	if skip_frame == "": 
		skip_frame = 0
	try:
		skip_frame = int(float(skip_frame))
	except:
		print("Skipable frames can't be ",type(skip_frame))
		quit()
	if skip_frame<0:
		print("Skipable frames can't be less than 0")
		quit()
	return name,int(skip_frame)+1

#Extract frames from video into a folder
def frames(name,dir_name):

	video = cv2.VideoCapture(name)
	frame_count = 1
	img_name = ""

	while(True):
		ret,frame = video.read()

		if ret:
			img_name = f'./{dir_name}/frame_{str(frame_count)}.jpg'
			print(f"Exporting frame {frame_count}..")

			cv2.imwrite(img_name,frame)
			frame_count = frame_count+1
		else:
			break
	video.release()
	cv2.destroyAllWindows()
	return frame_count-1

#Function to superimpose extracted images by changing factor
def superimpose(frame_count,dir_name,skip_frame):
				
	factor = (1 - 10/(frame_count/skip_frame)) if 10/(frame_count/skip_frame)>0.5 else 10/(frame_count/skip_frame)

	nfactor = factor
	temp = frame_count
	while(frame_count>1):
		try:
			img1 = Image.open("Imp_image.jpg")
		except:	
			Image.open(f'./{dir_name}/frame_{str(frame_count)}.jpg').save('Imp_image.jpg')
			img1 = Image.open("Imp_image.jpg")
		try:
			frame_count = frame_count - skip_frame
			print("Imposing image",temp - frame_count,"by factor:",nfactor)
			img2 = Image.open(f'./{dir_name}/frame_{str(frame_count)}.jpg')
			newimg = Image.blend(img1,img2,alpha = nfactor)
			nfactor = nfactor/2 + factor
			newimg.save('Imp_image.jpg')
		except:
			return		
	return

#Main function
def main():

	name,skip_frame = file()
	
	dir_name = ""
	dir_name = mkdir(name,"")
	
	frame_count = frames(name,dir_name)
	superimpose(frame_count,dir_name,skip_frame)
	
	return

if __name__=="__main__":

	main()	