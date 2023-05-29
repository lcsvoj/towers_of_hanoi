class Tower:

    def __init__(self, difficulty):
        self.tower_levels = {}
        self.tower_image = ""
        self.level_patterns = {
            "empty":  {"value": 0, "image": "           |           "}, # level 6
            "disk_1": {"value": 1, "image": "         (-1-)         "}, # level 5
            "disk_2": {"value": 2, "image": "        (--2--)        "}, # level 4 
            "disk_3": {"value": 3, "image": "       (---3---)       "}, # level 3
            "disk_4": {"value": 4, "image": "      (----4----)      "}, # level 2
            "disk_5": {"value": 5, "image": "     (-----5-----)     "}, # level 1
            "base":{"value": None, "image": "    [XXXXXX|XXXXXX]    "}, # level 0
        }

        self.create_empty_tower(difficulty)
        self.update_tower_image()

    def create_empty_tower(self, difficulty):
        """ Creates a tower with a base and {difficulty + 1} empty levels """
        for i in reversed(range(1, difficulty + 2)):
            self.tower_levels[i] = self.level_patterns["empty"]
        self.tower_levels[0] = self.level_patterns["base"]
    
    def update_tower_image(self):
        """ Creates/recreates the tower image string. """
        self.tower_image = ""
        for key in sorted(self.tower_levels.keys(), reverse=True):
            self.tower_image += self.tower_levels[key]["image"] + "\n"

    def get_highest_empty_level(self):
        """ Find the key for the highest level containing a disk. Returns None if there are no disks. """
        for key, level in self.tower_levels.items():
            if level["image"] != self.level_patterns["empty"]["image"]:
                return (key + 1)

    def remove_disk(self):
        """ Removes disk from a chosen tower, if there are disks to be removed. """
        target_level_key = self.get_highest_empty_level() - 1
        if self.tower_levels[target_level_key]["value"] == None:
            raise ValueError("There are no disks in this tower, try another one.")
        else:
            removed_level = self.tower_levels[target_level_key]
            self.tower_levels[target_level_key] = self.level_patterns["empty"]
            self.update_tower_image()
            return removed_level

    def add_disk(self, level_to_add=None, is_game_initialization=False, difficulty=None):
        """ Adds the passed disk on top of the current highest level disk. 
        If in initialization, fulfill the center tower with the initial disks. """
        if is_game_initialization:
            for i in range(1, difficulty + 1):
                self.tower_levels[i] = self.level_patterns[f"disk_{(difficulty + 1) - i}"]
        else:
            highest_empty_level_key = self.get_highest_empty_level()
            if highest_empty_level_key == 1:   # In other words, the tower is empty
                self.tower_levels[highest_empty_level_key] = level_to_add
            elif level_to_add["value"] > self.tower_levels[highest_empty_level_key - 1]["value"]:
                raise ValueError("Can't do that.\nThe disk you're trying to add is bigger than the disk on top of this tower.")
            else:
                self.tower_levels[highest_empty_level_key] = level_to_add

        self.update_tower_image()

    def get_image(self):
        """ Returns a string with the current tower image. """
        return "\n" + self.tower_image


class Game:
    def __init__(self):
        self.move_count = 0
        self.total_moves = 0
        self.difficulty = 0

        # Game introduction, prompt fot difficulty
        self.game_explanation()
        self.choose_difficulty()

        # Create and print the initial towers
        towers = self.start_towers()
        self.center_tower.add_disk(
            is_game_initialization=True, difficulty=self.difficulty
        )
        print(self.draw_towers(towers))

        # Copy the initial tower design to check in game results
        self.final_tower_image_objective = self.center_tower.tower_image

        # Game starts
        while True:
            # Make moves
            self.make_move()
            print(self.draw_towers(towers))
            # Update and check the moves status
            if self.is_game_over():
                break

        # Game ends
        if (
            self.left_tower.tower_image == self.final_tower_image_objective
            or self.right_tower.tower_image == self.final_tower_image_objective
        ):
            print("Congratulations, you solved the puzzle!")
        else:
            print("Sorry, you're out of moves. But don't give up, try again!")
        exit(0)

    def can_continue(self, answer):
        return answer == ""

    def game_explanation(self):
        objective = "Welcome to @lcsvoj's Towers of Hanoi!\nThe objective is to move all disks from the central rod to one of the other rods."
        rules = "Rules:\n1. Move only one disk at a time.\n2. Move a disk to the top of another stack or an empty rod.\n3. Never place a disk on top of a smaller disk."
        game_mechanism = "After each move, the remaining number of moves will be displayed. Use your moves wisely.\n\tGood luck, and don't f*ck it up!"
        introduction_content = [objective, rules, game_mechanism]

        for item in introduction_content:
            explanation = input(f"\n{item}\n\n[Press ENTER to continue] ")
            while not self.can_continue(explanation):
                explanation = input("[Press ENTER to continue] ")
        print()

    def choose_difficulty(self):
        min_level = 1
        max_level = 3
        while True:
            try:
                self.difficulty = int(
                    input(
                        f"Choose your difficulty level from {min_level} (easier) to {max_level} (harder). "
                    )
                )
                if min_level <= self.difficulty <= max_level:
                    break
                else:
                    print(f"Please enter a number between {min_level} and {max_level}.")
            except ValueError:
                print(f"Please enter a number between {min_level} and {max_level}.")
        self.difficulty += 2
        self.total_moves = 2**self.difficulty - 1

        print(
            f"\nIn this level, you'll have {self.total_moves} moves to reach the goal."
        )
        confirmation = input(
            "If you're ready for this challenge, [press ENTER to continue].\nIf you want to choose a different level, type anything else then press Enter. "
        )
        if not self.can_continue(confirmation):
            self.choose_difficulty()
        else:
            print("\nOk, let's begin! Here are the Towers of Hanoi: ")
            return

    def start_towers(self):
        self.left_tower = Tower(self.difficulty)
        self.center_tower = Tower(self.difficulty)
        self.right_tower = Tower(self.difficulty)
        towers = [self.left_tower, self.center_tower, self.right_tower]
        return towers

    def draw_towers(self, towers):
        recomposed_towers = "\n"
        for i in reversed(range(1, self.difficulty + 2)):
            for tower in towers:
                recomposed_towers += tower.tower_levels[i]["image"]
            recomposed_towers += "\n"
        recomposed_towers += towers[0].tower_levels[0]["image"] * 3 + "\n"
        recomposed_towers += (
            "\n"
            + "        Tower A        "
            + "        Tower B        "
            + "        Tower C        "
            + "\n"
        )
        return recomposed_towers

    def make_move(self):
        tower_options = {
            "a": self.left_tower,
            "tower a": self.left_tower,
            "b": self.center_tower,
            "tower b": self.center_tower,
            "c": self.right_tower,
            "tower c": self.right_tower,
        }

        from_tower = ""
        while True:
            try:
                from_tower = input("Select the tower to remove the top disk: ")
                removed_level = tower_options[from_tower.lower().strip()].remove_disk()
                break
            except KeyError:
                print(f"Oops, '{from_tower}' is not a valid tower!\n")
                pass
            except ValueError as e:
                print(e, "\n")
                pass

        to_tower = ""
        while True:
            try:
                to_tower = input("Now select the tower to place the disk: ")
                tower_options[to_tower.lower().strip()].add_disk(removed_level)
                break
            except KeyError:
                print(f"Oops, '{to_tower}' is not a valid tower!\n")
                pass
            except ValueError as e:
                print(e, "\n")
                pass

    def is_game_over(self):
        self.move_count += 1
        if self.move_count == self.total_moves:
            return True
        else:
            print(
                f"Used moves: {self.move_count} out of {self.total_moves}. Let's go to your next move!"
            )
            return False


def main():
    new_game = Game()


if __name__ == "__main__":
    main()
