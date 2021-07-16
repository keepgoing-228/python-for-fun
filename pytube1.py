from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=HTgVbJztIPY')

print("start download YouTube video: "+ yt.title)
downloadPath ='D:\\NTU\the DoDo men'
# yt.streams.first().download(downloadPath)
yt.streams.filter(res='1080p',subtype='mp4').download(downloadPath)
print("finish")

