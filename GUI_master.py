import tkinter as tk
from tkinter import ttk, LEFT, END
import warnings
warnings.filterwarnings('ignore') # suppress import warnings
from PIL import Image , ImageTk 
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
import time
import tfModel_CPU 
import tfModel_test as tf_test
global fn
fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Diabetic Retinopathy Detection System")


#430
lbl = tk.Label(root, text="Diabetic Retinopathy Detection System", font=('times', 35,' bold '), height=1, width=30,bg="seashell2",fg="indian red")
lbl.place(x=430, y=5)
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('Diabetic_Retinopathy.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#

frame_display = tk.LabelFrame(root, text=" --Display-- ", width=850, height=300, bd=5, font=('times', 10, ' bold '),bg="DarkGoldenrod1")
frame_display.grid(row=0, column=0, sticky='nw')
frame_display.place(x=5, y=400)



frame_alpr = tk.LabelFrame(root, text=" --Process-- ", width=880, height=120, bd=5, font=('times', 10, ' bold '),bg="gold")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=5, y=600)


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% 
def clear_img():
    
    img11 = tk.Label(frame_display, background='DarkGoldenrod1',width=160,height=120)
    img11.place(x=0, y=0)

def update_label(str_T):
    clear_img()
    result_label = tk.Label(frame_display, text=str_T, width=50, font=("bold", 25),bg='DarkGoldenrod1',fg='black' )
    result_label.place(x=0, y=0)

def train_model():
    
    update_label("Model Training Start...............")
    
    start = time.time()

    X=tfModel_CPU.main()
    
    end = time.time()
        
    ET="Execution Time: {0:.4} seconds \n".format(end-start)
    
    msg="Model Training Completed.."+'\n'+ X + '\n'+ ET

    update_label(msg)

def test_model():
    global fn
    if fn!="":
        update_label("Model Testing Start...............")
        
        start = time.time()
    
        X=tf_test.analysis(fn)
        X1="Selected Image is {0}".format(X)
        end = time.time()
            
        ET="Execution Time: {0:.4} seconds \n".format(end-start)
        
        msg="Image Testing Completed.."+'\n'+ X1 + '\n'+ ET
        fn=""
    else:
        msg="Please Select Image For Prediction...."
        
    update_label(msg)
    
    
def openimage():
   
    global fn
    clear_img()
    fileName = askopenfilename(initialdir='/demo', title='Select image for Aanalysis ',
                               filetypes=[("all files", "*.*")])
    IMAGE_SIZE=300
    imgpath = fileName
    fn = fileName
    
    if fn!="":
    
    #        img = Image.open(imgpath).convert("L")
        img = Image.open(imgpath)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
    #        img = img / 255.0```
    #        img = img.reshape(1,IMAGE_SIZE,IMAGE_SIZE,3)
    
    
        x1 = int(img.shape[0])
        y1 = int(img.shape[1])
    
    
    
    #        gs = cv2.cvtColor(cv2.imread(imgpath, 1), cv2.COLOR_RGB2GRAY)
    #
    #        gs = cv2.resize(gs, (x1, y1))
    #
    #        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        img = tk.Label(frame_display, image=imgtk, height=x1-50, width=y1-50)
        img.image = imgtk
        img.place(x=0, y=0)
    #        out_label.config(text=imgpath)
    else:
        msg="Please Select Image ..........."    
        update_label(msg)
    
def convert_grey():
    global fn    
    if fn !="":
        IMAGE_SIZE=300
        
        img = Image.open(fn)
        img = img.resize((IMAGE_SIZE,IMAGE_SIZE))
        img = np.array(img)
        
        x1 = int(img.shape[0])
        y1 = int(img.shape[1])
    
        gs = cv2.cvtColor(cv2.imread(fn, 1), cv2.COLOR_RGB2GRAY)
    
        gs = cv2.resize(gs, (x1, y1))
    
        retval, threshold = cv2.threshold(gs, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    
    
        im = Image.fromarray(gs)
        imgtk = ImageTk.PhotoImage(image=im)
        
        img2 = tk.Label(frame_display, image=imgtk, height=x1-50, width=y1-50)
        img2.image = imgtk
        img2.place(x=280, y=0)
    
        im = Image.fromarray(threshold)
        imgtk = ImageTk.PhotoImage(image=im)
    
        img3 = tk.Label(frame_display, image=imgtk, height=x1-50, width=y1-50)
        img3.image = imgtk
        img3.place(x=580, y=0)

    else:
        
        msg="Please Select Image ..........."    
        update_label(msg)































#################################################################################################################
def window():
    root.destroy()




button1 = tk.Button(frame_alpr, text=" Select Image ", command=openimage,width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button1.place(x=0, y=20)

button2 = tk.Button(frame_alpr, text="Image Process", command=convert_grey, width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button2.place(x=160, y=20)

button3 = tk.Button(frame_alpr, text="Train Model", command=train_model, width=12, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
button3.place(x=320, y=20)
#
button4 = tk.Button(frame_alpr, text="Prediction", command=test_model,width=12, height=1,bg="yellow4",fg="white", font=('times', 15, ' bold '))
button4.place(x=480, y=20)
#
#
#button5 = tk.Button(frame_alpr, text="button5", command=window,width=8, height=1, font=('times', 15, ' bold '),bg="yellow4",fg="white")
#button5.place(x=450, y=20)


exit = tk.Button(frame_alpr, text="Exit", command=window, width=10, height=1, font=('times', 15, ' bold '),bg="red",fg="white")
exit.place(x=710, y=20)



root.mainloop()