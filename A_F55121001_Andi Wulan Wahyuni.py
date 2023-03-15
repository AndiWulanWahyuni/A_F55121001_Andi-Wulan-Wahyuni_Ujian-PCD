import tkinter as tk
import cv2
import numpy as np
from tkinter import filedialog

root = tk.Tk()
root.title("Aplikasi Perbaikan Citra")

def open_image():
    global img_path
    img_path = filedialog.askopenfilename(initialdir="/", title="Pilih Citra", filetypes=(("Image Files", ".jpeg;.png"),))
    img = cv2.imread(img_path)
    img = cv2.resize(img, (400, 450))
    cv2.imshow("Citra Asli", img)

def show_image(img):
    cv2.imshow("Citra Hasil Perbaikan", img)

def gaussian_filter():
    img = cv2.imread(img_path)
    img = cv2.resize(img, (400, 450))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 0)
    show_image(img)

def sobel_edge_detection():
    img = cv2.imread(img_path)
    img = cv2.resize(img, (400, 450))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    img = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
    img = np.uint8(img)
    show_image(img)

btn_open = tk.Button(root, text="Buka Citra", command=open_image)
btn_open.pack(padx=10, pady=10)

btn_gaussian = tk.Button(root, text="Filter Gaussian", command=gaussian_filter)
btn_gaussian.pack(padx=10, pady=10)

btn_sobel = tk.Button(root, text="Deteksi Tepi Sobel", command=sobel_edge_detection)
btn_sobel.pack(padx=10, pady=10)

root.mainloop()