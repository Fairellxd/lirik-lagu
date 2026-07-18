import time

lyrics = [
    "i saw it glitter as i grew",
    "and loved, why i never knew",
    "i thought this place was heaven send",
    "but now it's just a monument in my mind",
    "in my mind",
    "and i couldn't help but fall in love again",
    "no i couldn't help but fall in love again",
    
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
        time.sleep(0.4)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)