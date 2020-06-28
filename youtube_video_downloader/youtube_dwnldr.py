from pytube import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter import *
from threading import *
size=0
def downloaderthread():
    thread=Thread(target=downloader)
    thread.start()

def percentdownloaded(stream=None, chunk=None, file_handle=None, remaining=None):
    d=size-remaining
    per=d/size*100
    dwnld_button.config(text="{:00.00f} % downloaded".format(per))

def downloader():
    url=enter_url.get()
    global size
    if url is not None:
        dwnld_button.config(state=DISABLED,text="Starting....")
    try:
        path=askdirectory()
        if path is None:
            return
        ob=YouTube(url,on_progress_callback=percentdownloaded)
        strm=ob.streams.all()
        size=strm.filesize
        l2.config(text=strm.title)
        l2.pack(side=TOP,fill=X,padx=60,pady=50)
        strm.download(path)
        dwnld_button.config(state=NORMAL,text="Download")
        showinfo("Downloaded","File is downloaded")
        enter_url.delete(0,END)
        l2.pack_forger()
    except:
        pass
main=Tk()
main.title("YOUTUBE VIDEO DOWNLOADER")
main.geometry("600x600")
l=Label(main,text="YOUTUBE VIDEO DOWNLOADER",font=("verdana",18),justify=CENTER)
l.pack(side=TOP,fill=X,padx=60,pady=50)


enter_url=Entry(main,font=("verdana",18),justify=CENTER)
enter_url.pack(side=TOP,fill=X,padx=60,pady=50)

dwnld_button=Button(main,text="Download",font=("verdana",18),command=downloaderthread)
dwnld_button.pack(side=TOP,fill=X,padx=60,pady=50)

l2=Label(main,text="Title will be shown here",font=("verdana",18),justify=CENTER)
l1=Label(main)


main.mainloop()
