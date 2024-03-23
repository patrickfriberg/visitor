import tkinter as tk
import os
from openpyxl import Workbook, load_workbook
from tkinter import messagebox

class MainApp:
    def __init__(self, master):
        self.master = master
        master.title("BRI 0.5")
        master.geometry("500x500")

        self.background_color = "#f0f0f0"
        self.button_color = "#4caf50"
        self.text_color = "#000000"

        self.master.configure(bg=self.background_color)

        # Get the directory of the Python script
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Construct the path to the logo image file
        logo_path = os.path.join(script_dir, "logo.png")

        # Load the logo image
        self.logo = tk.PhotoImage(file=logo_path)

        # Place logo in the lower right corner
        self.logo_label = tk.Label(master, image=self.logo, bg=self.background_color)
        self.logo_label.place(relx=1.0, rely=1.0, anchor="se")

        # Menu buttons
        self.register_button = tk.Button(master, text="Registrera användare", bg=self.button_color, fg=self.text_color,
                                         command=self.open_registration_window)
        self.register_button.place(relx=0.5, rely=0.3, anchor="center", width=200)

        self.log_button = tk.Button(master, text="Logga besök", bg=self.button_color, fg=self.text_color,
                                    command=self.open_logging_window)
        self.log_button.place(relx=0.5, rely=0.7, anchor="center", width=200)

    def open_registration_window(self):
        registration_window = tk.Toplevel(self.master)
        registration_window.title("Registrera användare")
        registration_window.geometry("200x200")
        registration_window.configure(bg=self.background_color)
        registration_window.grab_set()  # Make this window modal
        registration_window.focus_set()  # Focus on this window

        UserRegistrationApp(registration_window)

    def open_logging_window(self):
        logging_window = tk.Toplevel(self.master)
        logging_window.title("Logga besök")
        logging_window.geometry("200x200")
        logging_window.configure(bg=self.background_color)
        logging_window.grab_set()  # Make this window modal
        logging_window.focus_set()  # Focus on this window

        DataLoggingApp(logging_window)


class UserRegistrationApp:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.configure(bg="#f0f0f0")

        # Load the logo image
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
        self.logo = tk.PhotoImage(file=logo_path)

        # Display the logo
        self.logo_label = tk.Label(master, image=self.logo, bg="#f0f0f0")
        self.logo_label.grid(row=0, columnspan=2)

        # Label and Entry for username
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=1, column=0, sticky="e")
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=1, column=1)

        # Label and Entry for year of birth
        self.year_label = tk.Label(master, text="Födelseår:")
        self.year_label.grid(row=2, column=0, sticky="e")
        self.year_entry = tk.Entry(master)
        self.year_entry.grid(row=2, column=1)

        # Label and Entry for sex
        self.sex_label = tk.Label(master, text="Kön:")
        self.sex_label.grid(row=3, column=0, sticky="e")
        self.sex_entry = tk.Entry(master)
        self.sex_entry.grid(row=3, column=1)

        # Button to register user
        self.register_button = tk.Button(master, text="Registrera användare", command=self.register_user)
        self.register_button.grid(row=4, columnspan=2)

    def register_user(self):
        username = self.username_entry.get()
        year = self.year_entry.get()
        sex = self.sex_entry.get()

        # Perform registration logic here
        # For demonstration, we'll just print the entered data
        print("Registered User:")
        print("Username:", username)
        print("Year of Birth:", year)
        print("Sex:", sex)

        messagebox.showinfo("Registrering", "Användare registrerad!")

class DataLoggingApp:
    def __init__(self, master):
        self.master = master
        master.geometry("200x200")
        master.configure(bg="#f0f0f0")

        # Load the logo image
        logo_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")
        self.logo = tk.PhotoImage(file=logo_path)

        # Display the logo
        self.logo_label = tk.Label(master, image=self.logo, bg="#f0f0f0")
        self.logo_label.grid(row=0, columnspan=2)

        # Label and Entry for username
        self.username_label = tk.Label(master, text="Username:")
        self.username_label.grid(row=1, column=0, sticky="e")
        self.username_entry = tk.Entry(master)
        self.username_entry.grid(row=1, column=1)

        # Label and Entry for year of birth
        self.year_label = tk.Label(master, text="Födelseår:")
        self.year_label.grid(row=2, column=0, sticky="e")
        self.year_entry = tk.Entry(master)
        self.year_entry.grid(row=2, column=1)

        # Button to log visit
        self.log_button = tk.Button(master, text="Logga besök", command=self.log_visit)
        self.log_button.grid(row=3, columnspan=2)

    def log_visit(self):
        username = self.username_entry.get()
        year = self.year_entry.get()

        # Perform logging logic here
        # For demonstration, we'll just print the entered data
        print("Logged Visit:")
        print("Username:", username)
        print("Year of Birth:", year)

        messagebox.showinfo("Loggning", "Besök loggat!")

def main():
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
