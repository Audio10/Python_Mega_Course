"Context manager open doesn't need to use close()"

with open("files/vegetables.txt", "w") as myfile:
    myfile.write("Tomato")
