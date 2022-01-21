import tkinter as tk           #importing necessary modules
import random as r

class Rolling():
    def __init__(self, root):
        self.root = root
        l1 = tk.Label(self.root, text='Rolling Dice', font="arial 40 bold", bg='gray',width=50).pack()
        self.b1 = tk.Button(self.root, text="Let's start", font="arial 30 ", bg='green', command=self.roll)  #for command we can make the button funcional
        self.b1.pack(pady=50)
    def roll(self):
        self.num = r.randrange(0, 6)
        self.b1.forget()
        self.image()
        self.b1 = tk.Button(self.root, image=self.p1, command=self.roll)
        self.b1.pack(pady=50)
    def image(self):
        img =['dice1.png', 'dice2.png', 'dice3.png', 'dice4.png', 'dice5.png', 'dice5.png', 'dice6.png']
        self.p1 = tk.PhotoImage(file=img[self.num])
        #print(img[self].num)
root =tk.Tk()
root.title('Rolling Dice')
root.geometry('450x450')
run = Rolling(root)
root.mainloop()