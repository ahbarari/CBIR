from tkinter import *
import numpy as np
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
import cv2
from descriptor import ColorDescriptor
from searcher import Searcher


def is_similar(image1, image2):
    return image1.shape == image2.shape and not(np.bitwise_xor(image1, image2).any())


def select_image():
    top_left = Frame(root, bg='black', width=200, height=200)
    top_middle = Frame(root, bg='green', width=200, height=200)
    top_right = Frame(root, bg="green", width=200, height=200)
    middle_left = Frame(root, bg='green', width=200, height=200)
    middle = Frame(root, bg='green', width=200, height=200)
    middle_right = Frame(root, bg='green', width=200, height=200)
    bottom_left = Frame(root, bg='green', width=200, height=200)
    bottom_middle = Frame(root, bg='green', width=200, height=200)
    bottom_right = Frame(root, bg='green', width=200, height=200)

    top_left.grid(row=1, column=0, padx=5, pady=5)
    top_middle.grid(row=1, column=1, padx=5, pady=5)
    top_right.grid(row=1, column=2, padx=5, pady=5)
    middle_left.grid(row=2, column=0, padx=5, pady=5)
    middle.grid(row=2, column=1, padx=5, pady=5)
    middle_right.grid(row=2, column=2, padx=5, pady=5)
    bottom_left.grid(row=3, column=0, padx=5, pady=5)
    bottom_middle.grid(row=3, column=1, padx=5, pady=5)
    bottom_right.grid(row=3, column=2, padx=5, pady=5)

    path = filedialog.askopenfilename()

    if len(path) > 0:
        cd = ColorDescriptor((4, 4, 4), (8, 12, 3))
        query = cv2.imread(path)
        image = cv2.cvtColor(query, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image.resize((200, 200)))
        label = Label(top_left, image=image, bg='red')
        label.image = image
        label.pack()
        features = cd.describe(query)
        searcher = Searcher("features.csv")
        results = searcher.search(features)
        i = 0
        for (score, resultID) in results:
            result = cv2.imread(resultID)
            if is_similar(query, result):
                pass
            else:
                if i == 0:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(top_middle, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 1:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(top_right, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 2:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(middle_left, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 3:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(middle, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 4:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(middle_right, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 5:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(bottom_left, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 6:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(bottom_middle, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                elif i == 7:
                    res = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
                    res = Image.fromarray(res)
                    res = ImageTk.PhotoImage(res.resize((200, 200)))
                    lbl = Label(bottom_right, image=res, bg='green')
                    lbl.image = res
                    lbl.pack()
                i += 1


root = Tk()
root.title("CBIR")
root.geometry("700x700")
root.resizable(width=True, height=True)
btn_img = Button(root, text="Select an image", command=select_image, bd=0, height=2, bg='orange',
                 activebackground='orange').grid(row=0, columnspan=3, pady=10, sticky='nsew', padx=10)

root.mainloop()
