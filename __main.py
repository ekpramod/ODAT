import io
import os
import sys
import shutil
import streamlit as st

root = os.getcwd()

def AppRootDir():
    os.chdir(root)
    return root

def VideoDir():
    os.chdir( root + '/Detected')
    return root + '/Detected'    

def WriteTextFile():
    VideoDir()
    f = open("guru99.txt","w+")

    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
     
    f.close()
    AppRootDir()    

        
dir_list = os.listdir(AppRootDir())
st.write(dir_list)

WriteTextFile()

dir_list = os.listdir(VideoDir())
st.write(dir_list)

dir_list = os.listdir(AppRootDir())
st.write(dir_list)

f = os.remove(AppRootDir() + "/Detected/" + "guru99.txt")   

dir_list = os.listdir(VideoDir())
st.write(dir_list)

AppRootDir()
    