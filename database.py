import sqlite3
DATABASE_NAME = "flights.db"
def create_table():
    #  Connects with database and creates ‘reservations’ if doesn’t exit
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            flight_number TEXT NOT NULL,
            departure TEXT NOT NULL,
            destination TEXT NOT NULL,
            date TEXT NOT NULL,
            seat_number TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_reservations():
# Retrieves all reservations from the database
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    reservations = cursor.fetchall()
    conn.close()
    return reservations

def add_reservation(name, flight_number, departure, destination, date, seat_number):
# Adds a new reservation to the database
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (name, flight_number, departure, destination, date, seat_number)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, flight_number, departure, destination, date, seat_number))
    conn.commit()
    conn.close()

def update_reservation(reservation_id, name, flight_number, departure, destination, date, seat_number):
# Creates an existing reservation based on the ID
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET name=?, flight_number=?, departure=?, destination=?, date=?, seat_number=?
        WHERE id=?
    ''', (name, flight_number, departure, destination, date, seat_number, reservation_id))
    conn.commit()
    conn.close()

def delete_reservation(reservation_id):
# Deletes an existing reservation based on the ID
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id=?", (reservation_id,))
    conn.commit()
    conn.close()

