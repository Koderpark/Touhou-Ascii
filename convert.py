import sys, random, argparse, os, math, os.path
import numpy as np
from PIL import Image
import cv2
import subprocess

# set scale default as 0.43 which suits a Courier font

def main():
    os.system('mode con: lines=15 cols=40')
    
    print("■■■■■■■■■■■■■■■■■■■■")
    print("■                                    ■")
    print("■      Video To Ascii Converter      ■")
    print("■                                    ■")
    print("■        ⊙Made By Koder0205         ■")
    print("■                                    ■")
    print("■■■■■■■■■■■■■■■■■■■■")
    print("")
    print("  MP4 File's Name(In input Folder)")
    print("  → ", end="")
    FileName = input().replace(".mp4", "")

    if os.path.isfile("input\\"+FileName+".mp4") == False :
        print("\n  ERROR. Please Check Your FileName")
        tmp = input()
        sys.exit()
    
    scale = 0.43 # 0.43은 Courier폰트를 기준으로 함.
    lamp  = ' .,-=+#%@$'
    count = 0
    
    vidcap = cv2.VideoCapture('input\\'+FileName+'.mp4')
    command = 'ffmpeg -i input\\'+FileName+'.mp4 -ab 160k -ac 2 -ar 44100 -vn files\\'+FileName+'.wav -y'
    subprocess.call(command, shell=False)
    f = open('files\\'+FileName+'.txt', 'w')
    
    os.system("cls")
    print("")
    print("  Convert Start.")
    
    while vidcap.isOpened():
        count += 1
        if count%300 == 0 :
            print("  "+str(int(count/30))+" Second Converted.")
        
        success,image = vidcap.read()
        
        frame = Image.fromarray(image).resize((160,90)).convert('L')
        img = np.array(frame)
        
        for i in range(39):
            aimg = ""
            for j in range(160):
                gsval = lamp[int((int(img[int(i/scale)][j])*10 - 1)/255)]
                aimg += gsval
            f.write(aimg+"\n")
    print("  Convert End.")
    tmp = input()
    
if __name__ == '__main__':
    main()
