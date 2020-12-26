from pafy import new
url = input("entrer your video her:")
video = new(url)
dl = video.getbest()
dl.download()
