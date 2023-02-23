import io
import os
import sys
import shutil
import streamlit as st

cwd = os.getcwd()
dir_list = os.listdir(cwd)
print(cwd)
print(dir_list)

st.write(cwd)
st.write(dir_list)

os.chdir( cwd + '/Detected')
f= open("guru99.txt","w+")

for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
     
f.close()     

dir_list = os.listdir()
print(dir_list)

os.chdir(cwd)
