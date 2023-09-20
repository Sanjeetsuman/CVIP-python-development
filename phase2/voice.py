import tkinter as tk
import sounddevice as sd
import numpy as np
import wave
import os
from tkinter import messagebox

# Create a directory to store the recordings
if not os.path.exists("recordings"):
    os.mkdir("recordings")

recording_number = 1
is_recording = False

def start_recording():
    global is_recording
    global recording_number
    
    if not is_recording:
        is_recording = True
        record_button.config(text="Stop Recording", bg="red")
        file_name = f"recordings/recording{recording_number}.wav"
        recording_number += 1
        sd.default.samplerate = 44100  # Sample rate
        sd.default.channels = 2  # Stereo
        recording = sd.rec(int(10 * 44100), samplerate=44100, channels=2, dtype=np.int16)
        sd.wait()
        with wave.open(file_name, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(44100)
            wf.writeframes(recording.tobytes())
    else:
        is_recording = False
        record_button.config(text="Start Recording", bg="green")

def show_info():
    messagebox.showinfo("About", "Voice Recorder Application\nVersion 1.0\n© 2023 Your Name")

app = tk.Tk()
app.title("Voice Recorder")

record_button = tk.Button(app, text="Start Recording", command=start_recording, bg="green", padx=10, pady=5)
record_button.pack(pady=20)

info_button = tk.Button(app, text="About", command=show_info)
info_button.pack()

app.mainloop()
