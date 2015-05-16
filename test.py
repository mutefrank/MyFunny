#coding=utf-8
import os
import subprocess
from anjuke import pinyin
import jieba

videoPath = '../video/seg'
for root,dirs,files in os.walk(videoPath):
        for vFile in files:
            path = os.path.join(root,vFile)
            outputPath = os.path.join('../video/ts',vFile)
            param = 'ffmpeg -i '+path +'  -c copy -bsf h264_mp4toannexb '+ outputPath +'.ts' 
            print param
            subprocess.call([ param ], shell= True)
