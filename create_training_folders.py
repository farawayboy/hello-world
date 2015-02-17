'''
Created on 2015 2 15

@author: wshen
'''
import os

def makeFolder(folderName):
    if os.path.exists(folderName):
        print "folder existed: ",folderName
        pass
    else:
        os.makedirs(folderName)

if __name__ == '__main__':
    
    folderName = "./training_output/categories/models/event"
    makeFolder(folderName)

    folderName = "./training_output/meta_interests/models/tfidf"
    makeFolder(folderName)
    
    folderName = "./training_output/topics/models/sec_level"
    makeFolder(folderName)
    
    folderName = "./training_output/topics/models/tfidf"
    makeFolder(folderName)
    
    folderName = "./training_output/topics/models/top_level"
    makeFolder(folderName)
    
    print "done"
    pass