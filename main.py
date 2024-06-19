import pytube
import os

try:
    os.remove(r"C:\dloutput\output.mp4")
except:
    None

try:
    os.remove(r"C:\dloutput\output.mp3")
except:
    None

print(r"The files will be named output.mp3 and output.mp4 and will be stored in C:\dloutput\ ")
def mp3(link):
    yt = pytube.YouTube(str(link))
    vid = yt.streams.get_highest_resolution()
    try:
        vid.download(filename="output.mp4", output_path=r"C:\mpo")
        os.system(rf"ffmpeg -i C:\dloutput\output.mp4 C:\mpo\output.mp3")

    except:
        print("error")


link = input("YT Video link: ")
mp3(link)
