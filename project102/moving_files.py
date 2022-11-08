import os
import shutil

fromdir = "C:/Users/user/Downloads"
todir = "C:/Users/user/Desktop/document_files"

listOfFiles = os.listdir(fromdir)

for fileName in listOfFiles:
    name, nameExtension = os.path.splitext(fileName)

    if nameExtension == " " :
        continue

    if nameExtension == ['.jpg', '.jpeg', '.png', '.jfif', '.pdf', '.txt', '.txtas']:
        path1 = fromdir + "/" + fileName
        path2 = todir + "/" + "document_files"
        path3 = todir + "/" + "'document_files" + "/" + fileName

        print("path_1:", path1)
        print("path_3:", path3)

        if os.path.exists(path2):
            shutil.move(path1,path3)
        
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)