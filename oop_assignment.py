# ==================== ASSIGNMENT 1: SMARTPHONE CLASS ====================
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self._storage = storage  # Protected attribute
        self.__battery_life = battery_life  # Private attribute

    def display_info(self):
        return f"{self.brand} {self.model} | Storage: {self._storage}GB | Battery: {self.__battery_life}mAh"

    def check_battery(self):
        return f"Battery life: {self.__battery_life}mAh"

    def update_storage(self, new_storage):
        if new_storage > self._storage:
            self._storage = new_storage
            return f"Storage upgraded to {new_storage}GB"
        else:
            return "Storage must be larger than current"

class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu, cooling_system):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu
        self.cooling_system = cooling_system

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info} | GPU: {self.gpu} | Cooling: {self.cooling_system}"

    def game_mode(self):
        return f"Activating {self.cooling_system} cooling for optimal gaming!"

# ==================== ASSIGNMENT 2: POLYMORPHISM CHALLENGE ====================
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        pass

class Fish(Animal):
    def move(self):
        return "🐟 Swimming underwater!"

class Bird(Animal):
    def move(self):
        return "🐦 Flying in the sky!"

class Cheetah(Animal):
    def move(self):
        return "🐆 Running on land!"

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "🚗 Driving on the road!"

class Airplane(Vehicle):
    def move(self):
        return "✈️ Flying through the air!"

class Boat(Vehicle):
    def move(self):
        return "🚢 Sailing on water!"

# ==================== MAIN CODE TO RUN BOTH ASSIGNMENTS ====================
if __name__ == "__main__":
    print("📱 ASSIGNMENT 1: SMARTPHONE CLASS DEMONSTRATION")
    print("=" * 50)
    
    # Create a regular smartphone
    phone1 = Smartphone("Samsung", "Galaxy S23", 256, 5000)
    print(phone1.display_info())
    print(phone1.check_battery())
    print(phone1.update_storage(512))
    
    print("\n")
    
    # Create a gaming phone
    gaming_phone = GamingPhone("ASUS", "ROG Phone", 512, 6000, "Adreno 740", "Vapor Chamber")
    print(gaming_phone.display_info())
    print(gaming_phone.game_mode())
    print(gaming_phone.check_battery())
    
    print("\n\n")
    print("🐾 ASSIGNMENT 2: POLYMORPHISM CHALLENGE")
    print("=" * 50)
    
    # Test animal movement
    animals = [Fish("Nemo"), Bird("Eagle"), Cheetah("Swift")]
    for animal in animals:
        print(f"{animal.name}: {animal.move()}")
    
    print("\n")
    
    # Test vehicle movement
    vehicles = [Car("Toyota"), Airplane("Boeing"), Boat("Yacht")]
    for vehicle in vehicles:
        print(f"{vehicle.brand}: {vehicle.move()}")


        