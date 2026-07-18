import time

lyrics = [
    "I watch the moon",
    "let it run my mood",
    "can't stop thinking of... you",
    "i watch youuuu(now i let it go asn i watch as things play out like)",
    "so long,nice to know you i'll be moving on",
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
        time.sleep(1.7)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)