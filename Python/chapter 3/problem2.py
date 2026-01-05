letter = '''
Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''
name = input("Enter your name: ")
date = input("Enter date: ")
letter1 = letter.replace("<|NAME|>", name)
letter2 = letter1.replace("<|DATE|>", date)
print(letter2)
#or can chain the replace function as