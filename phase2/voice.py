import tkinter as tk
from tkinter import ttk
import sounddevice as sd
import wave
import os

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.recording = False
        self.file_number = 1
        # UI Elements
        self.record_button = ttk.Button(root, text="Start Recording", command=self.toggle_recording)
        self.record_button.pack(pady=20)

        self.file_listbox = tk.Listbox(root)
        self.file_listbox.pack(pady=10)

        self.save_button = ttk.Button(root, text="Save Recording", command=self.save_recording, state=tk.DISABLED)
        self.save_button.pack()

        # Create a directory to store the recordings
        if not os.path.exists("recordings"):
            os.mkdir("recordings")

        self.refresh_file_list()

    def toggle_recording(self):
        if not self.recording:
            self.start_recording()
        else:
            self.stop_recording()

    def start_recording(self):
        self.recording = True
        self.record_button.config(text="Stop Recording")
        self.save_button.config(state=tk.DISABLED)

        # Start recording
        self.recording_data = sd.rec(int(10 * 44100), samplerate=44100, channels=2, dtype='int16')

    def stop_recording(self):
        self.recording = False
        self.record_button.config(text="Start Recording")
        self.save_button.config(state=tk.NORMAL)

        # Stop recording
        sd.wait()

        # Save the recording as a WAV file
        file_name = f"recordings/recording{self.file_number}.wav"
        self.file_number += 1

        with wave.open(file_name, 'wb') as wf:
            wf.setnchannels(2)
            wf.setsampwidth(2)
            wf.setframerate(44100)
            wf.writeframes(self.recording_data.tobytes())

        self.refresh_file_list()

    def save_recording(self):
        selected_item = self.file_listbox.curselection()
        if selected_item:
            selected_file = self.file_listbox.get(selected_item)
            source_path = f"recordings/{selected_file}"
            destination_path = f"saved_recordings/{selected_file}"

            # Copy the recording to a new directory (e.g., 'saved_recordings')
            os.makedirs("saved_recordings", exist_ok=True)
            os.replace(source_path, destination_path)

            self.refresh_file_list()

    def refresh_file_list(self):
        self.file_listbox.delete(0, tk.END)

        # Display the list of recorded files
        recordings = sorted(os.listdir("recordings"))
        for recording in recordings:
            self.file_listbox.insert(tk.END, recording)

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
