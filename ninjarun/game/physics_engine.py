from game import constants
import arcade

class PhysicsEngine:
    """The physics engine for use in platformer game.

    Stereotype:
        Information Holder

    Attributes:
        self (PhysicsEngine)       
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (PhysicsEngine)
        """
        self.engine = None

    def set_engine(self, player, sprite_list, scene):
        """Set the physics engine.
        Args: 
          - self (PhysicsEngine)
          - player (Player)
          - sprite_list (Scene)
          - scene (Scene)
        """
        self.engine = arcade.PhysicsEnginePlatformer(
            player,
            [
                sprite_list(constants.LAYER_NAME_PLATFORMS),
                scene.get_sprite_list(constants.LAYER_NAME_MOVING_PLATFORMS),
            ],
            gravity_constant=constants.GRAVITY,
            ladders=scene.get_sprite_list(constants.LAYER_NAME_LADDERS),
        )
      
