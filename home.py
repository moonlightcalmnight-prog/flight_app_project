import tkinter as tk
from tkinter import ttk
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = ttk.Label(self, text="Flight Booking Page", font=("Arial", 20, "bold"))
        label.pack(pady=20)
        
        book_button = ttk.Button(self, text="Book a new flight", command=lambda: controller.show_frame("BookingPage"))
        book_button.pack(pady=10, ipadx=10, ipady=5)
        
        view_button = ttk.Button(self, text="View reservations", command=lambda: controller.show_frame("ReservationsPage"))
        view_button.pack(pady=10, ipadx=10, ipady=5)
