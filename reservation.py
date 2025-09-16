import tkinter as tk
from tkinter import ttk, messagebox
import database

class ReservationsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="List of Reservations", font=("Arial", 16, "bold"))
        label.pack(pady=10)
        
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Flight", "Departure", "Destination", "Date", "Seat"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Passenger Name")
        self.tree.heading("Flight", text="Flight Number")
        self.tree.heading("Departure", text="Departure")
        self.tree.heading("Destination", text="Destination")
        self.tree.heading("Date", text="Date")
        self.tree.heading("Seat", text="Seat Number")
        self.tree.pack(fill="both", expand=True)
        
        self.tree.bind("<Double-1>", self.on_double_click)

        refresh_button = ttk.Button(self, text="Refresh List", command=self.refresh_list)
        refresh_button.pack(pady=10)

        back_button = ttk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        back_button.pack(pady=5)
        
        self.refresh_list()

    def refresh_list(self):
    # Clears old data and loads new data from the database.
        for row in self.tree.get_children():
            self.tree.delete(row)
            
        reservations = database.get_all_reservations()
        for reservation in reservations:
            self.tree.insert("", "end", values=reservation)
            
    def on_double_click(self, event):
    # On double-click, shows the edit page for the selected item.
        selected_item = self.tree.focus()
        if not selected_item:
            return
        
        item_values = self.tree.item(selected_item, "values")
        reservation_id = item_values[0]
        self.controller.show_frame("EditReservationPage", reservation_id=reservation_id)
        