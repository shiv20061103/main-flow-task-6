import json
import os
import random

# --- Player Class ---
class Player:
    def __init__(self, name, health=100, attack=10, defense=5, inventory=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = inventory if inventory is not None else []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} took {actual_damage} damage! Health: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed by {amount}. Health: {self.health}")

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "attack": self.attack,
            "defense": self.defense,
            "inventory": self.inventory
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data["name"],
            health=data["health"],
            attack=data["attack"],
            defense=data["defense"],
            inventory=data["inventory"]
        )

# --- Enemy Class ---
class Enemy:
    def __init__(self, name="Goblin", health=30, attack=8, defense=2):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.health -= actual_damage
        print(f"{self.name} took {actual_damage} damage! Health: {self.health}")

# --- Fight System ---
def fight(player, enemy):
    print(f"\n⚔️  A wild {enemy.name} appears!")

    while player.is_alive() and enemy.is_alive():
        input("\nPress Enter to attack...")
        enemy.take_damage(player.attack)

        if enemy.is_alive():
            player.take_damage(enemy.attack)

    if player.is_alive():
        print(f"\n✅ You defeated the {enemy.name}!")
        player.inventory.append("Gold")
    else:
        print("\n💀 You died. Game over.")

# --- Save / Load ---
def save_game(player):
    with open("savefile.json", "w") as f:
        json.dump(player.to_dict(), f)
    print("💾 Game saved.")

def load_game():
    if not os.path.exists("savefile.json"):
        print("⚠️ No save file found.")
        return None
    with open("savefile.json", "r") as f:
        data = json.load(f)
        return Player.from_dict(data)

# --- Game Map Locations ---
locations = {
    "forest": "🌲 A peaceful forest with sunlight peeking through trees.",
    "cave": "🕳️ A dark, creepy cave. You hear distant growls.",
    "lake": "💧 A calm, shining lake. It feels safe here."
}

# --- Game Loop ---
def game_loop():
    print("🎮 Welcome to the Command-Line RPG!")

    load = input("Load saved game? (y/n): ").lower()
    if load == 'y':
        player = load_game()
        if not player:
            name = input("Enter your name: ")
            player = Player(name)
    else:
        name = input("Enter your name: ")
        player = Player(name)

    while player.is_alive():
        print("\n📍 Locations:", ", ".join(locations.keys()))
        loc = input("Where do you want to go? ").lower()

        if loc not in locations:
            print("❌ Invalid location. Try again.")
            continue

        print(f"\n➡️ {locations[loc]}")

        event = random.choice(["enemy", "item", "nothing"])
        if event == "enemy":
            enemy = Enemy()
            fight(player, enemy)
        elif event == "item":
            print("🧪 You found a healing potion!")
            player.heal(20)
        else:
            print("🔍 Nothing happened. You rest peacefully.")

        if not player.is_alive():
            break

        if input("Do you want to save the game? (y/n): ").lower() == 'y':
            save_game(player)

        if input("Continue exploring? (y/n): ").lower() != 'y':
            print("👋 Thanks for playing!")
            break

# --- Entry Point ---
if __name__ == "__main__":
    game_loop()
