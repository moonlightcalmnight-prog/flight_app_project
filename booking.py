import tkinter as tk
from tkinter import ttk, messagebox
import database

class BookingPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Book a new flight", font=("Arial", 16, "bold"))
        label.pack(pady=10)
        
        # Input Fields
        fields = ["Passanger Name:", "Flight No.:", "Departure:", "Destination:", "Date:", "Seat No.:"]
        self.entries = {}
        for i, field in enumerate(fields):
            row = tk.Frame(self)
            lbl = ttk.Label(row, text=field, width=15)
            ent = ttk.Entry(row, width=30)
            row.pack(pady=5)
            lbl.pack(side="left", padx=5)
            ent.pack(side="right", padx=5)
            self.entries[field] = ent

        save_button = ttk.Button(self, text="Save Reservation", command=self.save_booking)
        save_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to HomePage", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=5)

    def save_booking(self):
        try:
            name = self.entries["Passanger Name:"].get()
            flight_number = self.entries["Flight No.:"].get()
            departure = self.entries["Departure:"].get()
            destination = self.entries["Destination:"].get()
            date = self.entries["Date:"].get()
            seat_number = self.entries["Seat No.:"].get()
            
            if not all([name, flight_number, departure, destination, date, seat_number]):
                messagebox.showerror("Error", "All fields must be filled")
                return

            database.add_reservation(name, flight_number, departure, destination, date, seat_number)
            messagebox.showinfo("Success", "Your flight has been successfully booked!")
            self.controller.show_frame("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            