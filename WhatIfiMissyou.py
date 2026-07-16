import time

lyrics = [
    "i have build a house where i wait for you return",
    "I only want you to be mine and not a lesson learned",
    "and i will wait and wait and wait until this city burns",
    "I and i wil wait and wait and wait and live on what we were.......",
    
]

def typing_animation(text, delay=0.09):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_lyrics(lyrics):
    print("")
    for line in lyrics:
        typing_animation(line)
        time.sleep(1.3)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)