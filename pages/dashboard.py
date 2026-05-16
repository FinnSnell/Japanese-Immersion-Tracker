import customtkinter as ctk
from database import get_today

class DashboardPage(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        title = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=("Arial", 40)
        )
        title.pack(pady=40)

        timer_button = ctk.CTkButton(
            self,
            text="Go To Timer Page",
            command=lambda: self.app.show_page("timer")
        )
        timer_button.pack(pady=20)

        #display todays times
        total_seconds = int(get_today())
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60

        total_title = ctk.CTkLabel(self, text="Today's Time", font=("Arial", 30))
        total_title.pack(pady=(30, 10))
        time_label = ctk.CTkLabel(self, text=f"{hours}h {minutes}m", font=("Arial", 30))
        time_label.pack(pady=20)
 

    