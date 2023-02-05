import os
import re
from pytube import Playlist, YouTube

opt = int(input("Please choose an option:\n1-Download a playlist.\n2-Download only one video.\n3-Exit\n> "))
choice = int(input("Please choose an option:\n1-Audio\n2-Video\n3-Quit\n> "))
url = None
playlist = None

if opt == 3 or choice == 3:
    exit(1)
elif opt == 1:
    url = input("Playlist link: ")
    playlist = Playlist(url)
elif opt == 2:
    url = input("YouTube link: ")


def rename(title):
    name = re.sub(r'[\\~<>:;"#\'/?*.,|\\\\]+', '', title)
    return name


def get_single_audio_file():
    audio = YouTube(url)
    try:
        print(f"Downloading {audio.title}")
        audio.streams.filter(only_audio=True).get_by_itag(140).download()
        os.rename(f"{rename(audio.title)}.mp4", f"{rename(audio.title)}.mp3")
    except AttributeError:
        print('Attribute error.')


def get_single_video_file():
    video = YouTube(url)
    print(f"Downloading {video.title}")
    try:
        video.streams.filter(file_extension='mp4')
        print(f"Downloading {video.title}")
        video.streams.get_highest_resolution().download()
    except AttributeError:
        print('Attribute error.')


def get_audio_playlist():
    print(f'Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in.')

    for audio in playlist.videos:
        try:
            print(f"Downloading {audio.title}")
            audio.streams.filter(only_audio=True).get_by_itag(140).download()
            os.rename(f"{rename(audio.title)}.mp4", f"{rename(audio.title)}.mp3")
        except AttributeError:
            print('Attribute error.')


def get_video_playlist():
    print(f'Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in.')
    for video in playlist.videos:
        try:
            video.streams.filter(file_extension='mp4')
            print(f"Downloading {video.title}")
            video.streams.get_highest_resolution().download()
        except AttributeError:
            print('Attribute error.')


if __name__ == '__main__':
    if opt == 1 and choice == 1:
        get_audio_playlist()
    elif opt == 1 and choice == 2:
        get_video_playlist()
    elif opt == 2 and choice == 1:
        get_single_audio_file()
    elif opt == 2 and choice == 2:
        get_single_video_file()
    else:
        print("Invalid choice.")
