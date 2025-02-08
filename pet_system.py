# PET HEALTHCARE SYSTEM

class Owner:
    def __init__(self, name, ph_no, address, pet_any):
        self.name = name
        self.ph_no = ph_no
        self.address = address
        self.pet_any = pet_any


class Pet:
    def __init__(self, breed, age, food, health):
        self.breed = breed
        self.age = age
        self.food = food
        self.health = health


class Veterinarian:
    def __init__(self, specialisation, treatment_rec):
        self.specialisation = specialisation
        self.treatment_rec = treatment_rec

class Display:
    def get_pet_rec(Owner):
        pet = Owner.pet_any
        print(f"\n\t\t\t\tPet Details: \nBreed : {pet.breed}\nPet age: {pet.age} yrs\nPet food : {pet.food}\nPet Health : {pet.health} Condition\n")

    def get_owner_details(Owner):
        print(f"\n\t\t\t\tOwner Details: \nOwner name: {Owner.name}\nPhone_no : +91 {Owner.ph_no}\nAddress : {Owner.address} 403802\nPet Details : None\n ")


    def get_veterinarian_details(Veterinarian):
        print(f"\n\t\t\t\tVeterinarian Details: \nVeterinarian specialisation: {Veterinarian.specialisation}\nVeterinarian treatment: {Veterinarian.treatment_rec}\n")


my_pet = Pet("German Shepard",2,"Pedigree","Good")
owner = Owner("Rahul",7123456872,"Sasmolane Last Bust Stop Vasco da gama Goa",my_pet)
vet = Veterinarian("General Medicine", "Routine Checkup")

while True:
    print("\nPet Details:\n")
    print("1) Pet Name: ")
    print("2) Pet age: ")
    print("3) Pet Food: ")
    print("4) Pet Health: ")
    print("5) Display Pet Records")
    print("6) Owner Details")
    print("7) Veterinarian Details")
    print("8) Exit")

    Owner_input = input("Choose (1-8)\n")

    if Owner_input == '8':
        print("Exiting.....")
        break
    elif Owner_input == '1':
        print("Enter your pet name")
        print(f"Pet name is: {owner.pet_any.breed}")

    elif Owner_input == '2':
        print("Enter your pet age")
        print(f"Pet age is: {owner.pet_any.age} yrs")

    elif Owner_input == '3':
        print("Enter your pet food")
        print(f"Pet Food is: {owner.pet_any.food}")

    elif Owner_input == '4':
        print("Enter your pet health")
        print(f"Pet Health is: {owner.pet_any.health}")

    elif Owner_input == '5':
        Display.get_pet_rec(owner)

    elif Owner_input == '6':
        Display.get_owner_details(owner)

    elif Owner_input == '7':
        Display.get_veterinarian_details(vet)

    else:
        print("Invalid option, please choose a number between 1 and 5.")