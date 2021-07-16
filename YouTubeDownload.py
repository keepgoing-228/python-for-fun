
def rdVideo(): 
    global getVideo
    getVideo = videorb.get()
    labelmsg.config(text=getVideo)
    # print("hi")
    
def clickDown():  
    global getvideo, strftype, listradio
    labelmsg.config(text="")
    if(URL.get()==""):  
        labelmsg.config(text="URL has to be corrected!!")
        return

    if(path.get()==""):
        labelmsg.config(text="Please input your right download dir")
        return
    else:
        pathdir = path.get()
        pathdir = pathdir.replace("\\", "\\\\")  #將「\」轉換為「\\」

    try:
        yt = YouTube(URL.get())
        yt.streams.filter(subtype='mp4', res=getVideo, progressive=True).first().download(pathdir)  #下載mp4影片
        labelmsg.config(text="finish download :))")
    except:
        labelmsg.config(text="can't download :((")




import tkinter as tk
from pytube import YouTube


win = tk.Tk()
win.geometry("600x300")
win.title("YouTube Downloader")

getVideo = "720p"
videorb = tk.StringVar()
videorb.set(getVideo)
URL = tk.StringVar()
path = tk.StringVar()

label1 = tk.Label(win, text="Youtube URL: ")
label1.place(x = 90,y = 30)
entryURL = tk.Entry(win, textvariable= URL)
entryURL.config(width= 50)
entryURL.place(x = 200,y = 30)
label2 = tk.Label(win, text="Download path: ")
label2.place(x= 90, y=80)
entryPath = tk.Entry(win, textvariable= path)
entryPath.config(width= 50)
entryPath.place(x = 200,y = 80)

item1 = tk.Radiobutton(win, text="360p, mp4", variable=videorb, value="360p", command=rdVideo)
# item1.select()
item1.place(x=200, y=120)
item2 = tk.Radiobutton(win, text="720p, mp4", variable=videorb, value="720p", command=rdVideo)
item2.place(x=200, y=150)
item3 = tk.Radiobutton(win, text="1080p, mp4", variable=videorb, value="1080p", command=rdVideo)
item3.place(x=200, y=180)

buttonDown = tk.Button(win, text="Download", command=clickDown)
buttonDown.place(x=260, y=220)

labelmsg = tk.Label(win, text="", fg="red")
labelmsg.place(x=230, y=260)


win.mainloop()


# yt = YouTube('https://www.youtube.com/watch?v=HTgVbJztIPY')

# print("start download YouTube video: "+ yt.title)
# downloadPath ='D:\\NTU\the DoDo men'
# # yt.streams.first().download(downloadPath)
# yt.streams.filter(res='1080p',subtype='mp4').download(downloadPath)
# print("finish")

