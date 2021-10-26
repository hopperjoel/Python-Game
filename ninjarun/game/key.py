import arcade

class Key:
    """The responsibility of kEY is to keep track of key pressed 

    Stereotype:
        Information Holder

    Attributes:
        self (Key)       
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Key)
        """
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False 