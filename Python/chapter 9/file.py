f = open("Python/chapter 9/sample.txt", "a")
f.write("lorem ipsum dolor sit amet, consectetur adipiscing elit.lorem ipsum dolor sit amet, consectetur adipiscing elit.")
f.close()
with open("Python/chapter 9/sample.txt", "r") as f:
    content = f.read()
    print(content)