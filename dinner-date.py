import time

lyrics = [
    "I wanted to tell you",
    "Tell me what you thinking",
    "if you could see from my point of view,you'd understand the way i get so confused ",
    "By the way you looking at me",
    "i've done this so many times before",
    "So why'd i get so nervous that day",
    "from the second that you walked through the door ",
 
]

def typing_animation(text, delay=0.06):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_lyrics(lyrics):
    print("")
    for line in lyrics:
        typing_animation(line)
        time.sleep(1.2)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)