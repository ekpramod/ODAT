import torch
import io
import os
import shutil
from PIL import Image
import cv2
import streamlit as st
import numpy as np
from detect_track import run

print(os.listdir())