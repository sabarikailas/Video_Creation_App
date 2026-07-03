import streamlit as st
import os
import glob

# Handling MoviePy version difference(v1.x vs v2.x)
try:
  from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
except ImportError:
  
