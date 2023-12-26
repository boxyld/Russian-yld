#!/usr/bin/env python3

import random
import tkinter as tk
import os

class Roulette:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x200")
        self.root.title("روليت يلد")

        self.label = tk.Label(self.root, text="ﺪﻠﻳ ﺖﻴﻟﻭﺭ ﻲﻓ ﻚﺑ ﺎﺒﺣﺮﻣ")
        self.label.pack()

        self.spin_button = tk.Button(self.root, text="ﻂﻐﻇﺍ", command=self.spin)
        self.spin_button.pack()

        self.chamber_number = random.randint(0, 6)

    def spin(self):
        self.chamber_number += 1

        if self.chamber_number >= 6:
            self.label.config(text="GG")
            os.system("poweroff")
        else:
            self.label.config(text="ﺪﻌﺑ ﺖﻤﺗ ﻢﻟ")


    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    roulette = Roulette()
    roulette.start()
