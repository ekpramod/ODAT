import io
import os
import sys
import shutil
import streamlit as st

cwd = os.getcwd()
dir = os.listdir(cwd)
print(cwd,flush)
print(dir,flush)

st.write("Hello")

