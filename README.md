# __TOWERS OF HANOI__

## __Video Demo:__  <https://youtu.be/FFcHMRpUZUk>

## __Description:__

  This project was created as the final project of CS50's Introduction to Programming with Python.
  It is a "Tower of Hanoi" puzzle.  

  The implementation not only to correctly process the classic game mechanism, but also to provide a graphic representation of the game. It's designed to addapt to 3 levels of difficulty, which is chosen by the user.

### __Implementation__

  I've focused on object-oriented programming. The program is written with two classes as main columns: `Game` and `Tower`, and their methods are responsible for the vast majority of the game's mechanisms, including graphic construction and representation.

#### __Tower class__

  A Tower instance is created (by the `create_empty_tower` method) accepting the chosen difficulty as an argument. It'll have a base and a variable number of empty levels, depending on the passed argument, accepting values from 1 to 3, respectively corresponding to the puzzle with 3 to 5 disks. Each level is labeled with a numeric correspondence ascending from the base (set to zero) to the top.

  Each tower holds it's structure real-time information in `tower_levels`, a dictionary where the keys correspond to the numeric representation of the tower's level and the values are a second dictionary with 2 valuable pieces of data: the size of the disk that the level contains (incluindg `0` if the level does not have a disk, and `None` if it corresponds to the base level).

  The bigger dictionary is the source for the creation of the tower's image, that is updated (by the `update_tower_image` method) every time any modification (such as adding or removing disks) is made.

  The level patterns are held inside each tower, to be easily accessible. They're formatted in a way to instantly provide the visualization of the result that will be printed to the user, so it can be modified easily according to the programmer's desire.

  The `add_disk` and `remove_disk` methods, before updating the tower current image, check for the first empty level to correctly edit the tower state and can raise errors if the player is trying to remove a disk from a tower that doesn't have one to be removed or to put a bigger disk on top of a smaller one, which would break one of the fundaments of the puzzle.

  To access the image of the tower, an specific method is defined, `get_image`, that returns the printable string.

#### __Game class__

  This class keeps track of the number of moves made and the maximum of it, based on the chosen difficulty, which it takes as an argument. It's also responsible for starting the 3 towers and filling one of the to prepare the game.
  
  After initializing the towers in their first state (01 completely full and the other 2 completely empty), a dictionary indexes them with 2 possible keys for each, so we can make the game more user-friendly.
  
  At last, a copy of the "full tower" string is made to be used as comparison when the game ends and we check if the player won or lose it. This comparison is made by the `is_game_over` method, when the move counts matches the maximum moves permitted. This count is also encapsulated within this same method. If one of the edges towers matches the before saved pattern, the method prints a congratulation message. Otherwise, it's game over and good luck for the next attemp.

  With everything ready, the towers are printed and the user sees how many moves he'll get before the end.

#### __Auxiliary functions__

  As the project requires, some behaviors were included outside of the classes. These are:

- `get_name`, to prompt the user for it's name, that'll be used in the game introduction steps;
- `welcome`, that greets the user according to the given name;
- `get_difficulty`, that's the key function that defines the structure of the towers, as said before, receiving the difficult level that the player will choose;
- `make_move`, that's closely connected with the `remove_disk` and `add_disk` methods, integrating them and secure-checking their arguments before passing them;
- `new_game`, that will be responsible for instantiating the Game class object;
- and `play_game`, aggregator of the in-game behaviors, which are: `make_move`, the tower printing that shows every movement and the checking for the game end. 
