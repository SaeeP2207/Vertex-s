class Movie:
    def __init__(self, movie_id, name, duration, genre):
        self.movie_id = movie_id
        self.name = name
        self.duration = duration
        self.genre = genre
    def display_movie(self):
        print(f"{self.movie_id}. {self.name} ({self.genre}, {self.duration} mins)")

class Seat:
    def __init__(self, seat_number):
        self.seat_number = seat_number
        self.__status = "Available"
    def is_available(self):
        return self.__status == "Available"
    def book_seat(self):
        if self.is_available():
            self.__status = "Booked"
            return True
        return False
    def get_price(self):
        return 0

class RegularSeat(Seat):
    def get_price(self):
        return 150

class PremiumSeat(Seat):
    def get_price(self):
        return 250

class Show:
    def __init__(self, show_id, movie, time):
        self.show_id = show_id
        self.movie = movie
        self.time = time
        self.seats = []
        for i in range(1, 6):
            self.seats.append(RegularSeat(f"R{i}"))
        for i in range(1, 4):
            self.seats.append(PremiumSeat(f"P{i}"))
    def display_show(self):
        print(f"Show {self.show_id}: {self.movie.name} at {self.time}")
    def display_seats(self):
        for seat in self.seats:
            status = "Available" if seat.is_available() else "Booked"
            print(seat.seat_number, "-", status)
    def get_seat(self, seat_number):
        for seat in self.seats:
            if seat.seat_number == seat_number:
                return seat
        return None

class Snack:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class FoodCounter:
    def __init__(self):
        self.snacks = [
            Snack("Popcorn", 120),
            Snack("Burger", 150),
            Snack("Nachos", 100),
            Snack("Cold Drink", 80)
        ]

    def display_menu(self):
        print("\n--- Snack Menu ---")
        for i, snack in enumerate(self.snacks, 1):
            print(f"{i}. {snack.name} - ₹{snack.price}")

    def order_snacks(self):
        self.display_menu()
        choices = input("Enter snack numbers (comma separated): ").split(",")
        selected = []
        for ch in choices:
            idx = int(ch.strip()) - 1
            if 0 <= idx < len(self.snacks):
                selected.append(self.snacks[idx])
        service = input("Service type (1-Self Service / 2-In Seat Service): ")
        extra_charge = 30 if service == "2" else 0
        total = sum(snack.price for snack in selected) + extra_charge
        return selected, total

class Booking:
    booking_counter = 1
    def __init__(self, customer_name):
        self.booking_id = Booking.booking_counter
        Booking.booking_counter += 1
        self.customer_name = customer_name
        self.seats = []
        self.snacks = []
        self.food_bill = 0
        self.is_paid = False
    def add_seats(self, seats):
        self.seats.extend(seats)
    def add_snacks(self, snacks, bill):
        self.snacks.extend(snacks)
        self.food_bill += bill
    def calculate_total(self):
        seat_total = sum(seat.get_price() for seat in self.seats)
        return seat_total + self.food_bill
    def display_summary(self):
        print("\n--- Booking Summary ---")
        print("Booking ID:", self.booking_id)
        print("Customer:", self.customer_name)
        print("Seats:", ", ".join(seat.seat_number for seat in self.seats))
        if self.snacks:
            print("Snacks:", ", ".join(snack.name for snack in self.snacks))
            print("Food Bill: ₹", self.food_bill)
        print("Total Amount: ₹", self.calculate_total())
        print("Payment Status:", "Paid" if self.is_paid else "Pending")
    def make_payment(self):
        if self.is_paid:
            print("Payment already completed.")
            return
        print("\n--- Payment Options ---")
        print("1. Cash")
        print("2. UPI")
        print("3. Card")
        choice = input("Select payment method: ")
        if choice in ["1", "2", "3"]:
            self.is_paid = True
            print("Payment successful! Booking confirmed 🎉")
        else:
            print("Invalid payment option.")

class Theatre:
    def __init__(self):
        self.shows = []
        self.food_counter = FoodCounter()
        self.current_booking = None
    def setup(self):
        m1 = Movie(1, "Inception", 148, "Sci-Fi")
        m2 = Movie(2, "Interstellar", 169, "Sci-Fi")
        self.shows.append(Show(1, m1, "10:00 AM"))
        self.shows.append(Show(2, m2, "2:00 PM"))
    def start(self):
        while True:
            print("\n--- Movie Theatre Menu ---")
            print("1. View Shows")
            print("2. View Seat Availability")
            print("3. Book Movie Tickets")
            print("4. Order Snacks")
            print("5. View Snack Menu")
            print("6. View Booking Summary")
            print("7. Billing & Payment")
            print("8. Exit")
            choice = input("Enter choice: ")
            if choice == "1":
                for show in self.shows:
                    show.display_show()
            elif choice == "2":
                sid = int(input("Enter Show ID: "))
                show = next((s for s in self.shows if s.show_id == sid), None)
                if show:
                    show.display_seats()
            elif choice == "3":
                name = input("Enter customer name: ")
                self.current_booking = Booking(name)
                sid = int(input("Enter Show ID: "))
                show = next((s for s in self.shows if s.show_id == sid), None)
                if show:
                    show.display_seats()
                    seats = input("Enter seat numbers: ").split(",")
                    selected = []
                    for s in seats:
                        seat = show.get_seat(s.strip())
                        if seat and seat.book_seat():
                            selected.append(seat)
                    self.current_booking.add_seats(selected)
            elif choice == "4":
                if self.current_booking:
                    snacks, bill = self.food_counter.order_snacks()
                    self.current_booking.add_snacks(snacks, bill)
                else:
                    print("Please book tickets first.")
            elif choice == "5":
                self.food_counter.display_menu()
            elif choice == "6":
                if self.current_booking:
                    self.current_booking.display_summary()
                else:
                    print("No booking found.")
            elif choice == "7":
                if self.current_booking:
                    self.current_booking.make_payment()
                else:
                    print("No booking available.")
            elif choice == "8":
                print("Thank you for visiting the theatre 🎬")
                break
            else:
                print("Invalid choice")

theatre = Theatre()
theatre.setup()
theatre.start()