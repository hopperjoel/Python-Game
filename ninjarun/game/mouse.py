import arcade
from game import constants
from pathlib import Path

class Mouse(arcade.Sprite):
    """Class to manage mouse input
    
    Stereotype:
        Information Holder
        Coordinator

    Attributes:
        self (Sprite)        
    """
    def __init__(self):
        """ The class constructor

        Attributes:
            self.ammo_count - for throwable "ammo"
            self.ammo_count - a list for ammo sprites
            self.center_x - starting point for thrown object
            self.center_y - starting point for thrown object        
        """

        super().__init__()
        self._ammo_count = 0
        self._ammo_list = []
        self.center_x = 0
        self.center_y = 0


    """
    def on_mouse_motion(self, x, y, dx, dy):
        Called whenever the mouse moves.
        
        self._mouse_manager.center_x = x
        self._mouse_manager.center_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        Called whenever the mouse button is clicked.
        Need to move to objects class

        # Kunai Throwing sound
        self._sound_manager.get_sound("throw")
        arcade.play_sound(self._sound_manager.sound)

        # Create a kunai
        kunai = arcade.Sprite(f"{constants.IMAGE_DIR}/kunai.png", constants.KUNAI_SCALING)

        # Reorient the image according to angle of throw
        # a = abs(y - self._player.center_y) 
        # b = abs(x - self._player.center_x)
        # adjusted_angle = atan(a / b)
        kunai.angle = 90

        # Give the bullet a speed
        kunai.change_y = constants.KUNAI_SPEED

        # Position the bullet
        kunai.center_x = self._player.center_x
        kunai.bottom = self._player.top

        # Add the bullet to the appropriate lists
        self._ammo_list.append(kunai)

    
    def create_ammo(self, x, y, button, modifiers):
        # Kunai Throwing sound
        self._sound_manager.get_sound("throw")
        arcade.play_sound(self._sound_manager.sound)

        # Create a kunai
        kunai = arcade.Sprite(f"{constants.IMAGE_DIR}/kunai.png", constants.KUNAI_SCALING)

        # The image points to the right, and we want it to point up. So
        # rotate it.
        kunai.angle = 90 # absolute(y - self._player.center_y) = a
                        # absolute(x - self._player.center_x) = b
                        # tan(x) = a / b

        # Give the bullet a speed
        kunai.change_y = constants.KUNAI_SPEED

        # Position the bullet
        kunai.center_x = self._player.center_x
        kunai.bottom = self._player.top

        # Add the bullet to the appropriate lists
        self._ammo_list.append(kunai)

        return self._ammo_list
        """