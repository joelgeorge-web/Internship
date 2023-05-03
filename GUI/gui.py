import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x450")

def button_function():
    print("Menu Edited")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Edit Menu", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
app.mainloop()

