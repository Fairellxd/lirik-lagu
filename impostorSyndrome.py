import time

lyrics = [
    "just watch me moving far away",
    "nobody even know my name and",
    "no one suspects that im not fine and",
    "nobody outs behavioral Frankenstein",
    "just look at victor in LA",
    "and Syd with the Y at U of A",
    "and all the majors at the labels",
    "rebooting soon as im able"
]

def typing_animation(text, delay=0.12):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def show_lyrics(lyrics):
    print("")
    for line in lyrics:
        typing_animation(line)
        time.sleep(0.2)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)