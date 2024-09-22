import time
import os

manzana = "🍏"
silueta = "🔴"

def drop():
    for i in range(10):
        os.system('cls' if os.name == 'nt' else 'clear')
        for _ in range(i):
            print()
        print(" "*10 + manzana)
        time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Manzana caida B)")
drop()