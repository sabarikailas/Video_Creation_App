import streamlit as st
import os
import glob

# Handling MoviePy version difference(v1.x vs v2.x)
try:
  from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
except ImportError:
    from moviepy import ImageClip, concatenate_videoclips, AudioFileClip
import yt_dlp

# --- 1. INITIALIZE STATE ---
if 'audio_path' not in st.session_state:
  st.session_state['audio_path'] = None
if 'yt_error' in st.session_state:
  pass # Keep it for display logic

# --- 2. DEFINE ALL FUNCTIONS ---

def
