## Para baixar a lib pytube:  pip install pytube 
## baixar um video do youtube com pytube
## python youtube.py   https://youtu.be/61R6Qq7mmIA

from pytube import YouTube
link = str(input("Digite o link: "))
video = YouTube(link)
stream = video.streams.get_highest_resolution()
stream.download()