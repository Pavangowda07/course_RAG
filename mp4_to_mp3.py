# Converting the videos to audios

import os
import subprocess

files = os.listdir("videos")

for file in files:
    # print(file)
    video_number = file.split("_")[0]
    video_name = file.split("_")[1].split(".mp3")[0]
    # print(video_number, video_name)
    subprocess.run(["ffmpeg", "-i", f"videos/{file}", f"audios/{video_number}_{video_name}.mp3"])
