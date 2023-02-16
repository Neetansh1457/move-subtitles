import os
import shutil

path = "ENTER YOUR PATH"

os.chdir(path)

for file in os.listdir(path):
    srt_files = [f for f in os.listdir(path + "\\" + file) if f.lower().endswith(".srt")]
    if srt_files:
        os.chdir(path + "\\" + file)
        if not os.path.exists(os.path.join(os.getcwd(), "Subs")):
            os.mkdir("Subs")
        for srt in srt_files:
            shutil.move(srt, os.path.join(os.getcwd(), "Subs", srt))
    os.chdir(path)