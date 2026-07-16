import time

lyrics = [
    "sesi potret yg slalu kuu benci",
    "aneh rasanya kau tak disinii",
    "susunan barisannya tak sama lagi",
    "satu dua tigaa",
    "ini nyata kau tlah pergi"
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
        time.sleep(1.9)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)