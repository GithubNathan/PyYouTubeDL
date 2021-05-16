from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)
ys = yt.streams.get_highest_resolution()
print("Downloading...")
ys.download("C:\Videos")
print("Download complete!")