class Game:
    def __init__(self):
        self.move_count = 0
        self.difficulty = 0
        
        self.meet_user()
        self.game_explanation()
        self.choose_difficulty()
        self.required_moves = 2 ** self.difficulty - 1

        self.start_towers()
        
        #TODO
        self.get_move()
        self.make_a_move()


    def validate_yes_or_no_input(self, answer):
        positive_confirmation_input_accepted = [
            "Y",
            "YES",
            "YEAH",
            "OK",
            "ALRIGHT",
            "SIM",
            "S",
            "GO",
        ]
        stripped_answer = "".join(c for c in answer if c.isalnum())
        return stripped_answer.upper() in positive_confirmation_input_accepted

    def meet_user(self):
        name = input("How do you want to be called? ").strip().capitalize()
        print(f"\nHello, {name}! 😄\nWelcome to @lcsvoj's Tower of Hanoi!")

    def game_explanation(self):
        objective = "Your task is to move the entire stack of disks from the central rod to one of the other two."
        rules = "You must follow 3 simple rules:\n\t1. Only one disk can be moved at a time.\n\t2. Each move consists of replacing the upper disk from one of the stacks to the top of another or on an empty rod.\n\t3. No disk may be placed on top of a smaller disk."
        game_mechanism = ""  # TODO
        introduction_content = [objective, rules, game_mechanism]

        for item in introduction_content:
            confirmation = input(f"\n{item}\nType [Y] to continue. ")
            while not self.validate_yes_or_no_input(confirmation):
                confirmation = input("Type [Y] to continue. ")


    def choose_difficulty(self):
        while True:
            try:
                self.difficulty = int(input("Choose your difficulty level from 1 (easier) to 5 (harder).\nThis will be the total number of disks in the game. "))
                if 1 <= self.difficulty <= 5:
                    break
                else:
                    print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Please enter a number between 1 and 5.")
        
        print(f"The required number of moves to complete this level is {self.required_moves}.")
        confirmation = input("If you're ready for this challenge, say [Yes] and we'll begin.\nIf you want to choose a different level, type anything else. ")
        if not self.validate_yes_or_no_input(confirmation):
            self.choose_difficulty()
        else:
            return

    def start_towers(self):
        self.left_tower = Tower()
        self.right_tower = Tower()
        self.center_tower = Tower(self.difficulty)
        self.print_towers()

    def print_towers(self):
        # TODO
        
class Tower:
    def __init__(self, number_of_disks=0):
        self.number_of_disks = number_of_disks
        pass
    


def main():
    new_game = Game()


if __name__ == "__main__":
    main()
