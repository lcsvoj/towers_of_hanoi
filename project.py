class Tower:
    def __init__(self, difficulty):
        self.tower_levels = {}
        self.tower_image = ""
        self.level_patterns = {
            "empty":  {"value": 0, "image": "           |           "},  # level 6
            "disk_1": {"value": 1, "image": "         (-1-)         "},  # level 5
            "disk_2": {"value": 2, "image": "        (--2--)        "},  # level 4
            "disk_3": {"value": 3, "image": "       (---3---)       "},  # level 3
            "disk_4": {"value": 4, "image": "      (----4----)      "},  # level 2
            "disk_5": {"value": 5, "image": "     (-----5-----)     "},  # level 1
            "base":{"value": None, "image": "    [XXXXXX|XXXXXX]    "},  # level 0
        }

        self.create_empty_tower(difficulty)
        self.update_tower_image()

    def create_empty_tower(self, difficulty):
        """Creates a tower with a base and {difficulty + 1} empty levels"""
        for i in reversed(range(1, difficulty + 2)):
            self.tower_levels[i] = self.level_patterns["empty"]
        self.tower_levels[0] = self.level_patterns["base"]

    def update_tower_image(self):
        """Creates/recreates the tower image string."""
        self.tower_image = ""
        for key in sorted(self.tower_levels.keys(), reverse=True):
            self.tower_image += self.tower_levels[key]["image"] + "\n"

    def get_highest_empty_level(self):
        """Find the key for the highest level containing a disk. Returns None if there are no disks."""
        for key, level in self.tower_levels.items():
            if level["image"] != self.level_patterns["empty"]["image"]:
                return key + 1

    def remove_disk(self):
        """Removes disk from a chosen tower, if there are disks to be removed."""
        target_level_key = self.get_highest_empty_level() - 1
        if self.tower_levels[target_level_key]["value"] == None:
            raise ValueError("There are no disks in this tower, try another one.")
        else:
            removed_level = self.tower_levels[target_level_key]
            self.tower_levels[target_level_key] = self.level_patterns["empty"]
            self.update_tower_image()
            return removed_level

    def add_disk(
        self, level_to_add=None, is_game_initialization=False, difficulty=None
    ):
        """Adds the passed disk on top of the current highest level disk.
        If in initialization, fulfill the center tower with the initial disks."""
        if is_game_initialization:
            for i in range(1, difficulty + 1):
                self.tower_levels[i] = self.level_patterns[
                    f"disk_{(difficulty + 1) - i}"
                ]
        else:
            highest_empty_level_key = self.get_highest_empty_level()
            if highest_empty_level_key == 1:  # In other words, the tower is empty
                self.tower_levels[highest_empty_level_key] = level_to_add
            elif (
                level_to_add["value"]
                > self.tower_levels[highest_empty_level_key - 1]["value"]
            ):
                raise ValueError(
                    "Can't do that.\nThe disk you're trying to add is bigger than the disk on top of this tower."
                )
            else:
                self.tower_levels[highest_empty_level_key] = level_to_add

        self.update_tower_image()

    def get_image(self):
        """Returns a string with the current tower image."""
        return "\n" + self.tower_image


class Game:
    def __init__(self, difficulty):
        self.move_count = 0
        self.total_moves = 2**difficulty - 1
        self.difficulty = difficulty
        # Create and print the initial towers
        self.towers = self.start_towers()
        self.center_tower.add_disk(
            is_game_initialization=True, difficulty=self.difficulty
        )
        print(self.draw_towers())

        self.tower_options = {
            "a": self.left_tower,
            "tower a": self.left_tower,
            "b": self.center_tower,
            "tower b": self.center_tower,
            "c": self.right_tower,
            "tower c": self.right_tower,
        }
        # Copy the initial tower design to check in game results
        self.final_tower_image_objective = self.center_tower.tower_image

    def start_towers(self):
        self.left_tower = Tower(self.difficulty)
        self.center_tower = Tower(self.difficulty)
        self.right_tower = Tower(self.difficulty)
        towers = [self.left_tower, self.center_tower, self.right_tower]
        return towers

    def draw_towers(self):
        recomposed_towers = "\n"
        for i in reversed(range(1, self.difficulty + 2)):
            for tower in self.towers:
                recomposed_towers += tower.tower_levels[i]["image"]
            recomposed_towers += "\n"
        recomposed_towers += self.towers[0].tower_levels[0]["image"] * 3 + "\n"
        recomposed_towers += (
            "\n"
            + "        Tower A        "
            + "        Tower B        "
            + "        Tower C        "
            + "\n"
        )
        return recomposed_towers

    def is_game_over(self):
        self.move_count += 1
        if self.move_count == self.total_moves:  # Game ends
            if (
                self.left_tower.tower_image == self.final_tower_image_objective
                or self.right_tower.tower_image == self.final_tower_image_objective
            ):
                print("Congratulations, you solved the puzzle!")
            else:
                print("Sorry, you're out of moves. But don't give up, try again!")
            return True
        else:
            print(
                f"Used moves: {self.move_count} out of {self.total_moves}. Let's go to your next move!"
            )
            return False


def main():
    name = get_name()
    print(welcome(name))
    difficulty = get_difficulty(name)
    game = new_game(difficulty)
    play_game(game)


def get_name():
    while True:
        name = input("Hello! What's your name? ")
        if name.strip().isalpha():
            return name.strip().capitalize()
        else:
            pass


def welcome(name):
    objective = f"Welcome to @lcsvoj's Towers of Hanoi, {name}!\nThe objective is to move all disks from the central rod to one of the other rods."
    rules = "Rules:\n1. Move only one disk at a time.\n2. Move a disk to the top of another stack or an empty rod.\n3. Never place a disk on top of a smaller disk."
    game_mechanism = "After each move, the remaining number of moves will be displayed. Use your moves wisely.\n\tGood luck!"
    return objective + rules + game_mechanism


def get_difficulty(name, difficulty=None):
    min_level = 1
    max_level = 3
    while True:
        try:
            difficulty = int(
                input(
                    f"{name}, you may choose your difficulty level from {min_level} (easier) to {max_level} (harder). "
                )
            )
            if min_level <= difficulty <= max_level:
                number_of_disks = difficulty + 2
                return number_of_disks
            else:
                raise ValueError(f"Please enter a number between {min_level} and {max_level}.")
        except ValueError as e:
            print(e)
    


def make_move(game):
    while True:
            try:
                from_tower = input("Select the tower to remove the top disk: ")
                removed_level = game.tower_options[from_tower.lower().strip()].remove_disk()
                break
            except KeyError:
                print(f"Oops, '{from_tower}' is not a valid tower!\n")
                pass
            except ValueError as e:
                print(e, "\n")
                pass

    while True:
        try:
            to_tower = input("Now select the tower to place the disk: ")
            game.tower_options[to_tower.lower().strip()].add_disk(removed_level)
            break
        except KeyError:
            print(f"Oops, '{to_tower}' is not a valid tower!\n")
            pass
        except ValueError as e:
            print(e, "\n")
            pass


def new_game(difficulty):
    game = Game(difficulty)
    print(
            f"\nIn this level, you'll have {game.total_moves} moves to reach the goal.\n"
        )
    return game


def play_game(game):
    while True:
        make_move(game)
        print(game.draw_towers())
        if game.is_game_over():
            break


if __name__ == "__main__":
    main()
