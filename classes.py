from data import pokemon
import random


class Card:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def __str__(self):
        return self.name


class Deck:
    def __init__(self):
        self.cards = []
        self.discard_pile = []
        self.generate_deck(pokemon)

    def generate_deck(self, data):
        for pokemon in data:
            self.cards.append(Card(pokemon.get("name"), pokemon.get("damage")))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop(0)

    def discard(self, card):
        self.discard_pile.append(card)

    def has_more_than_three(self):
        if len(self.cards) > 3:
            return True
        else:
            return False


class Player:
    def __init__(self, name, deck):
        self.points = 0
        self.rounds_won = 0
        self.hand = []
        self.name = name
        self.deck = deck

    def draw(self):
        while len(self.hand) < 3:
            self.hand.append(self.deck.draw())

    def play_card(self, index):
        return self.hand.pop(index)

    def choose_card(self):
        display_options = ""
        for index, card in enumerate(self.hand):
            display_options += f"{index}:{card.name} - {card.damage}\n"
        else:
            print("==== Your Hand ====\n")
            print(display_options)
        choice = input(
            "==== Choose your pokemon! ====\nPick the number associated with the pokemon\n")
        return self.play_card(int(choice))


class Game:
    def __init__(self, player, cpu):
        self.round = 0
        self.player = player
        self.cpu = cpu
        self.playable_cards = pokemon

    def start(self):
        print("\n==== Game Start ====\n")
        while self.player.deck.has_more_than_three() and self.cpu.deck.has_more_than_three():
            self.play_round()
        else:
            self.winner()

    def play_round(self):
        print("\n==== Start Round ====\n")
        self.deal_cards()
        self.battle()

    def deal_cards(self):
        self.player.draw()
        self.cpu.draw()

    def battle(self):
        player_round_points = 0
        cpu_round_points = 0

        while len(self.player.hand) > 0:
            player_card = self.player.choose_card()
            cpu_card = self.cpu.play_card(0)

            if player_card.damage > cpu_card.damage:
                print("Player Wins!")
                player_round_points += 1
            else:
                print("Cpu wins!")
                cpu_round_points += 1
            self.player.deck.discard(player_card)
            self.cpu.deck.discard(cpu_card)
        else:
            if player_round_points > cpu_round_points:
                self.player.rounds_won += 1
            else:
                self.cpu.rounds_won += 1

    def winner(self):
        output = "You Lose! Play Again?\nYes or No\n"
        if self.player.rounds_won > self.player.rounds_won:
            output = "You Win! Play Again?\nYes or No\n"
        choice = input(output)
        if choice == "yes":
            print("==== Starting Over ====")
        else:
            print("game Over")
