import os
import cv2


path = "Images\Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        images.append(file_name)
        

count = len(images)

frame = cv2.imread(images[0])
height,width,channel = frame.shape



friends_video= cv2.VideoWriter('friends.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 10, (width,height))

for i in range(count-1,0,-1):
    friend = cv2.imread(images[i])
    friends_video.write(friend)

friends_video.release()
print("Video is created...")
