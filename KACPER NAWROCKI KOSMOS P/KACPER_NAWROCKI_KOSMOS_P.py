# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from typing import List

# --- INTERFEJSY ---
class BaseBuilder(ABC):
    @abstractmethod
    def build_secret_base(self) -> str:
        pass

# --- 1. ABSTRAKCJA (Klasa bazowa) ---
class SpaceObject(ABC):
    def __init__(self, name: str, danger_level: int):
        self.name = name
        self.danger_level = danger_level  # Uzywa ukrytego settera!
        self.is_scanned = False

    # WALIDACJA (Enkapsulacja)
    @property
    def danger_level(self) -> int:
        return self._danger_level

    @danger_level.setter
    def danger_level(self, value: int):
        if value < 1 or value > 10:
            raise ValueError(f"Poziom zagrozenia dla {self.name} musi byc w skali 1-10!")
        self._danger_level = value

    @abstractmethod
    def get_vibe(self) -> str:
        pass

    # PRZECIAZENIE METOD (Symulacja)
    def scan(self, deep_scan: bool = False):
        self.is_scanned = True
        if deep_scan:
            print(f"Gleboki skan {self.name}: Wykryto ukryte anomalie!")
        else:
            print(f"Szybki skan {self.name}: Wyglada bezpiecznie... chyba.")

# --- 2. DZIEDZICZENIE I POLIMORFIZM ---
class CoolPlanet(SpaceObject):
    def __init__(self, name: str, danger_level: int, has_aliens: bool, weather: str):
        super().__init__(name, danger_level)
        self.has_aliens = has_aliens
        self.weather = weather

    # PRZECIAZENIE KONSTRUKTOROW
    @classmethod
    def create_peaceful_world(cls, name: str):
        return cls(name, danger_level=1, has_aliens=True, weather="Ciagla tecza i slonce")

    def get_vibe(self) -> str:
        alien_status = "Pelno obcych!" if self.has_aliens else "Pusto i cicho."
        return f"Planeta. Pogoda: {self.weather}. {alien_status}"

class TreasureAsteroid(SpaceObject):
    def __init__(self, name: str, danger_level: int, tons_of_gold: int):
        super().__init__(name, danger_level)
        self.tons_of_gold = tons_of_gold

    def get_vibe(self) -> str:
        return f"Asteroida. Zloto: {self.tons_of_gold} ton. Czas sie bogacic!"

# --- WIELOKROTNE DZIEDZICZENIE ---
class SciFiWorld(CoolPlanet, BaseBuilder):
    def __init__(self, name: str, danger_level: int, has_aliens: bool, weather: str, secret_tech: str):
        super().__init__(name, danger_level, has_aliens, weather)
        self.secret_tech = secret_tech

    def build_secret_base(self) -> str:
        return f"Budujemy tajna baze na {self.name}, zeby badac technologie: {self.secret_tech}!"

# --- 3. ENKAPSULACJA ---
class SpaceExplorer:
    def __init__(self, nickname: str, space_credits: int):
        self._nickname = nickname
        self._space_credits = space_credits

    @property
    def nickname(self):
        return self._nickname

# --- 4. KOMPOZYCJA ---
class SpaceAdventure:
    def __init__(self, explorer: SpaceExplorer, destination: SpaceObject):
        self.explorer = explorer
        self.destination = destination
        self.status = "W trakcie lotu"

# --- KLASA Z METODAMI STATYCZNYMI ---
class GalacticFederation:
    adventures: List[SpaceAdventure] = []

    @staticmethod
    def send_on_adventure(explorer: SpaceExplorer, destination: SpaceObject):
        if destination.danger_level > 8:
            print(f"UWAGA: {explorer.nickname} leci na {destination.name}! To samobojcza misja!")
        
        adventure = SpaceAdventure(explorer, destination)
        GalacticFederation.adventures.append(adventure)
        return adventure

# --- KLASA ZARZADCZA ---
class StarMap:
    def __init__(self):
        self.objects = []

    def add_to_map(self, space_obj: SpaceObject):
        self.objects.append(space_obj)

    def print_cool_map(self):
        print("\n--- MAPA GALAKTYKI ---")
        for obj in self.objects:
            print(f"{obj.name} (Zagrozenie: {obj.danger_level}/10) -> {obj.get_vibe()}")

# --- ODPALAMY PROGRAM ---
if __name__ == "__main__":
    starmap = StarMap()
    
    # Tworzymy obiekty
    arrakis = CoolPlanet("Arrakis", 9, True, "Ciagla burza piaskowa i wielkie czerwie")
    naboo = CoolPlanet.create_peaceful_world("Naboo")
    gold_rock = TreasureAsteroid("Zlota Bryla X-99", 5, 5000)
    cybertron = SciFiWorld("Cybertron", 10, True, "Metaliczny deszcz", "Zmiennoksztaltne roboty")

    # Dodajemy do mapy
    starmap.add_to_map(arrakis)
    starmap.add_to_map(naboo)
    starmap.add_to_map(gold_rock)
    starmap.add_to_map(cybertron)

    starmap.print_cool_map()

    # Polimorfizm i metody przeciazone
    print("\n--- SKANOWANIE ---")
    naboo.scan()
    arrakis.scan(deep_scan=True)

    # Interfejs
    print("\n--- AKCJE SPECJALNE ---")
    print(cybertron.build_secret_base())

    # Misje
    print("\n--- WYSYLAMY ODKRYWCOW ---")
    han_solo = SpaceExplorer("Han Solo", 15000)
    GalacticFederation.send_on_adventure(han_solo, arrakis)