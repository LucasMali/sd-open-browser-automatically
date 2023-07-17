import subprocess 
import gradio as gr
from modules import script_callbacks
from fastapi import FastAPI


def open_browser_after_startup_please(_: gr.Blocks, app: FastAPI):
  subprocess.call(["open", "http://localhost:7860"])

script_callbacks.on_app_started(open_browser_after_startup_please)