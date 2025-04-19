import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
#sample dictionary(which can be extended with more words and meanings)
dictionary = {
"A&M": "\n -engineering \n-business \n -agricultural and veterinary sciences \n",
"Rice": "\n -computer and information sciences, general (13%) \n -biology/ biological sciences, general (6%) \n -economics, general (6%)",
"UT Austin": "\n -engineeerng (14%) \n -business, management, marketing, and related support services (12%) \n -biological and biomedical sciences (11%)",
"Baylor": "\n -registered nurisng/ registered nurse (11%) \n -biology/ biological sciences, general (7%) \n -marketing/ marketing managememt, general (6%)"}

#function to search for word meaning
def search_word():
    "A&M" == entry.get().lower() #Convert input to lowercase
    meaning = dictionary.get("A&M") #Search for the word in the dictionary
def search_word():
    "Rice" == entry.get().lower()
    meaning = dictionary.get("Rice")
def search_word():
    "UT Austin" == entry.get().lower()
    meaning = dictionary.get("UT Austin")
def search_word():
    "Baylor" == entry.get().lower()
    meaning = dictionary.get("Baylor")

    if meaning:
        result_label.config(text=f"top 3 majors are : {meaning}") #display the meaning 
    else:
        result_label.config(text="Word not found in the dictionary.")
#if word doesn't exist
#initialize the main window
root = tk.Tk()
root.title("tx uni's majors")
root.geometry("400x300")
#set the window size
#title label
title_label = tk.Label(root, text="best majors in tx universities", font=("Helvetica", 16))
title_label.pack(pady=20)

#Entry widget for user input (word search)
entry = tk.Entry(root, font = ("Helvetica", 14), width=20)
entry.pack(pady=10)

#button to search the word
search_button = tk.Button(root, text="Search", fg= "green", bg = "pink", font=("Helvetica", 14), command=search_word)
search_button.pack(pady=5)

#Label to show the result(Meaning of the word)
result_label = tk.Label(root, text = "Enter a university to search", fg= "blue", font = ("Helvetica", 12),wraplength=300)
result_label.pack(pady=10)







photo_image = ImageTk.PhotoImage
#Start the GUI loop
root.mainloop()