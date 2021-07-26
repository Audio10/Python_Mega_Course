"Context manager open doesn't need to use close()"

with open("files/fruits.txt") as myfile:
    content = myfile.read()

print(content)