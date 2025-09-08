import sqlite3
import requests

# connect to database (creates file if it doesn’t exist)
conn = sqlite3.connect("dream_cars.db")
cursor = conn.cursor()

# create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS cars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
)
""")

def add_car(name):
    try:
        cursor.execute("INSERT INTO cars (name) VALUES (?)", (name,))
        conn.commit()
        print(f"{name} added to database!")
    except sqlite3.IntegrityError:
        print(f"{name} already exists in the list.")

def delete_car(name):
    cursor.execute("DELETE FROM cars WHERE name = ?", (name,))
    conn.commit()
    print(f"{name} removed (if it was in the list).")

def show_cars():
    cursor.execute("SELECT name FROM cars")
    cars = cursor.fetchall()
    if cars:
        print("Your dream cars:")
        for car in cars:
            print("-", car[0])
    else:
        print("No cars in the list yet.") #note to self - functions here are already defined, i just need to call said functions later in the code.
"""
def browse_cars():
    response = requests.get("/vehicles/GetModelsForMake/honda?format=json")

    if response.status_code == 200:
        car_data = response.json()  # Parse the JSON response
        print("Available Cars:")
        for car in car_data:
            print(f"- {car['make']} {car['model']} ({car['year']}) - Fuel Type: {car['fuel_type']}")
    else:
        print("Failed to retrieve car data. Please try again later.")
"""
def main():

    while True: #loop to keep the program running

        choice = input("\nwhat would you like to do? add a car?, delete a car?, display(show) your list?, browse?, or exit the program?").strip().lower()

        if choice == "add":

            car = input("enter your dream car, ").strip() #note to self - .strip() removes any spaces (and line breaks, tabs, etc.) from the beginning and end of a string.

            add_car(car) #function defined earlier

        elif choice == "delete":

            car = input("enter the car you want to delete, ").strip()

            delete_car(car)

        elif choice == "show":

            show_cars()

        #elif choice == "browse":

            #browse_cars()

        elif choice == "exit": #ends the loop

            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again")

    conn.close()  # Close the database connection

if __name__ == "__main__":
    main()  # Call the main function to start the program