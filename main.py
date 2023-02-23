import io
import os
import sys
import shutil
import streamlit as st

cwd = os.getcwd()
dir = os.listdir(cwd)
print(cwd,flush-True)
print(dir,flush=True)

st.write("Hello")

