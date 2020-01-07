import string
import random

library=[]
class Generator(object):
    def __init__(self):
        pass

    def name(self):
        
        alphabet=random.choices(string.ascii_uppercase,k=2)
        key="".join(alphabet)
        print(key)
        numbers=random.choices(string.digits,k=3)
        tag="".join(numbers)
        print(tag)
        code=str(key+tag)
        print(code)
        if code not in library:
            library.append(code)
            print(library)
            if code in library:
                run.name()
run=Generator()
while True:
    run.name()
#take two random letters from the string


