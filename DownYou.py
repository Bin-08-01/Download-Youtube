from time import sleep

from pytube import YouTube

from tkinter import filedialog

patch1 = "*Hi! Đây là ứng dụng tải video từ Youtube \n"
patch2 = "*Welcome to my program \n"
patch3 = "*Tải video Youtube \n"

for x in patch1 + patch2 + patch3:
    print(x, end="", flush = True)
    sleep(0.05)
print()

while True:
    url = input("Nhập URL video và chọn nơi lưu: ").strip()
    yt = YouTube(url)
    global FolderName
    FolderName = filedialog.askdirectory()

    patch1 = "**Chọn định dạng file muốn tải về: \n"
    patch2 = "**1. sd.mp4 \n"
    patch3 = "**2. hd.mp4 \n"
    patch4 = "**3. audio.mp3 \n"
    patch5 = "**12 hoặc 23 để đồng thời tải 2 định dạng: \n"
    patch6 = "**4. Đóng chương trình."
    

    for x in patch1 + patch2 + patch3 + patch4 + patch5:
        print(x, end="", flush = True)
        sleep(0.05)
    print()

    key = int(input("Nhập lựa chọn của bạn: "))
    
    if (key==1):
        print("Video sd file downloading...")
        yt.streams.filter(progressive=True).first().download(FolderName)
    elif (key==2):
        print("Video hd file downloading...")
        yt.streams.filter(progressive=True).last().download(FolderName)
    elif (key==3):
        print("Audio file downloading...")
        yt.streams.filter(only_audio=True).first().download(FolderName)
    elif (key==13):
        print("Video sd and Audio file downloading...")
        yt.streams.filter(progressive=True).first().download(FolderName)
        yt.streams.filter(only_audio=True).first().download(FolderName)
    elif (key==23):
        print("Video hd and Audio file downloading...")
        yt.streams.filter(only_audio=True).first().download(FolderName)
        yt.streams.filter(progressive=True).last().download(FolderName)    
    elif (key==123):
        print("Tất cả định dạng đang được tải về...")
        yt.streams.filter(progressive=True).first().download(FolderName)
        yt.streams.filter(progressive=True).last().download(FolderName)
        yt.streams.filter(only_audio=True).first().download(FolderName)
    elif (key==4):
        print("Bạn đã thoát chương trình!")
        break
    
    else:
        print("Không có lựa chọn nào.")

