import os
import pathlib

def main():
    path=input("Enter the path of directory\n")  
    dest=input("Enter the name to apply\n")
    try:
        if os.path.exists(path):  #checks the path here
            i=1     
            for filenames in os.listdir(path):      #iterate through the directory
                extension=pathlib.Path(filenames).suffix   #got filetype
                new_src=path+"\\"+filenames
                new_dest=path+"\\"+dest+"_"+str(i)+extension
                os.rename(new_src,new_dest)
                i+=1
        else:
            print("Path not found\n")
    except KeyboardInterrupt:
        print("Keyboard Interrupt occured\nProgram Terminated")

if __name__=="__main__":
    main()


"""
Future Updates: 
1. differentiate file and folder  
2. ask user to include folder for process or not
3. should have interactive prompt atleast
"""