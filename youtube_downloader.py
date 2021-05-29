from pytube import YouTube

#author rado

link = input("Please input your YouTube URL:")

yt = YouTube(link)

# to get all the formats?
videos = yt.streams.all()

# index all the formats in asc order
video = list(enumerate(videos))

for vid in video:
    print(vid)
    #print all the formats of the video
    
print ("Please input the desired format:")

download_options = int(input(" Enter the format: "))

download_video = videos[download_options]
download_video.download()

print("Video has downloaded successfully!")