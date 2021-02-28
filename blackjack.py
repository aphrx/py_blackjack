from deck import Deck
from player import Player

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        self.player.show()

        if p_status == 1:
            print("Player got Blackjack! Congrats!")
            if d_status == 1:
                print("Dealer and Player got Blackjack! It's a push. (Tie)")
            return 1

        cmd = ""
        while cmd != "Stand":
            bust = 0
            cmd = input("Hit or Stand? ")

            if cmd == "Hit":
                bust = self.player.hit()
                self.player.show()
            if bust == 1:
                print("Player busted. Good Game!")
                return 1
        print("\n")
        self.dealer.show()
        if d_status == 1:
            print("Dealer got Blackjack! Better luck next time!")
            return 1

        while self.dealer.check_score() < 17:
            if self.dealer.hit() == 1:
                self.dealer.show()
                print("Dealer busted. Congrats!")
                return 1
            self.dealer.show()

        if self.dealer.check_score() == self.player.check_score():
            print("It's a Push (Tie). Better luck next time!")
        elif self.dealer.check_score() > self.player.check_score():
            print("Dealer wins. Good Game!")
        elif self.dealer.check_score() < self.player.check_score():
            print("Player wins. Congratulations!")

b = Blackjack()
b.play()