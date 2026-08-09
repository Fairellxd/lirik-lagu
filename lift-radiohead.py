import time

lyrics = [
    "The smell of air conditioning",
    "The fish are belly up",
    "empty all you pockets",
    "Because it's time......",
    "to come home"
    
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
        time.sleep(0.6)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)