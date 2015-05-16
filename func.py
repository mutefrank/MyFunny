#coding=utf-8
import os
import subprocess
import web
from anjuke import pinyin
import jieba
import random
import datetime
videoPath = '/usr/local/nginx/video/ts/'

def splitWords(words):
    return jieba.cut(words, cut_all=False)

def convert(word):
    converter = pinyin.Converter()
    converter.load_word_file('chars.txt')
    return  converter.convert(word, fmt = 'tn')

def findVideo(word):
    for root,dirs,files in os.walk(videoPath):
        for vFile in files:
	    if '_'+word in vFile:
                return os.path.join(root,vFile)
    return None

def generateH5Page(video):
    print '--------------- video',video
    return '<video src="http://123.57.137.127/'+video+'" controls="controls">video</video><h1>:)</h1>'

def mergeVideo(videoPaths):
    params = 'ffmpeg -i "concat:'
    for path in videoPaths:
	params += path
	params += '|'
    params = params[0:len(params)-1] 
    fileName = str(datetime.datetime.now().microsecond) + str(random.randint(0,100000))+ '.mp4'
    outputPath = '/usr/local/nginx/html/' + fileName
    params += '" -c copy -bsf:a aac_adtstoasc '+ outputPath
    print '----------------------params:', params
    subprocess.call(params,shell=True)    
    return fileName

urls = (
    '/v1/video/(.*)', 'video'
)

class video:
    def GET(self,name):      
        value = web.input()
	inputWords = value.name
        splitWords = convert(inputWords).split(' ')
        finalPath = []
        for word in splitWords:
            videoPath = findVideo(word)
            if videoPath != None:
                finalPath.append(videoPath)
        outputVideo = mergeVideo(finalPath)
        web.header('content-type','text/html')
        return generateH5Page(outputVideo)

app = web.application(urls, globals())
application = app.wsgifunc()

