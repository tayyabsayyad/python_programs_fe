class Vehicle:
    def __init__(self, vehicle_id, type, brand, price_per_day, available=True):
        """
        Initialize a Vehicle with its ID, type, brand, price per day, and availability.
        """
        self.vehicle_id = vehicle_id
        self.type = type  # e.g., Car, Bike, Truck
        self.brand = brand
        self.available = available

    def mark_as_rented(self):
        """
        Mark the vehicle as not available for rent.
        """
        self.available = False

    def mark_as_available(self):
        """
        Mark the vehicle as available for rent.
        """
        self.available = True

    def __str__(self):
        return (f"Vehicle ID: {self.vehicle_id}, Type: {self.type}, Brand: {self.brand}, "
                f"Price/Day: ${self.price_per_day}, Available: {self.available}")


class RentalTransaction:
    def __init__(self, transaction_id, customer_name, vehicle, rental_days):
        """
        Initialize a RentalTransaction with ID, customer name, vehicle, and rental period.
        """
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.vehicle = vehicle
        self.rental_days = rental_days
        self.total_price = self.calculate_price()

    def calculate_price(self):
        """
        Calculate the total rental price based on rental days and price per day.
        """
        return self.rental_days * self.vehicle.price_per_day

    def __str__(self):
        return (f"Transaction ID: {self.transaction_id}, Customer: {self.customer_name}, "
                f"Vehicle: {self.vehicle.type} ({self.vehicle.brand}), "
                f"Rental Days: {self.rental_days}, Total Price: ${self.total_price}")


class RentalAgency:
    def __init__(self, name):
        """
      sion access points for IntelliSense (Pylance), Debugging  Initialize a RentalAgency with its name and an inventory of vehicles.
        """
        self.name = name
        self.vehicles = []  # List of Vehicle objects
        self.transactions = []  # List of RentalTransaction objects

    def add_vehicle(self, vehicle):
        """
        Add a new vehicle to the agency's inventory.
        """
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to the inventory.")

    def display_available_vehicles(self):
        """
        Display all available vehicles.
        """
        print(f"\nAvailable Vehicles in {self.name}:")
        available_vehicles = [vehicle for vehicle in self.vehicles if vehicle.available]
        if not available_vehicles:
            print("No vehicles available.")
        else:
            for vehicle in available_vehicles:
                print(vehicle)

    def book_vehicle(self, customer_name, vehicle_id, rental_days):
        """
        Book a vehicle for a customer if it is available.
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if vehicle.available:
                    vehicle.mark_as_rented()
                    transaction = RentalTransaction(
                        len(self.transactions) + 1,
                        customer_name,
                        vehicle,
                        rental_days
                    )
                    self.transactions.append(transaction)
                    print(f"\nBooking successful! Transaction details:")
                    print(transaction)
                    return
                else:
                    print(f"Error: Vehicle {vehicle_id} is not available.")
                    return
        print(f"Error: Vehicle {vehicle_id} not found.")

    def return_vehicle(self, vehicle_id):
        """
        Return a rented vehicle and mark it as available.
        """
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                if not vehicle.available:
                    vehicle.mark_as_available()
                    print(f"Vehicle {vehicle_id} has been returned and is now available.")
                    return
                else:
                    print(f"Error: Vehicle {vehicle_id} is already available.")
                    return
        print(f"Error: Vehicle {vehicle_id} not found.")

    def display_transactions(self):
        """
        Display all rental transactions.
        """
        print(f"\nRental Transactions at {self.name}:")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)

# Create a rental agency
agency = RentalAgency("City Rentals")

# Add vehicles to the agency
vehicle1 = Vehicle(101, "Car", "Toyota Corolla", 50)
vehicle2 = Vehicle(102, "Bike", "Yamaha R15", 20)
vehicle3 = Vehicle(103, "Truck", "Ford F-150", 100)
agency.add_vehicle(vehicle1)
agency.add_vehicle(vehicle2)
agency.add_vehicle(vehicle3)

# Display available vehicles
agency.display_available_vehicles()

# Book a vehicle
agency.book_vehicle("Alice", 101, 3)  # Alice rents the Toyota Corolla for 3 days

# Try booking the same vehicle
agency.book_vehicle("Bob", 101, 2)  # Error: Vehicle not available

# Display available vehicles
agency.display_available_vehicles()

# Return the vehiclesion access points for IntelliSense (Pylance), Debugging

# Display transactions
agency.display_transactions()