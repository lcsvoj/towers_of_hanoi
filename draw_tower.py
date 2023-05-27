""" tower design:

           |           empty
         (o|o)         
        (oo|oo)        
       (ooo|ooo)       
      (oooo|oooo)      
     (ooooo|ooooo)     
   [[[[[[[[|]]]]]]]]   base

"""


class TowerLevel:
    level_patterns = {
        "disk_0": {"value": 0, "image": "           |           "},
        "disk_1": {"value": 1, "image": "         (o|o)         "},
        "disk_2": {"value": 2, "image": "        (oo|oo)        "},
        "disk_3": {"value": 3, "image": "       (ooo|ooo)       "},
        "disk_4": {"value": 4, "image": "      (oooo|oooo)      "},
        "disk_5": {"value": 5, "image": "     (ooooo|ooooo)     "},
        "base": {"value": None, "image": "   [[[[[[[[|]]]]]]]]   "},
    }

    def __init__(self, value=0, is_base=False):
        self.value = value
        if self.value == 0:
            self.is_empty = True
        self.is_base = is_base
        if not self.is_base:
            self.image = self.level_patterns[f"disk_{self.value}"]["image"]
            self.value = self.level_patterns[f"disk_{self.value}"]["value"]
        else:
            self.image = self.level_patterns["base"]["image"]
            self.value = self.level_patterns["base"]["value"]

    def __str__(self):
        return self.image
