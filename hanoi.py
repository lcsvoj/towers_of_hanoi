import draw_tower as draw


class Game:
    def __init__(self):
        self.move_count = 0
        self.difficulty = 0
        
        self.meet_user()
        self.game_explanation()
        self.choose_difficulty()

        towers = self.start_towers()
        print(self.draw_towers(towers))
        
        #TODO
        #self.get_move()
        #self.make_a_move()


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
            confirmation = input(f"\n{item}\n\n[Type 'Y' to continue] ")
            while not self.validate_yes_or_no_input(confirmation):
                confirmation = input("[Type 'Y' to continue] ")
        print()

    def choose_difficulty(self):
        min_level = 1
        max_level = 3        
        while True:
            try:
                self.difficulty = int(input(f"\nChoose your difficulty level from {min_level} (easier) to {max_level} (harder).\nThis will be the total number of disks in the game. "))
                if min_level <= self.difficulty <= max_level:
                    break
                else:
                    print(f"Please enter a number between {min_level} and {max_level}.")
            except ValueError:
                print(f"Please enter a number between {min_level} and {max_level}.")
        self.difficulty += 2
        required_moves = 2 ** self.difficulty - 1

        print(f"\nThe required number of moves to complete this level is {required_moves}.")
        confirmation = input("If you're ready for this challenge, type 'Yes' and we'll begin.\nIf you want to choose a different level, type anything else. ")
        if not self.validate_yes_or_no_input(confirmation):
            self.choose_difficulty()
        else:
            return

    def start_towers(self):
        self.left_tower = Tower(self.difficulty)
        self.right_tower = Tower(self.difficulty)
        self.center_tower = Tower(self.difficulty)
        towers = [self.left_tower, self.right_tower, self.center_tower]
        return towers

    def draw_towers(self, towers):
        # Decompose each tower str line by line
        all_towers_lines = []
        for tower in towers:
            all_towers_lines.append(tower.get_image().split("\n"))
        
        # Recompose uniting the 3 towers into a single str
        recomposed_towers = ""
        for i in range(self.center_tower.height):
            for j in range(len(towers)):
                recomposed_towers += all_towers_lines[j][i]
            recomposed_towers += "\n"
        
        return recomposed_towers

class Tower:
    
    def __init__(self, number_of_disks=0):
        self.number_of_disks = number_of_disks
        self.height = self.number_of_disks + 2
        self.image = (draw.empty_level + "\n") * self.height + draw.base_level

    def get_image(self):
        return self.image
        


def main():
    new_game = Game()


if __name__ == "__main__":
    main()
