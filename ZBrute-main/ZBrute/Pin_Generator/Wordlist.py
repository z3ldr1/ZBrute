with open("passwords.txt", "w") as file:
    for i in range(10000):
        sequence = str(i).zfill(4)
        file.write(sequence + "\n")