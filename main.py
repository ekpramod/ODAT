import io
import os
import sys
import shutil
import streamlit as st

cwd = os.getcwd()
dir_list = os.listdir(cwd)
print(cwd)
print(dir_list)

st.write("Hello")

