from pytube import YouTube
import os

isDone = False

while not isDone:
    url = input("Enter the URL of the Youtube Video you wish to convert to MP3:")
    ytManager = YouTube(url)
    sound = ytManager.streams.filter(only_audio=True).first()

    folder = input("Enter the MP3 file destination folder (Leave it blank if you wish to be the current folder)\n") or os.getcwd()
    file = sound.download(output_path=folder)
    base, ext = os.path.splitext(file)
    name = base + '.mp3'
    os.rename(file, name)
    
    print(f"{base} has been downloaded to {folder}\n")
    checker = input("Do you wish to continue downloading? Y/N\n")
    checker.upper
    if checker == "N":
        isDone = True