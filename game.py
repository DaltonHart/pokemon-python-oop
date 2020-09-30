from classes import Deck, Player, Game

eggbert = Player("Eggbert", Deck())
cpu = Player("Cpu", Deck())

game = Game(eggbert, cpu)

game.start()
