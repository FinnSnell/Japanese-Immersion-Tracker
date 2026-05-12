import customtkinter as ctk


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