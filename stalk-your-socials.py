import time

lyrics = [
    "i'll stalk you social 'til my eyes are numb",
    "you don't even know how much i need your heart",
    "i'll see all your repost and what's on your mind",
    "because i cannot date you,you want another guy",
    "i'll stalk you social 'til my eyes are numb",
    "you don't even know how much i need your heart",
    "i'll see all your repost and what's on your mind",
    "because i cannot date you,you want another guy"

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
        time.sleep(0.5)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)