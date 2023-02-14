import pandas as pd
import string
import numpy as np
import random
def data (index):
    df = pd.read_csv("data_sets/data_hack.csv")
    random_ips = ["5LVD3AJKM3ZL","sdlaoo5dsf","3GWN3EWF516F","GPXXM9LMT5EL","sdlaoo5dsf"]

    #index = random.randint(0, len(random_ips)-1)
    card_id =random_ips[index]
    try:
        client_balance = df[df["Card_ID"] == card_id].balance.values[0]
        client_data = df[df["Card_ID"] == card_id]
    except:
        client_balance = -10

    fees_of_passing=25

    if (client_balance > 0 and client_balance > fees_of_passing):
        df.loc[client_data.index.values[0], "balance"] -= fees_of_passing

        return df[df['Card_ID'] == card_id].names.values[0], df[df['Card_ID'] == card_id].balance.values[0] , df[df['Card_ID'] == card_id].voiltaion_should_paid.values[0],df[df['Card_ID'] == card_id].Card_ID.values[0]

    elif (client_balance >= 0 and client_balance <= fees_of_passing):
        df.loc[client_data.index.values[0], "balance"] -= 1.25 * fees_of_passing
        return df[df['Card_ID'] == card_id].names.values[0], df[df['Card_ID'] == card_id].balance.values[0], df[df['Card_ID'] == card_id].voiltaion_should_paid.values[0],df[df['Card_ID'] == card_id].Card_ID.values[0]
    elif client_balance == -10:
       return None
def gui (name, balance, voiltaion, card_ID):
    import tkinter as tk
    from tkinter import ttk
    import time
    from tkinter import messagebox
    from PIL import Image, ImageTk

    root = tk.Tk()
    root.title("Government Information")
    root.geometry("1080x600")

    # Font for the labels
    label_font = ("Times New Roman", 20)

    # Load logos
    logo_left = Image.open("Images/LEFT.png")
    logo_left = logo_left.resize((100, 100), Image.ANTIALIAS)
    logo_left = ImageTk.PhotoImage(logo_left)

    logo_right = Image.open("Images/RIGHT.png")
    logo_right = logo_right.resize((120, 120), Image.ANTIALIAS)
    logo_right = ImageTk.PhotoImage(logo_right)

    # Left logo
    left_logo = tk.Label(root, image=logo_left)
    left_logo.place(x=10, y=10)

    # Right logo
    right_logo = tk.Label(root, image=logo_right)
    right_logo.place(x=950, y=8)

    # Labels
    frame_1 = tk.Frame(root, bd=2, relief="solid")
    frame_1.pack(padx=30, pady=30)

    name_label_1 = tk.Label(frame_1, text="Name:", font=label_font, width=15, anchor="w")
    data_label_1 = tk.Label(frame_1, text=str(name), font=label_font, width=20, anchor="w")
    name_label_1.pack(side="left", padx=5)
    data_label_1.pack(side="left", padx=5)

    frame_2 = tk.Frame(root, bd=2, relief="solid")
    frame_2.pack(padx=30, pady=30)

    name_label_2 = tk.Label(frame_2, text="toll station:", font=label_font, width=15, anchor="w")
    data_label_2 = tk.Label(frame_2, text="Benha", font=label_font, width=20, anchor="w")
    name_label_2.pack(side="left", padx=5)
    data_label_2.pack(side="left", padx=5)

    frame_3 = tk.Frame(root, bd=2, relief="solid")
    frame_3.pack(padx=30, pady=30)

    name_label_3 = tk.Label(frame_3, text="Current Balance:", font=label_font, width=15, anchor="w")
    data_label_3 = tk.Label(frame_3, text=str(balance)+" EGP", font=label_font, width=20, anchor="w")
    name_label_3.pack(side="left", padx=5)
    data_label_3.pack(side="left", padx=5)

    frame_4 = tk.Frame(root, bd=2, relief="solid")
    frame_4.pack(padx=30, pady=30)

    name_label_4 = tk.Label(frame_4, text="Fees of passing :", font=label_font, width=15, anchor="w")
    data_label_4 = tk.Label(frame_4, text=str(25)+" EGP", font=label_font, width=20, anchor="w")

    name_label_4.pack(side="left", padx=5)
    data_label_4.pack(side="left", padx=5)


    frame_5 = tk.Frame(root, bd=2, relief="solid")
    frame_5.pack(padx=30, pady=30)

    name_label_5 = tk.Label(frame_5, text="Violation on you :", font=label_font, width=15, anchor="w")
    data_label_5 = tk.Label(frame_5, text=str(voiltaion)+" EGP", font=label_font, width=20, anchor="w")
    name_label_5.pack(side="left", padx=5)
    data_label_5.pack(side="left", padx=5)

    # Check balance and display message box if necessary
    if balance == None:
        messagebox.showerror("Warning", " yours card isn't vaild , please wait the support ")
        name_label_1.pack_forget()
        data_label_1.pack_forget()
        name_label_2.pack_forget()
        data_label_2.pack_forget()
    elif balance <= 0:
        messagebox.showwarning("Warning", "Your balance is zero. Please recharge.")
    """"elif balance < 0:
        messagebox.showerror("Error", "Your balance is negative.")"""

    # function to submit the text
    def submit_text(text_field):
        text = text_field.get()
        text_df.loc[len(text_df) + 1] = [name, card_ID, text]
        text_df.to_csv("data_sets/user_text.csv", index=False)
        text_field.delete(0, 'end')

    # creating the label
    label = tk.Label(root, text="Please Write any complament you want")
    label.pack()
    #  the text field
    text_field = tk.Entry(root)
    text_field.pack()
    #  the submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: submit_text(text_field))
    submit_button.pack()

    # DataFrame to store the input text
    text_df = pd.read_csv("user_text.csv")

    # time
    def show_time():
        current_time = time.strftime("%I:%M:%S %p")
        current_date = time.strftime("%d-%m-%Y")
        time_date_label.config(text=current_date + "\n" + current_time)
        root.after(1000, show_time)

    time_date_label = ttk.Label(root, text="", font=("TkDefaultFont", 24))
    time_date_label.place(x=25, y=200)

    show_time()

    root.mainloop()

if __name__ == "__main__":
    x=0
    while x<3:
        returnend_data = data(x)

        if returnend_data != None:
            name, balance, voiltaion, card_ID = returnend_data[0], returnend_data[1], returnend_data[2], returnend_data[3]
        else:
            name, balance, voiltaion, card_ID = None, None, None, None
        gui(name, balance, voiltaion, card_ID)
        x+=1





