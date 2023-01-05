import random
import os


def create_base_file():
    songs = [
        "prayer",
        "one_day",
        "nuria",
        "fall",
        "neon_lights",
        "tricity",
        "fields",
        "iDupted",
    ]
    if not os.path.exists("all_songs.txt"):
        with open("all_songs.txt", "w") as file:
            for song in songs:
                file.write(f"{song} \n")


def load_all_songs():
    with open("all_songs.txt", "r") as file:
        songs = file.readlines()
    return songs


def load_played_songs():
    if not os.path.exists("played_songs.txt"):
        with open("played_songs.txt", "a") as file:
            file.write("")
    with open("played_songs.txt", "r") as file:
        played = file.readlines()
    return played


def update_played(songs):
    with open("played_songs.txt", "a") as file:
        for song in songs:
            file.write(song)


def select_songs(all_songs, played_songs):
    to_play = []
    how_many = int(input("Ile piosenek byczq: "))
    i = 0
    while i < how_many:
        chosen = random.choice(all_songs)
        all_songs.remove(chosen)
        if chosen not in played_songs:
            to_play.append(chosen)
            i += 1
    update_played(to_play)
    print("Dzisiaj łoicie:")
    for s in to_play:
        print(f"{s} \n")


def reset_list():
    with open("played_songs.txt", "w") as file:
        file.write("")


def how_many_songs_left(all_songs, played_songs):
    print(f"Zostało {len(all_songs) - len(played_songs)} piosenek do zagrania")


def main():
    create_base_file()
    all_songs = load_all_songs()
    played_songs = load_played_songs()
    how_many_songs_left(all_songs=all_songs, played_songs=played_songs)
    select_songs(all_songs=all_songs, played_songs=played_songs)


if __name__ == "__main__":
    while True:
        what_to_do = int(
            input("Byczq co robimy?\n 1. Gramy \n 2. Resetujemy listę \n 3. Sramy \n")
        )

        match what_to_do:
            case 1:
                main()
            case 2:
                reset_list()
            case 3:
                exit()
