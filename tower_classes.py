class Tower:

    def __init__(self, difficulty):
        self.tower_levels = {}
        self.tower_image = ""
        self.level_patterns = {
            "empty":  {"value": 0, "image": "           |           "}, # level 6
            "disk_1": {"value": 1, "image": "         (o|o)         "}, # level 5
            "disk_2": {"value": 2, "image": "        (oo|oo)        "}, # level 4 
            "disk_3": {"value": 3, "image": "       (ooo|ooo)       "}, # level 3
            "disk_4": {"value": 4, "image": "      (oooo|oooo)      "}, # level 2
            "disk_5": {"value": 5, "image": "     (ooooo|ooooo)     "}, # level 1
            "base":{"value": None, "image": "   [[[[[[[[|]]]]]]]]   "}, # level 0
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

    def get_top_disk_level_key(self):
        """ Find the key for the highest level containing a disk. Returns None if there are no disks. """
        for key, level in self.tower_levels.items():
            if level["image"] != self.level_patterns["empty"]["image"]:
                if level["value"] == None:
                    return None
                else:
                    return key

    def remove_disk(self):
        """ Removes disk from a chosen tower, if there are disks to be removed. """
        target_level_key = self.get_top_disk_level_key()
        if target_level_key == None:
            raise ValueError("There are no disks in this tower, try another one.")
            return
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
            self.update_tower_image()
        
        else:
            top_disk_level_key = self.tower_levels[self.get_top_disk_level_key()]
            if level_to_add["value"] < self.tower_levels[top_disk_level_key]["value"]:
                raise ValueError("Can't do that.\nThe disk you're trying to add is bigger than the disk on top of this tower.")
                return
            else:
                self.tower_levels[top_disk_level_key] = level_to_add
                self.update_tower_image()

    def get_image(self):
        """ Returns a string with the current tower image. """
        return "\n" + self.tower_image
    