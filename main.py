import random
import requests


class Felimon:
    def __init__(self, name, element, attack, defense):
        self.name = name
        self.element = element
        self.attack = attack
        self.defense = defense
        self.level = 1

    def __repr__(self):
        return f"[{self.element.upper()}] {self.name} (ATK:{self.attack}/DEF:{self.defense}) LV:{self.level}"

    def attack_target(self, target_felimon):
        """Calcula o dano causado a outro Felimon (Ataque - Defesa)."""
        damage = self.attack - target_felimon.defense
        return max(0, damage)

    def level_up(self):
        """Aumenta o nível e os atributos aleatoriamente."""
        self.level += 1
        self.attack += random.randint(1, 3)
        self.defense += random.randint(1, 2)


class Deck:
    def __init__(self, owner_name):
        self.owner_name = owner_name
        self.cards = []

    def add_card(self, felimon):
        self.cards.append(felimon)

    def get_strongest(self):
        """Retorna o Felimon com maior ataque. Ótimo para testar cobertura."""
        if not self.cards:
            return None
        return max(self.cards, key=lambda f: f.attack)

    def fetch_magical_name(self):
        """
        Simula busca de nome em API externa. 
        PONTO DE MOCK: Essencial para a demo de pytest-mock.
        """
        try:
            # Simulando endpoint de nomes mágicos
            response = requests.get("https://api.magicnames.com/v1/cat", timeout=1)
            if response.status_code == 200:
                return response.json()['name']
            return "Gato Comum"
        except Exception:
            return "Gato Misterioso"


# Lógica de execução manual (Botão verde do PyCharm)
if __name__ == '__main__':
    print("--- Felimon ---")

    f1 = Felimon("Pyromander", "Fogo", 12, 5)
    f2 = Felimon("Aqualeo", "Água", 10, 8)

    meu_deck = Deck(owner_name="Chrystian")
    meu_deck.add_card(f1)
    meu_deck.add_card(f2)

    print(f"Deck de {meu_deck.owner_name} criado com {len(meu_deck.cards)} cartas.")
    print(f"O mais forte é: {meu_deck.get_strongest()}")

    dano = f1.attack_target(f2)
    print(f"\n{f1.name} ataca {f2.name} e causa {dano} de dano!")

    novo_nome = meu_deck.fetch_magical_name()
    print(f"Nome sugerido pela 'API' para o próximo Felimon: {novo_nome}")