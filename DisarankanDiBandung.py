import time

lyrics = [
    "Tak hanya sekali ku mearasa mesra",
    "berharap mentari terbit dari barat",
    "kami sudah muak putus asa besar",
    "mimpi tak pernah berjalan lancar",
    "(bajingan,keparat)",
    "baiknya mreka masuk neraka",
    "untungnya ku bertemu dengan mu",
    "di sela sempit hidup ini"
]

def typing_animation(text, delay=0.08):
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