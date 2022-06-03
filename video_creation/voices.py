from gtts import gTTS
from pathlib import Path
from mutagen.mp3 import MP3
from utils.console import print_step, print_substep
from rich.progress import track


def save_text_to_mp3(reddit_obj):
    print_step("Saving Text to MP3 files 🎶")
    length = 0


    Path("assets/mp3").mkdir(parents=True, exist_ok=True)
    # print(type(reddit_obj),reddit_obj)
    tts = gTTS(text=reddit_obj["thread_title"], lang="en", slow=False, tld="co.uk")
    tts.save(f"assets/mp3/title.mp3")
    length += MP3(f"assets/mp3/title.mp3").info.length

    for idx, comment in track(enumerate(reddit_obj["comments"]), "Saving..."):
        if length > 40:
            break
        tts = gTTS(text=comment["comment_body"], lang="en")
        tts.save(f"assets/mp3/{idx}.mp3")
        length += MP3(f"assets/mp3/{idx}.mp3").info.length

    print_substep("Saved Text to MP3 files Successfully.", style="bold green")
    return length, idx
