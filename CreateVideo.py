import os , cv2
Images =[]
path= "/Images"
file =os.listdir(path)
ext = os.splitext(file)
if ext in ['.gif', '.png','.jpg','.jpeg','.jfif']:
    file_name=path+"/"+file
print(file_name)
images= file.append()
count= len(images)
frame= cv2.imread(images[0])
width,height=frame.shape
size = (width,height)
print(size)
out= cv2.VideoWriter('Priject.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)
for i in range(0, count-1):
    cv2.imread(images)
    out.write()
    print('DONE')