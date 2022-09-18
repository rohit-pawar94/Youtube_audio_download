from pytube import YouTube

yt_link = input("Enter Youtube Link :=) ")

yt = YouTube(yt_link)
file_info = yt.streams.filter(only_audio=True)
print(yt.title)

############## Looping to get information of audio files ##############
# for index, info in enumerate(file_info):
#    print(index, info)

#download_audio = yt.streams.get_by_itag(140)
# download_audio.download()

print("Download Completed!!")
