import time

lyrics = [
    "I miss that kind of misery",
    "The kind where you are nice to me",
    "But only in the evening",
    "So I ask, am I just dreaming?",
    "i love you so much that's it's dripping..dripping from my arms and such",
    "im sorry i know im to much to love to trust to nothing but",
    "i miss that kind of misery",
    "The kind where you are nice to me",
    "But only in the evening",
    "So I ask, am I just dreaming?",
    
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
