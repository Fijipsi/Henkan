from __future__ import unicode_literals
import youtube_dl
from tkinter import Tk,Label,Button,Frame,simpledialog
from tkinter import messagebox
from tkinter.ttk import Progressbar
from PIL import Image, ImageTk
import os
import requests

#---YoutubeDL functions

#video_name='https://www.youtube.com/watch?v=GGQygrKegFc'


ydl_opts = {
	'format': 'bestaudio/best/filesize',
	'postprocessors' : [{
	'key': 'FFmpegExtractAudio',
	'preferredcodec': 'mp3',
	'preferredquality': '192',
	}],
}


#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#	ydl.download([video_name])


#---Functions---
def passUrlData(url=0):
	url = simpledialog.askstring("Enter URL", "Please Enter a Youtube Video Link")
	addDownloadItem(url)

def getStandardSize(size):
	itme = ['bytes','KB','MB','GB','TB']

	for x in itme:
		if size<1024.0:
			return "%3.1f %s" % (size, x)
		size/=1024.0

	return size

def addDownloadItem(url):

	if url != None:

		req = requests.get(url, stream=True)

		try:

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:			
				total_size = ydl.filesize[url]
		except:
			total_size = 1000
			filename = ""

			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				fname = "file" #ydl.tittle(url)



		frame2=Frame(window,bg="red", height="5")
		frame2.pack(fill="x",expand=False, pady=10)
		frame2.columnconfigure(1,weight=1)

		img=Image.open("file_icon.png")
		render=ImageTk.PhotoImage(img)


		label=Label(frame2,image=render,width=150,height=150, bg="red")
		label.image=render
		label.grid(row=0,column=0, rowspan=2)


		tittle=Label(frame2,text="File",padx=5,pady=5, bg="red",fg="white", anchor="w")
		tittle.config(font=("Arial","15"))
		tittle.grid(row=0,column=1,sticky="nsew")

		progress=Progressbar(frame2)
		progress['value']=50
		progress.grid(row=1,column=1,padx=5,pady=5,sticky="nsew")

		labelPercentage=Label(frame2,text="0%", padx="5",anchor="w" , bg="red",fg="white")
		labelPercentage.grid(row=0,column=2)
		labelSize=Label(frame2,text="0 Kb", padx="5",anchor="w" , bg="red",fg="white")
		labelSize.grid(row=1,column=2)



		with open(fname,"wb") as fileobj:
			for chunk in req.iter_content(chunk_size=1024):
				if chunk:
					fileobj.write(chunk)
					current_size=os.path.getsize(fname)
					print(current_size)
					labelSize.config(text=str(getStandardSize(current_size)))
					print(total_size)
				
					#percentg=round((int(current_size)/int(total_size))*145)
					#labelPercentage.config(text=str(percentg)+" %") 	
					#progress['value']=percentg

		current_size=os.path.getsize(fname)

		percentg=round((int(current_size)/int(total_size))*100)
		progress['value']=percentg







		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
			ydl.download([url])




#---Tkinter---

window=Tk()
window.title("Henkan")
window.geometry("800x600")
frame=Frame(window, bg="gray")
frame.pack(fill="both", expand=True)


rowframe=Frame(frame, bg="yellow")
rowframe.pack(fill="x", expand=True)
button=Button(rowframe,text="Add Download URL",bg="#27AE60",fg="white",padx=10,pady=10,activebackground="#34e0d5", command=passUrlData) 
button.grid(row=0,column=0,sticky="nsew",padx=10,pady=10)
button1=Button(rowframe,text="Exit Program",bg="#ff0000",fg="white",padx=10,pady=10,activebackground="#34e0d5")
button1.grid(row=0,column=1,sticky="nsew",padx=10,pady=10)
#rowframe.grid_columnconfigure(0,weight=1)
#rowframe.grid_columnconfigure(1,weight=1)
rowframe.pack(fill="x", expand=True)


window.mainloop()