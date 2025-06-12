import time
import os
from termcolor import colored, cprint

def animasi_bendera(lebar, tinggi):
    for gerak in range(30):
        os.system("cls")

        for i in range(tinggi // 2):
            maju_mundur = " " * ((gerak + i * 2) % 6)
            cprint(maju_mundur + " " * lebar, "white", "on_red")

        for i in range(tinggi // 2):
            maju_mundur = " " * ((gerak + i * 2) % 6)
            cprint(maju_mundur + " " * lebar, "white", "on_white")

        for i in range(10):
            cprint("||", "grey", "on_blue")

        time.sleep(0.2)

animasi_bendera(15,6)



