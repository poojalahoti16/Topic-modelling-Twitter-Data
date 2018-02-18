# from os import  rename, listdir
import os
import json



def extractJson(file1):

   # infileName = os.path.splitext(os.path.basename(file))[0]

    #outfileName =  fileToWrite + file
    global i
    infile = open(file1, 'r')
    lines = infile.read()
    infile.close()
    jsonObjects = json.loads(lines)

    
    for each in jsonObjects:
        
        try:
            print i
            i+=1
            jsonList.append(each['text'])
        except:
            jsonList.append(each)
            continue
    
     
        
        

i=0
fileStart = 'tweet_trump'

filelist = os.listdir('.')


jsonList = []
# out file
fileToWrite = 'extracted_Tweets.json'

for file1 in filelist:
    if file1.startswith(fileStart):
        extractJson(file1);

#
#for file1 in only_text:
#    if file1.startswith(fileStart):
#        extractJson(file1);


outfile = open(fileToWrite,'w')
outfile.write(json.dumps(jsonList))

outfile.close()





