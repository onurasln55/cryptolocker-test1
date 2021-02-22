import os
import fnmatch
path=input("drive path:") #partition
key=input("extension:")
for root, dir, files in os.walk(path+":/"):#folder walking
        print (root)
        print ("")
        for items in fnmatch.filter(files, "*"):
                print ("..." + items)
                name=items.split("."+key,1)
                try:
                    os.rename(root+"/"+items,root+"/"+name[0])
                except:
                    print("bu dosya var")
        print ("")
