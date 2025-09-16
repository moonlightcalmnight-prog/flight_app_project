# flight_app_project
Simple Flight Reservation Desktop App  Using Tkinter and SQLite
Flight Reservation System
A desktop application for a flight reservation system, designed to be intuitive and easy to use. This project demonstrates skills in graphical user interface (GUI) development, database management, and application packaging.

Features
Simple Booking: Easily book new flights with a user-friendly form.

Reservation Management: View, edit, and cancel existing flight reservations.

Search Functionality: Quickly find specific reservations.

Integrated Database: Stores all data locally using SQLite, requiring no external server.

User-friendly Interface: Developed with Tkinter for a clean and simple design.

Technologies Used
Python: The core programming language.

Tkinter: Used for building the desktop GUI.

SQLite3: A lightweight, serverless database for persistent data storage.

PyInstaller: For creating a standalone executable file (.exe).

Getting Started
1. Clone the Repository
To get a local copy of the project, use the following command in your terminal:

Bash

git clone https://github.com/moonlightcalmnight-prog/Flight_Reservation_App.git
2. Navigate to the Project Directory

Bash

cd Flight_Reservation_App
3. Run the Application
To run the application from the source code, make sure you have Python installed and then execute:

Bash

python main.py
Building the Executable
If you want to create a standalone application that does not require Python to be installed on the user's machine, you can build an executable (.exe) file using PyInstaller.

Install PyInstaller

Bash

pip install pyinstaller
Build the Executable
Navigate to the project's root directory and run the following command:

Bash

pyinstaller --onefile --windowed main.py
The final executable file will be located in the dist folder.

File Structure
This is the file structure of the project:

/Flight_Reservation_App
├── main.py                    # Main application file
├── database.py                # Handles SQLite database operations
├── home.py                    # User interface for the home page
├── booking.py                 # UI for flight booking
├── reservations.py            # Displays list of reservations
├── edit_reservation.py        # Handles updating and deleting reservations
├── flights.db                 # SQLite database file (generated automatically)
├── requirements.txt           # List of required Python libraries
├── .gitignore                 # Files to be ignored by Git
├── README.md                  # Project documentation (this file)
└── assets/                    # Optional: folder for images or icons
