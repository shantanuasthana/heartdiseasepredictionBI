
import os
import tkinter as tk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import ttk
import numpy as np


os_name = os.name


bg_color = "#E8E8E8"

art = "           ________   Enter patient data                 \n          |           |  /   or try with a test patient        \n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"

if os_name == "nt": #windows
    bg_color = "#F0F0F0"
    art = "          _______ _   Enter patient data             \n           |            |  /   or try with a test patient        \n           |   |    |  |\n           |            |\n           |___  _ __|\n         ____|  |____\n \n"
elif os_name == "posix": #OS X
    bg_color = "#E8E8E8"
    art = "           ________   Enter patient data                 \n          |           |  /   or try with a test patient\n          |   |    |  |\n          |           |\n          |___  ___|\n         ____|  |____\n \n"




class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                         background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                         font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

            

def createToolTip(widget, text):
    toolTip = ToolTip(widget)

    def enter(event):
        toolTip.showtip(text)

    def leave(event):
        toolTip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)



win = tk.Tk()
win.columnconfigure(0, weight=1)


win.title("Heart Disease Prediction")




tabControl = ttk.Notebook(win)

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Heart AI')

tabControl.pack(expand=1, fill="both") 
# ---------------Heart GUI Start------------------#
monty3 = ttk.LabelFrame(tab3, text="Data measured on a patient")
monty3.grid(column=0, row=0, padx=10, pady=0)


labelText1 = tk.StringVar()
labelText1.set("Age :")
ttk.Label(monty3, width=16, textvariable=labelText1, justify='left').grid(column=0, row=0)

age = tk.DoubleVar()
tk.Entry(monty3, textvariable=age, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=0, sticky='NW')

labelUnit1 = tk.Label(monty3, text="ans", anchor='w', width=8, justify='right', background=bg_color)
labelUnit1.grid(column=1, row=0)

ttk.Label(monty3, textvariable=labelUnit1, justify='right').grid(column=1, row=0)
ttk.Separator(monty3, orient='horizontal').grid(row=1, columnspan=3, sticky="ew")

labelText2 = tk.StringVar()
labelText2.set("Gender :")
ttk.Label(monty3, width=16, textvariable=labelText2, justify='left').grid(column=0, row=2)

sex = tk.StringVar()
sex.set('0.0')
tk.Radiobutton(monty3, text="Female", variable=sex, value='0.0', width=12, justify='left', background=bg_color).grid(
    column=1, row=2, sticky='W')
tk.Radiobutton(monty3, text="Male", variable=sex, value='1.0', width=12, justify='left', background=bg_color).grid(
    column=2, row=2, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=3, columnspan=3, sticky="ew")


labelText3 = tk.StringVar()
labelText3.set("Type of chest pain \n")
ttk.Label(monty3, width=16, textvariable=labelText3, justify='left').grid(column=0, row=4, rowspan=2)

chestPain = tk.StringVar()
chestPain.set('1.0')
tk.Radiobutton(monty3, text="Typical angina", variable=chestPain, value='3', justify='left',
               background=bg_color).grid(column=1, row=4, sticky='W')
tk.Radiobutton(monty3, text="Atypical angina", variable=chestPain, value='1', justify='left',
               background=bg_color).grid(column=2, row=4, sticky='W')
tk.Radiobutton(monty3, text="Non-anginal Pain", variable=chestPain, value='2', justify='left',
               background=bg_color).grid(column=1, row=5, sticky='NW')
tk.Radiobutton(monty3, text="Asymptomatic", variable=chestPain, value='0', justify='left',
               background=bg_color).grid(column=2, row=5, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=5, columnspan=3, sticky="ews")


labelText4 = tk.StringVar()
labelText4.set("Blood Pressure :")
ttk.Label(monty3, width=16, textvariable=labelText4, justify='left').grid(column=0, row=6)

pression_sang = tk.DoubleVar()
tk.Entry(monty3, textvariable=pression_sang, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=6, sticky='NW')

labelUnit4 = tk.Label(monty3, text="mmHg", anchor='w', width=8, justify='right', background=bg_color)
labelUnit4.grid(column=1, row=6)

ttk.Separator(monty3, orient='horizontal').grid(row=7, columnspan=3, sticky="ew")


labelText5 = tk.StringVar()
labelText5.set("Serum cholesterol :")
ttk.Label(monty3, textvariable=labelText5, justify='left').grid(column=0, row=8)

chol_sterique = tk.DoubleVar()
tk.Entry(monty3, textvariable=chol_sterique, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=8, sticky='NW')

labelUnit5 = tk.Label(monty3, text="mg/dL", anchor='w', width=8, justify='right', background=bg_color)
labelUnit5.grid(column=1, row=8)

ttk.Separator(monty3, orient='horizontal').grid(row=9, columnspan=3, sticky="ew")


labelText6 = tk.StringVar()
labelText6.set("Fasting blood sugar :")
ttk.Label(monty3, width=16, textvariable=labelText6, justify='left').grid(column=0, row=10)

glycemie = tk.DoubleVar()

tk.Radiobutton(monty3, text="> 120 mg/dL", variable=glycemie, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=10, sticky='NW')
tk.Radiobutton(monty3, text="< 120 mg/dL", variable=glycemie, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=10, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=11, columnspan=3, sticky="ew")

labelText7 = tk.StringVar()
labelText7.set("Resting ECG:")
ttk.Label(monty3, width=16, textvariable=labelText7, justify='left').grid(column=0, row=12)

ecgresult = tk.StringVar()
ecgresult.set('0.0')
tk.Radiobutton(monty3, text="Normal", variable=ecgresult, value='2', justify='left', background=bg_color).grid(
    column=1, row=12, sticky='NW')

tk.Radiobutton(monty3, text="Abnormal ST-T wave (inversion of the T wave and \ or \n ST segment shift> 0.05 mV)", variable=ecgresult, value='0', justify='left',
               background=bg_color).grid(column=1, row=13, sticky='NW', columnspan=2)
tk.Radiobutton(monty3, text="Probable or confirmed presence \n hypertrophy of the left ventricle ", variable=ecgresult, value='1', justify='left',
               background=bg_color).grid(column=1, row=14, sticky='NW', columnspan=2)

ttk.Separator(monty3, orient='horizontal').grid(row=15, columnspan=3, sticky="ew")


labelText8 = tk.StringVar()
labelText8.set("Maximum Heart Rate")
ttk.Label(monty3, textvariable=labelText8, justify='left').grid(column=0, row=16)

fcm = tk.DoubleVar()
tk.Entry(monty3, textvariable=fcm, width=8, justify='left', highlightbackground=bg_color, background=bg_color).grid(
    column=1, row=16, sticky='NW')

labelUnit8 = tk.Label(monty3, text="bts/min", anchor='w', width=8, justify='right', background=bg_color)
labelUnit8.grid(column=1, row=16)

ttk.Separator(monty3, orient='horizontal').grid(row=17, columnspan=3, sticky="ew")


labelText9 = tk.StringVar()
labelText9.set("Exercise-induced angina:")
ttk.Label(monty3, textvariable=labelText9, justify='left', background=bg_color).grid(column=0, row=18)

exerciseangina = tk.StringVar()
exerciseangina.set("1.0")
tk.Radiobutton(monty3, text="Yes", variable=exerciseangina, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=18, sticky='NW')
tk.Radiobutton(monty3, text="No", variable=exerciseangina, value='0.0', justify='left', background=bg_color).grid(
    column=2, row=18, sticky='NW')

ttk.Separator(monty3, orient='horizontal').grid(row=19, columnspan=3, sticky="ew")


labelText10 = tk.StringVar()
labelText10.set("S-T \n by segment offset:")
ttk.Label(monty3, width=20, textvariable=labelText10, justify='left', background=bg_color).grid(column=0, row=20,
                                                                                                 rowspan=1)

st_depression = tk.DoubleVar()
tk.Entry(monty3, textvariable=st_depression, width=8, justify='left', highlightbackground=bg_color,
         background=bg_color).grid(column=1, row=20, sticky='W')

labelUnit10 = tk.Label(monty3, text="mV", anchor='w', width=8, justify='right', background=bg_color)
labelUnit10.grid(column=1, row=20)

ttk.Separator(monty3, orient='horizontal').grid(row=21, columnspan=3, sticky="ew")


labelText11 = tk.StringVar()
labelText11.set("Slope at the top \n of the S-T segment \n during effort:")
ttk.Label(monty3, textvariable=labelText11, justify='left', background=bg_color).grid(column=0, row=22, rowspan=2)

peakexercise = tk.StringVar()
peakexercise.set('1.0')

tk.Radiobutton(monty3, text="Upsloping", variable=peakexercise, value='2', justify='left',
               background=bg_color).grid(column=1, row=22, sticky='W')
tk.Radiobutton(monty3, text="Flat", variable=peakexercise, value='1', justify='left', background=bg_color).grid(
    column=1, row=23, sticky='W')
tk.Radiobutton(monty3, text="Downsloping", variable=peakexercise, value='0', justify='left',
               background=bg_color).grid(column=1, row=24, sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=25, columnspan=3, sticky="ew")


labelText12 = tk.StringVar()
labelText12.set("Number of \n principal vessels stained by \n fluoroscopy / radioscopy:")
ttk.Label(monty3, textvariable=labelText12, justify='left').grid(column=0, row=26, rowspan =2)
nb_vessels = tk.StringVar()
nb_vessels.set("0.0")
tk.Radiobutton(monty3, text="0", variable=nb_vessels, value='0.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="1", variable=nb_vessels, value='1.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=26,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="2", variable=nb_vessels, value='2.0', justify='left', background=bg_color).grid(column=1,
                                                                                                              row=27,
                                                                                                              sticky='W')
tk.Radiobutton(monty3, text="3", variable=nb_vessels, value='3.0', justify='left', background=bg_color).grid(column=2,
                                                                                                              row=27,
                                                                                                              sticky='W')

ttk.Separator(monty3, orient='horizontal').grid(row=28, columnspan=3, sticky="ew")

labelText13 = tk.StringVar()
labelText13.set("Examination of the heart at Thallasimia :")
ttk.Label(monty3, textvariable=labelText13, justify='left').grid(column=0, row=29)
tha_heartscan = tk.StringVar()
tha_heartscan.set('1.0')
tk.Radiobutton(monty3, text="Normal", variable=tha_heartscan, value='1.0', justify='left', background=bg_color).grid(
    column=1, row=29, sticky='W')
tk.Radiobutton(monty3, text="Reversible malformation", variable=tha_heartscan, value='2.0', justify='left',
               background=bg_color).grid(column=1, row=30, sticky='W')
tk.Radiobutton(monty3, text="Irreversible malformation", variable=tha_heartscan, value='0.0', justify='left',
               background=bg_color).grid(column=1, row=31, sticky='W')

ttk.Separator(monty3, orient='vertical').grid(column=4, rowspan=32, sticky="ns")


def ageProcessor(age):
    age_p = str(age.get())
    return age_p


def pression_sangProcessor(pression_sang):
    pression_sang_p = str(pression_sang.get())
    return pression_sang_p


def chol_steriqueProcessor(chol_sterique):
    chol_sterique_p = str(chol_sterique.get())
    return chol_sterique_p

def glycemieProcessor(glycemie):
    glycemie_p = str(glycemie.get())
    return glycemie_p


def fcmProcessor(fcm):
    fcm_p = str(fcm.get())
    return fcm_p


def st_depressionProcessor(st_depression):
    st_depression_p = str(st_depression.get())
    return st_depression_p


def dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm, exerciseangina,
                     st_depression, peakexercise, nb_vessels, tha_heartscan):

    processed_vars = []
    processed_vars.append(ageProcessor(age))
    processed_vars.append(sex.get())
    processed_vars.append(chestPain.get())
    processed_vars.append(pression_sangProcessor(pression_sang))
    processed_vars.append(chol_steriqueProcessor(chol_sterique))
    processed_vars.append(glycemieProcessor(glycemie))
    processed_vars.append(ecgresult.get())
    processed_vars.append(fcmProcessor(fcm))
    processed_vars.append(exerciseangina.get())
    processed_vars.append(st_depressionProcessor(st_depression))
    processed_vars.append(peakexercise.get())
    processed_vars.append(nb_vessels.get())
    processed_vars.append(tha_heartscan.get())
   
    data_string = ''
    c = 1
    for var in processed_vars:
        if c == 13:
            data_string += var
            print(var)
        else:
            data_string += var + ' '
            c += 1
    print(data_string)
    return np.array([float(ageProcessor(age)),sex.get(),chestPain.get(),float(pression_sangProcessor(pression_sang)),float(chol_steriqueProcessor(chol_sterique)),
                     float(glycemieProcessor(glycemie)),ecgresult.get(),float(fcmProcessor(fcm)),exerciseangina.get(),float(st_depressionProcessor(st_depression)),peakexercise.get(),nb_vessels.get(),tha_heartscan.get()]).reshape(1,-1)




def HeartAIModel(data_string, algo=0):
    "Function that checks the relevance of the data"
    """Cast the form data then
    Calls a prediction algorithm with the data entered and returns its result """
    print(data_string)
    if algo == 0:
        import pickle
        import sklearn
        import sklearn.ensemble
        filename = "finalheart_rfmodel.sav"
        model = pickle.load(open(filename, 'rb'))
        print("datastring is: ",data_string)
        output = model.predict(data_string)
        if output[0]== 0:
            return "High risk"
        elif output[0]== 1:
            return "Mild Risk"
        elif output[0]== 2:
            return "Low or No risk"
        else:
            return "Invalid. Try again"

def predict():
   
    data_string = dataPreprocessor(age, sex, chestPain, pression_sang, chol_sterique, glycemie, ecgresult, fcm, exerciseangina, st_depression, peakexercise, nb_vessels, tha_heartscan)
    output = HeartAIModel(data_string)
    print(output)
    mBox.showinfo("Result of prediction", output)


labelText15 = tk.StringVar()
labelText15.set("Prediction of the result:")
text15 = ttk.Label(monty3, width=25, textvariable=labelText15, background=bg_color, anchor='center')
text15.grid(column=6, row=5, sticky="EW", columnspan=4)

s = ttk.Style().configure("cta.TButton", foreground='#562742', font=('Sans', '12', 'bold'))
action3 = ttk.Button(monty3, text="Attempt the prediction", width=40, command=predict, style="cta.TButton")
action3.grid(column=6, row=6, rowspan=1, columnspan=4, sticky="EW")

# prediction = tk.StringVar()
# prediction.set(art)
# text16 = ttk.Label(monty3, width=40, textvariable=prediction, background=bg_color, anchor='w', justify='left')
# text16.grid(column=6, row=7, sticky="EW", columnspan=4, rowspan=7)


# ---------------Example 3 End------------------#


# ----------------menu-------------------#
# Exit GUI
def _quit():
    win.quit()
    win.destroy()
    exit()


# creation menubar
menuBar = Menu(win)
win.config(menu=menuBar)

# add items to a menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Create")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)


# Show message
def _msgBox1():
    mBox.showinfo('Python Message Info Box', 'Program:')


def _msgBox2():
    mBox.showwarning('Python Message Warning Box', 'Alert:')


def _msgBox3():
    mBox.showwarning('Python Message Error Box', 'Error')



# Add another menu


msgMenu = Menu(menuBar, tearoff=0)
msgMenu.add_command(label="notification Box", command=_msgBox1)
msgMenu.add_command(label="warning Box", command=_msgBox2)
msgMenu.add_command(label="error Box", command=_msgBox3)
menuBar.add_cascade(label="message", menu=msgMenu)


# ======================
# Start GUI  
# ======================
win.mainloop()  
