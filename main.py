import tkinter as tk
import database
from home import HomePage
from booking import BookingPage
from reservation import ReservationsPage
from edit_reservation import EditReservationPage

class FlightReservationApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Flight Reservation App")
        self.geometry("800x600")
        
        database.create_table()  # Ensure the table is created on app startup
        
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, BookingPage, ReservationsPage, EditReservationPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name, **kwargs):
        """Displays a specific frame."""
        frame = self.frames[page_name]
        if page_name == "EditReservationPage" and "reservation_id" in kwargs:
            frame.load_reservation_data(kwargs["reservation_id"])
        frame.tkraise()

if __name__ == "__main__":
    app = FlightReservationApp()
    app.mainloop()
    