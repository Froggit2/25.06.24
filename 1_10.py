import time
from threading import Thread
from time import sleep


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
def numb():
    for num in range(10):
        num += 1
        print(num)
        time.sleep(1)


def lett():
    for let in letters:
        print(let)
        time.sleep(0.999)


number = Thread(target=numb)
letter = Thread(target=lett)

number.start()
letter.start()

number.join()
letter.join()