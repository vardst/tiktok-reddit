from turtle import title
from utils.console import print_markdown
import time
from reddit.askreddit import get_askreddit_threads
from video_creation.background import download_background, chop_background_video
from video_creation.voices import save_text_to_mp3
from video_creation.screenshot_downloader import download_screenshots_of_reddit_posts
from video_creation.final_video import make_final_video



def main():
    print_markdown("Vurdun And Co Creation")
    time.sleep(1)
    reddit_object = get_askreddit_threads()
    length, number_of_comments = save_text_to_mp3(reddit_object[0])
    download_screenshots_of_reddit_posts(reddit_object[0], number_of_comments)
    download_background()
    chop_background_video(length)
    final_video = make_final_video(number_of_comments)

if __name__ == '__main__':
    main()