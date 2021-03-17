from pytube import Youtube

link = input("O link: ")
video = Youtube(link)
stream = video.streams.get_highest_resolution()
stream.download