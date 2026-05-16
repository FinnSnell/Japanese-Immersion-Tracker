import customtkinter as ctk

class Navbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        dashbtn = ctk.CTkButton(self, text="Dashboard", command=lambda: parent.show_page("dashboard"))
        dashbtn.pack(side="left", padx=1, pady=5 )

        timerbtn = ctk.CTkButton(self, text="Timer", command=lambda: parent.show_page("timer"))
        timerbtn.pack(side="left", padx=1, pady=5)

