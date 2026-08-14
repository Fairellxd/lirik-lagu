import time

lyrics = [
    "For what is a man",
    "What has he got",
    "If not himself",
    "Then he has naught",
    "To say the things",
    "he truly feels",
    "And not the words",
    "of one who kneels",
    "The record shows",
    "I took the blows",
    "And did it my way",
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