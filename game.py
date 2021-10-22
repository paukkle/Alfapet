from linkedlist import LinkedList


class AlfapetPlayers:
    def __init__(self):
        self.__players = None

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players_list: list):
        self.__players = LinkedList(players_list)

    def print_players(self):
        print("The players are:")
        players = []
        for player in self.__players:
            players.append(player.name)
            if player.next == self.players.head:
                break
        print(", ".join(players))
        print("")

    def add_points(self, player, amount):
        player.points += amount

    def get_sorted_points(self):
        points = {}
        for player in self.players:
            points[player.name] = player.points
            if player.next == self.players.head:
                break
        return {k: v for k, v in sorted(points.items(), key=lambda item: item[1], reverse=True)}

    def show_points(self):
        print("\nGame Over!\nPoints:")
        for player, points in self.get_sorted_points().items():
            print(f"{player}: {points}")
        print("")

    def zero_points(self):
        for player in self.players:
            player.points = 0
            if player.next == self.players.head:
                return


class Game:
    def __init__(self):
        self.alfapet = AlfapetPlayers()
        self.players = []
        self.running = True

    def get_players(self):
        while True:
            player = input("Add players into the game. Adding player named 'FINISH' starts the game: ")
            if player != "FINISH":
                if player in self.players:
                    print("Player already in game, pick another name.")
                    continue
                self.players.append(player)
                continue
            print("")
            break

    def set_players(self):
        self.alfapet.players = self.players

    def players_setup(self):
        self.get_players()
        if len(self.players) > 0:
            self.set_players()
            return True
        return False

    def get_choice(self):
        choice = input("Play again? Enter 'yes' for another game. ")
        return choice.lower() == "yes"

    def new_game(self):
        choice = self.get_choice()
        if choice:
            self.alfapet.zero_points()
            return
        self.running = False

    def play(self):
        print("Let's play Alfapet!")
        players_exist = self.players_setup()
        if not players_exist:
            print("No players. Exiting.")
            return
        print("Game starting.")
        self.alfapet.print_players()

        while self.running:
            for player in self.alfapet.players:
                print(f"{player.name}'s turn. Enter non-numerical character to finish the game.")
                try:
                    points = int(input("Points: "))
                    self.alfapet.add_points(player, points)
                except ValueError:
                    break
            self.alfapet.show_points()
            self.new_game()
        

a = Game()
a.play()
