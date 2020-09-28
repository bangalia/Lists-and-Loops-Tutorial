songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0:2])
print(songs[1:2])

songs[2] = "Say My Name"
print(songs)
songs.extend(["Jolene","Cranes in the Sky","Rainy Saturday"])
print(songs)
del songs[0]
print(songs)

animals = ["dog","chicken","octopus"]
animals.append("hamster")
print(animals[2])
del animals[0]
print(animals)

for i in range(len(animals)):
    print(animals[i])