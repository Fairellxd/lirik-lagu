import time

lyrics = [
    "Now really,how you smile makes me melt",
    "But you're so cold,you never listen",
    "Always ignore me,leaving the blue",
    "Oh,What can i do to get you to love me",
    "you're so damn perfect,i don't wanna lose",
    "You my mystery girl(you my mystery my mystery)",

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
        time.sleep(1.0)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)