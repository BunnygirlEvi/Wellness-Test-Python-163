from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("500x600")
root.title("Wellness Test")
root.configure(background="purple")

question1_radiobutton = StringVar(value="0")
question1 = Label(root, text="Do you experience shortness of breath during routine activities?")
question1.place(relx=0.5, rely=0.20, anchor=CENTER)
question1_r1 = Radiobutton(root, text="yes", variable=question1_radiobutton, value="yes", bg="white")
question1_r1.place(relx=0.5, rely=0.25, anchor=CENTER)
question1_r2 = Radiobutton(root, text="no", variable=question1_radiobutton, value="no", bg="white")
question1_r2.place(relx=0.5, rely=0.30, anchor=CENTER)

question2_radiobutton = StringVar(value="0")
question2 = Label(root, text="Do you have swelling in your feet, legs, ankles, or abdomen?")
question2.place(relx=0.5, rely=0.35, anchor=CENTER)
question2_r1 = Radiobutton(root, text="yes", variable=question2_radiobutton, value="yes", bg="white")
question2_r1.place(relx=0.5, rely=0.40, anchor=CENTER)
question2_r2 = Radiobutton(root, text="no", variable=question2_radiobutton, value="no", bg="white")
question2_r2.place(relx=0.5, rely=0.45, anchor=CENTER)

question3_radiobutton = StringVar(value="0")
question3 = Label(root, text="Do you ever feel confused, disoriented, or have a loss of memory?")
question3.place(relx=0.5, rely=0.50, anchor=CENTER)
question3_r1 = Radiobutton(root, text="yes", variable=question3_radiobutton, value="yes", bg="white")
question3_r1.place(relx=0.5, rely=0.55, anchor=CENTER)
question3_r2 = Radiobutton(root, text="no", variable=question3_radiobutton, value="no", bg="white")
question3_r2.place(relx=0.5, rely=0.60, anchor=CENTER)

question4_radiobutton = StringVar(value="0")
question4 = Label(root, text="Do you experience shortness of breath when lying down/resting?")
question4.place(relx=0.5, rely=0.65, anchor=CENTER)
question4_r1 = Radiobutton(root, text="yes", variable=question4_radiobutton, value="yes", bg="white")
question4_r1.place(relx=0.5, rely=0.70, anchor=CENTER)
question4_r2 = Radiobutton(root, text="no", variable=question4_radiobutton, value="no", bg="white")
question4_r2.place(relx=0.5, rely=0.75, anchor=CENTER)

question5_radiobutton = StringVar(value="0")
question5 = Label(root, text="Do you have persistent fits of coughing/wheezing?")
question5_r1 = Radiobutton(root, text="yes", variable=question5_radiobutton, value="yes", bg="white")
question5.place(relx=0.5, rely=0.80, anchor=CENTER)
question5_r1.place(relx=0.5, rely=0.85, anchor=CENTER)
question5_r2 = Radiobutton(root, text="no", variable=question5_radiobutton, value="no", bg="white")
question5_r2.place(relx=0.5, rely=0.90, anchor=CENTER)


def wellnessCheck():
    score = 0
    if question1_radiobutton.get() == "yes":
        score = score+1
        print(score)
    if question2_radiobutton.get() == "yes":
        score=score+1
        print(score)
    if question3_radiobutton.get() == "yes":
        score=score+1
        print(score)
    if question4_radiobutton.get() == "yes":
        score = score+1
        print(score)
    if question5_radiobutton.get() == "yes":
        score=score+1
        print(score)
    if score < 2 and score > 0:
        messagebox.showinfo("Report","You probably don't need to visit a doctor.")
    elif score >= 2 and score <= 4:
        messagebox.showinfo("Report", "You might need to visit the doctor.")
    elif score == 5:
        messagebox.showinfo("Report","You should probably visit a doctor.") 
    else:
        messagebox.showinfo("Report","You're either fine, or need to select your options.")
    print(score)


enter_button = Button(root, text = "Enter", command = wellnessCheck)
enter_button.place(relx=0.5, rely= 0.100, anchor=CENTER)

root.mainloop()