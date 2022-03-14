import os
import re
from pytube import Playlist

url = input("Playlist link:\n")
choice = int(input("Please choose one of the options:\n1-Audio\n2-Video\n3-Quit\n"))
playlist = Playlist(url)
if choice == 3:
    exit(1)


def get_audio():
    print(f'Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in.')

    for audio in playlist.videos:
        try:
            print(f"Downloading {audio.title}")
            audio.streams.filter(only_audio=True).get_by_itag(140).download()

            def rename(title):
                name = re.sub('[~<>:;"\'/?*.,|\\\\]', '', title)
                return name

            os.rename(f"{rename(audio.title)}.mp4", f"{rename(audio.title)}.mp3")
        except AttributeError:
            print('Attribute error.')


def get_video():
    print(f'Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in.')
    for video in playlist.videos:
        try:
            video.streams.filter(file_extension='mp4')
            print(f"Downloading {video.title}")
            video.streams.get_highest_resolution().download()
        except AttributeError:
            print('Attribute error.')


if __name__ == '__main__':
    if choice == 1:
        get_audio()
    elif choice == 2:
        get_video()
    else:
        print("Invalid choice.")
