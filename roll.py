import random
import os

how_many = int(input("Ile piosenek byczq: "))
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

trained = []
to_train = []

for i in range(how_many):
    chosen = random.choice(songs)
    to_train.append(chosen)
    trained.append(chosen)
    songs.remove(chosen)

print(trained)
print(to_train)
