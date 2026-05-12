import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        timerbtn = ctk.CTkButton(self, text="Timer", command=lambda: parent.show_page("timer"))
        timerbtn.pack(side="left", padx=10, pady=5)
