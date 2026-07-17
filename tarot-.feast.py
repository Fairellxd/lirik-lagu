import time

lyrics = [
    "namun aku bingung kenapa ku tak pergi",
    "aku bingung kalian masih di sini",
    "apa mungkin karna terlalu lama",
    "apa benar tuk berbagi derita",
    "mungkin nanti semua justru memburuk",
    "hati hati namun terjatuh lagi",
    "tapi luka adalah niscaya",
    "kutanggung bebanmu",
    "slama ku mampu"
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
        time.sleep(0.04)
    print("")

if __name__ == "__main__":
    show_lyrics(lyrics)
