import pytube
import os

try:
    os.remove(r"output.mp4")
except:
    None

try:
    os.remove(r"output.mp3")
except:
    None
    
def mp3(link):
    yt = pytube.YouTube(str(link))
    vid = yt.streams.get_highest_resolution()
    try:
        vid.download(filename="output.mp4", output_path="")
        os.system(rf"ffmpeg -i output.mp4 output.mp3")

    except:
        print("error")


link = input("YT Video link: ")
mp3(link)
