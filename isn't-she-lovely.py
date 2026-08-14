import time

lyrics = [
    "isn't she lovely",
    "isn't she wonderful",
    "isn't she precious",
    "Less than one minute old",
    "I never thought through love we'd be making one as lovely as she",
    "But isn't she lovely made from love",
    
]

def typing_animation(text, delay=0.10):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_lyrics(lyrics):
    print("")
    for line in lyrics:
        typing_animation(line)
        time.sleep(2.0)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)