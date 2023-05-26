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
    levels = {
        "disk_0": {"value": 0, "image": "           |           "},
        "disk_1": {"value": 1, "image": "         (o|o)         "},
        "disk_2": {"value": 2, "image": "        (oo|oo)        "}, 
        "disk_3": {"value": 3, "image": "       (ooo|ooo)       "},
        "disk_4": {"value": 4, "image": "      (oooo|oooo)      "},
        "disk_5": {"value": 5, "image": "     (ooooo|ooooo)     "},
        "base": {"value": None,"image": "   [[[[[[[[|]]]]]]]]   "},
    }

    def __init__(self, level_disk_value=0, is_base=False):
        self.level_disk_value = level_disk_value
        
        if self.level_disk_value == 0:
          self.is_empty = True

        self.is_base = is_base
        
        if not self.is_base:
           self.image = self.levels[f"disk_{self.level_disk_value}"]["image"]
        else:
           self.image = self.levels["base"]

    def __str__(self):
        return self.image
