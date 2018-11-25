import cv2
import numpy as np
from matplotlib import pyplot as plt

#�������{�^���̐F�͈̔͐ݒ�AHSV�\�L
HueTop = 30
HueBottom = 25
SatTop = 50
SatBottom = 0
ValTop = 256
ValBottom = 245

#�{�^���̍��W�Ɩ��O
coordinate = [
              [[40,240],[80,280]],[[125,240],[165,280]],
              [[205,240],[245,280]],[[285,240],[325,280]],
              [[360,240],[400,280]],[[440,240],[480,280]]
              ]
name = {0:"�������x��",1:"��t�������x��",2:"�V�A�����o�x��",3:"������PH�ُ�",4:"�x�R�x��",5:"�ߓd���ꊇ"}


point = []
count = [0 for i in range(len(coordinate))]
#�ǂݍ���
img_path = 'C:\\Users\\mststar0510\\Desktop\\programing\\jupyter\\img\\redonlylamp.png'
img = cv2.imread(img_path)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#blur = cv2.GaussianBlur(img,(31,31),0)

#RGB��HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#�����p
h1 = hsv[:,:,0]>HueBottom
h2 = hsv[:,:,0]<HueTop
s1 = hsv[:,:,1]>SatBottom
s2 = hsv[:,:,1]<SatTop
v1 = hsv[:,:,2]>ValBottom
v2 = hsv[:,:,2]<ValTop


for i in range(hsv.shape[0]):
    for j in range(hsv.shape[1]):
        if (h1[i][j] and h2[i][j]) and (s1[i][j] and s2[i][j]) and (v[i][j] and v[i][j]):
            point.append([j,i])
print(point)

for i in range(len(point)):
    for j in range(len(coordinate)):
        if coordinate[j][0][0]<point[i][0]<coordinate[j][1][0] and coordinate[j][0][1]<point[i][1]<coordinate[j][1][1]:
            count[j]=1
            break
            
for i in range(len(coordinate)):
    if count[i]==1:
        print(name[i],'���_�����Ă��܂��B')
print("finish")
plt.imshow(img)