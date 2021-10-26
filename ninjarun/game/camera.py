import arcade
from game import constants

class Camera:
    """The responsibility of Camera is to keep the player position at the screen center

    Stereotype:
        Information Holder

    Attributes:
        self.self.camera_to_player
        self.camera_to_gui            
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Camera)
        """
        self.camera_to_player = None
        self.camera_to_gui = None

    def set_camera(self):
        """ Set the camera
        Args:
            self (Camera)
        Return:
            arcade.Camera
        """
        return arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    
    def center_camera_to_player(self, player):
        """ keep the player position at the screen center
        Args:
            self (Camera)
            player (Player)
        Return:
            -
        """       
        screen_center_x = player.center_x - (self.camera_to_player.viewport_width / 2)       
        screen_center_y = player.center_y - (self.camera_to_player.viewport_height / 2)
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        self.camera_to_player.move_to(player_centered, 0.01)
      
    