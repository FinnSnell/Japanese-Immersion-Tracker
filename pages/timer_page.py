import customtkinter as ctk
import time
import sqlite3
from database import add_category

class addCategoriesWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")
        self.attributes("-topmost", True)
        self.lift()

        #textbok to create
        self.entry = ctk.CTkEntry(self, placeholder_text = "category")
        self.entry.pack(pady=20)

        #dropdown
        self.optionmenu = ctk.CTkOptionMenu(self,values=["Reading", "Listening", "Speaking"])
        self.optionmenu.pack(pady=20)
        self.optionmenu.set("Choose Category")
        
        self.button = ctk.CTkButton(self, text="Submit", command=self.submit_data)
        self.button.pack(pady=20)

    def get_database_options(self):
         # connect and fetch data
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM categories")
        rows = cursor.fetchall()
        conn.close()
        return [row[0] for row in rows] if rows else ["No Categories"]

    def submit_data(self):
        entry_val = self.entry.get()
        dropdown_val = self.optionmenu.get()
        if entry_val and dropdown_val:
            add_category(entry_val, dropdown_val)

        else:
            self.destroy()




class TimerPage(ctk.CTkFrame):
    #layout in the init
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.categories_window = None

        #make the stopwatch application
        self.running = False
        self.start_time = 0
        self.timer_label = ctk.CTkLabel(self, text="00:00:00", font=("Arial", 40))
        self.timer_label.pack(pady=40)
        self.timer_button = ctk.CTkButton(self, text="Start Timer", command=self.toggle_timer)
        self.timer_button.pack(pady=20)

        #dropdown menu for categories


        #new window
        self.categories_button = ctk.CTkButton(self, text="Create New Category", command=self.open_CategoriesWindow)
        self.categories_button.pack(pady=20)
        #####
    def toggle_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.timer_button.configure(text="Stop Timer")
            self.update_timer()

        else:
            self.running = False
            self.timer_button.configure(text="Start Timer")

    def update_timer(self):
        if self.running:
            elapsed = int(time.time() - self.start_time)

            hours = elapsed //3600
            minutes = (elapsed % 3600) // 60
            seconds = elapsed % 60

            self.timer_label.configure(
                text=f"{hours:02}:{minutes:02}:{seconds:02}"
            )

            self.after(1000, self.update_timer)

    def open_CategoriesWindow(self):
        if self.categories_window is None or not self.categories_window.winfo_exists():
            self.categories_window = addCategoriesWindow(self)
            self.categories_window.attributes("-topmost", True)
        else:
            self.categories_window.focus()
