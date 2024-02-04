import os
import re
from pytube import Playlist, YouTube


def check_option():
    opt = 0
    while True:
        try:
            opt = int(
                input(
                    "Please choose an option:\n1-Download a playlist.\n2-Download only one video.\n3-Exit\n> "
                )
            )
            if opt in [1, 2, 3]:
                break
            else:
                print("Invalid option. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    if opt == 3:
        exit(1)
    return opt


def get_choice():
    choice = 0
    while True:
        try:
            choice = int(
                input("Please choose an option:\n1-Audio\n2-Video\n3-Quit\n> ")
            )
            if choice in [1, 2, 3]:
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    return choice


def rename(title):
    name = re.sub(r'[\/~<>:"#\'/?*.|,\\\\]+', "", title)
    return name


def download_single_audio(url):
    audio = YouTube(url)
    try:
        print(f"Downloading {audio.title}")
        audio.streams.filter(only_audio=True).get_by_itag(140).download()
        name = rename(audio.title)
        print(f"Saved as {name}.mp3")
        os.rename(f"{name}.mp4", f"{name}.mp3")
    except Exception as e:
        print(f"Download failed: {e}")


def download_single_video(url):
    video = YouTube(url)
    print(f"Downloading {video.title}")
    try:
        video.streams.get_highest_resolution().download()
        name = rename(video.title)
        print(f"Saved as {name}.mp4")
    except Exception as e:
        print(f"Download failed: {e}")


def download_audio_playlist(playlist):
    print(
        f"Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in."
    )
    for audio in playlist.videos:
        try:
            print(f"Downloading {audio.title}")
            audio.streams.filter(only_audio=True).get_by_itag(140).download()
            name = rename(audio.title)
            print(f"Saved as {name}.mp3")
            os.rename(f"{name}.mp4", f"{name}.mp3")
        except Exception as e:
            print(f"Download failed for {audio.title}: {e}")


def download_video_playlist(playlist):
    print(
        f"Downloading: {playlist.title} which has {len(playlist.video_urls)} videos in."
    )
    for video in playlist.videos:
        try:
            video.streams.get_highest_resolution().download()
            name = rename(video.title)
            print(f"Saved as {name}.mp4")
        except Exception as e:
            print(f"Download failed for {video.title}: {e}")


if __name__ == "__main__":

    opt = check_option()
    if opt == 1:
        url = input("Playlist link: ")
        playlist = Playlist(url)
    elif opt == 2:
        url = input("YouTube link: ")

    choice = get_choice()

    if opt == 1 and choice == 1:
        download_audio_playlist(playlist)
    elif opt == 1 and choice == 2:
        download_video_playlist(playlist)
    elif opt == 2 and choice == 1:
        download_single_audio(url)
    elif opt == 2 and choice == 2:
        download_single_video(url)

print("Done!")
input("Press any key to exit.")
