import time

lyrics = [
    "light blue eyes didn,t show surprise",
    "when i explained the fact that im...satisfied",
    "the butterflies moving in my tummy",
    "float arround and make me feel really funny",
    "you dissagree with my self-esteem",
    "did i mention you were in my dreams",
    "we could walk in the ceiling",
    "and we thougt that nothing would go wrong....."

]
def typing_animation(text, delay=0.07):
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