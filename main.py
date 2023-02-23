import io
import os
import sys
import shutil
import streamlit as st

root = os.getcwd()
dir_list = os.listdir(root)

def AppRootDir():
    return root

def VideoDir():
    return os.chdir( AppRootDir() + '/Detected') 

def WriteTextFile():
    VideoDir()
    f = open("guru99.txt","w+")

    for i in range(10):
        f.write("This is line %d\r\n" % (i+1))
     
    f.close()     

        
AppRootDir()
dir_list = os.listdir()
st.write(dir_list)

VideoDir()
dir_list = os.listdir()
st.write(dir_list)

AppRootDir()
dir_list = os.listdir()
st.write(dir_list)

   
    