from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np

root = Tk()
root.title("EDGE Detector")
root.geometry("1350x700+0+0")

def open():
    label.config(text = "You selected : " + var.get())
    label.pack()
    if var.get() == "Image":
        button1 = Button(root,text="Browse a file",command=imagebutton)
        button1.pack()
    if var.get() == "Video":
        button2 = Button(root,text='Browse a file',command=videobutton)
        button2.pack()
    if var.get() == "Webcam":
        button3 = Button(root,text='Start',command=webacambutton)
        button3.pack()

def imagebutton():
    imagefile = filedialog.askopenfilename(initialdir ='/',title='Select A File',filetypes=(("jpeg", "*.jpg",".png"),("All Files","*.*")))
    img = cv2.imread(imagefile,0)
    height,width = img.shape
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
    cv2.imshow('Original', img)
    cv2.waitKey(0)
    cv2.imshow('Sobel X', sobel_x)
    cv2.waitKey(0)
    cv2.imshow('Sobel Y', sobel_y)
    cv2.waitKey(0)
    sobel_OR = cv2.bitwise_or(sobel_x, sobel_y)
    cv2.imshow('sobel_OR', sobel_OR) 
    cv2.waitKey(0)
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    cv2.imshow('Laplacian', laplacian)
    cv2.waitKey(0)
    canny = cv2.Canny(img, 50, 120)
    cv2.imshow('Canny', canny)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def videobutton():
    videofile = filedialog.askopenfilenames(initialdir='/',title='Select A File',filetypes=[("all video format", ".mp4"),("all video format", ".flv"),("all video format", ".avi")])
    video = cv2.VideoCapture(videofile)
    video = cv2.VideoCapture('car.mp4',0) #use this if you get error in above line where we browsing filename in videofile variable
    while True:
        successful_frame_read,frame = video.read()
        cv2.imshow('Original', frame)
        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        cv2.imshow('Laplacian', laplacian)
        cv2.waitKey(0)
        canny = cv2.Canny(frame, 50, 120)
        cv2.imshow('Canny', canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

def webacambutton():
    webcam = cv2.VideoCapture(0,0)
    while True:
        successful_frame_read,frame = webcam.read()
        cv2.imshow('Original', frame)
        laplacian = cv2.Laplacian(frame, cv2.CV_64F)
        cv2.imshow('Laplacian', laplacian)
        cv2.waitKey(0)
        canny = cv2.Canny(frame, 50, 120)
        cv2.imshow('Canny', canny)
        cv2.waitKey(0)
        cv2.destroyAllWindows() 

name = Label(root,text ="CHOOSE ONE")
name.pack()
var = StringVar(root)
var.set("Image")

option = OptionMenu(root, var, "Image", "Video", "Webcam")
option.pack()

button = Button(root, text="Ok",command=open)
button.pack()

label = Label(root,text="You selected")
label.pack()

root.mainloop()

