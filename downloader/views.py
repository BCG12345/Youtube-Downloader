from django.shortcuts import render
from pytube import YouTube

def download(request):
    if request.method == 'POST':
        video_url = request.POST['video_url']
        try:
            yt = YouTube(video_url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            return render(request, 'success.html')
        except:
            return render(request, 'error.html')
    else:
        return render(request, 'download.html')