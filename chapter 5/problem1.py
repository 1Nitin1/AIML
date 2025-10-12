dict = {"namaste":"hello",
        "shukriya":"thank you",
        "aap kaise hain":"how are you",}
s = input("Enter a hindi word: ")
print(dict.get(s,"not found")) #if key not found, it will return "not