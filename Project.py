class CarRegistrationSystem:
    def __init__(self):
        self.registry = []

    def register_car(self, registration_number, make, model, year):
        car_data = {
            'apke gari ka registration number': registration_number,
            'apke gari ka make': make,
            'apke gari ka model': model,
            'apke gari ka saal': year
        }
        self.registry.append(car_data)
        print(f"apki gari register ho chuki hai:\n{car_data}")

    def display_registry(self):
        if not self.registry:
            print("yahan par kohi gari register nhi howi hai.")
        else:
            print("apni gari register kare:")
            for car in self.registry:
                print(f"Registration Number: {car['apke gari ka registration number']}")
                print(f"apke gari ka make: {car['apke gari ka make']}")
                print(f"apke gari ka model: {car['apke gari ka model']}")
                print(f"apke gari ka model: {car['apke gari ka saal']}")
                print("----------------------------")

def main():
    registration_system = CarRegistrationSystem()

    while True:
        print("\nCar Registration System")
        print("1. Apni Gari Register karen")
        print("2. Mujhuda Gario Ko Dekae")
        print("3. Exit Karen")

        choice = input("chioce karen (1/2/3): ")

        if choice == '1':
            registration_number = input("apni gari ka registration number leken: ")
            make = input("apki gari konsi company ki hai: ")
            model = input("apne gari ka model darjh kare: ")
            year = input("apne gari ka saal darjh karen: ")


            registration_system.register_car(registration_number, make, model, year)

        elif choice == '2':
            registration_system.display_registry()

        elif choice == '3':
            print("Ap car registration system se bahir nekal gaye hain. shukriya!")
            break

        else:
            print("apne galat number join kiya hai")
if __name__ == "__main__":
    main()
