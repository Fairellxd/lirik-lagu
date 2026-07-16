import time

lyrics = [
    "Kill the lights",
    "oh baby close your eyes",
    "the way you looking at me",
    "you got me mezmerized",
    "something i can't escape",
    "Feel like i'm lost in space",
    "you've got that good loving",
    "girl if you leave me i might throw my heart away"
]

def typing_animation(text, delay=0.05):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_lyrics(lyrics):
    print("")
    for line in lyrics:
        typing_animation(line)
        time.sleep(0.6)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)