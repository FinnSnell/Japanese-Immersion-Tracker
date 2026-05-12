# CustomTkinter window + layout
# Stopwatch working (start/stop)
# SQLite logging
# “Today total” display
# Category tracking
# matplotlib graphs
import customtkinter as ctk
from pages.timer_page import TimerPage
from pages.dashboard import DashboardPage
from components.navbar import Navbar

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("1000x1000")
        # navbar
        self.navbar = Navbar(self)
        self.navbar.pack(side="top", fill="x")

        # container for pages
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        # pages dictionary
        self.pages = {}

        # create pages
        self.pages["timer"] = TimerPage(self.container, self)
        self.pages["dashboard"] = DashboardPage(self.container, self)

        # show default page
        self.show_page("dashboard")

    def show_page(self, page_name):

        # hide all pages
        for page in self.pages.values():
            page.pack_forget()

        # show selected page
        self.pages[page_name].pack(fill="both", expand=True)


app = App()
app.mainloop()