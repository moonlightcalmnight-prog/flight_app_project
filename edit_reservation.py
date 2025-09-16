import tkinter as tk
from tkinter import ttk, messagebox
import database
import sqlite3

class EditReservationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.reservation_id = None
        self.entries = {}
        
        label = ttk.Label(self, text="Edit Reservation", font=("Arial", 16, "bold"))
        label.pack(pady=10)
        
        fields = ["ID:", "Passenger Name:", "Flight Number:", "Departure:", "Destination:", "Date:", "Seat Number:"]
        for i, field in enumerate(fields):
            row = tk.Frame(self)
            lbl = ttk.Label(row, text=field, width=15)
            ent = ttk.Entry(row, width=30)
            row.pack(pady=5)
            lbl.pack(side="left", padx=5)
            ent.pack(side="right", padx=5)
            self.entries[field] = ent
        
        self.entries["ID:"].config(state="readonly")

        update_button = ttk.Button(self, text="Update Reservation", command=self.update_booking)
        update_button.pack(pady=10)
        
        delete_button = ttk.Button(self, text="Delete Reservation", command=self.delete_booking)
        delete_button.pack(pady=5)
        
        back_button = ttk.Button(self, text="Back to Reservations List", command=lambda: controller.show_frame("ReservationsPage"))
        back_button.pack(pady=5)

    def load_reservation_data(self, reservation_id):
        """Fills the form with the selected reservation's data."""
        self.reservation_id = reservation_id
        conn = sqlite3.connect(database.DATABASE_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM reservations WHERE id=?", (reservation_id,))
        record = cursor.fetchone()
        conn.close()
        
        if record:
            self.entries["ID:"].config(state="normal")
            self.entries["ID:"].delete(0, tk.END)
            self.entries["ID:"].insert(0, record[0])
            self.entries["ID:"].config(state="readonly")
            
            self.entries["Passenger Name:"].delete(0, tk.END)
            self.entries["Passenger Name:"].insert(0, record[1])
            
            self.entries["Flight Number:"].delete(0, tk.END)
            self.entries["Flight Number:"].insert(0, record[2])
            
            self.entries["Departure:"].delete(0, tk.END)
            self.entries["Departure:"].insert(0, record[3])
            
            self.entries["Destination:"].delete(0, tk.END)
            self.entries["Destination:"].insert(0, record[4])
            
            self.entries["Date:"].delete(0, tk.END)
            self.entries["Date:"].insert(0, record[5])
            
            self.entries["Seat Number:"].delete(0, tk.END)
            self.entries["Seat Number:"].insert(0, record[6])

    def update_booking(self):
        try:
            name = self.entries["Passenger Name:"].get()
            flight_number = self.entries["Flight Number:"].get()
            departure = self.entries["Departure:"].get()
            destination = self.entries["Destination:"].get()
            date = self.entries["Date:"].get()
            seat_number = self.entries["Seat Number:"].get()
            
            if not all([name, flight_number, departure, destination, date, seat_number]):
                messagebox.showerror("Error", "All fields must be filled.")
                return

            database.update_reservation(self.reservation_id, name, flight_number, departure, destination, date, seat_number)
            messagebox.showinfo("Success", "Reservation updated successfully!")
            self.controller.show_frame("ReservationsPage")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def delete_booking(self):
        if messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this reservation?"):
            database.delete_reservation(self.reservation_id)
            messagebox.showinfo("Success", "Reservation deleted successfully!")
            self.controller.show_frame("ReservationsPage")
            