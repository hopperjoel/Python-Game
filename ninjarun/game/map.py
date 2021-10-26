from game import constants
import arcade

class Map:
    """The responsibility of Map is to load the map used in the game

    Stereotype:
        Information Holder

    Attributes:
        self (Map)       
    """
    def __init__(self):  
        """The class constructor.
        
        Args:
            self (Map)
        """ 
        self.map_path = constants.MAP_DIR
        self.level = 1
        self.name = f"{self.map_path}/map1_level_{self.level}.json"
        
        self.layer_options = {
             constants.LAYER_NAME_GROUND: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_MOVING_PLATFORMS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_BACKGROUND: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_LADDERS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_KUNAI: {
                "use_spatial_hash": True,
            },
             constants.LAYER_NAME_ENEMIES: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_DONT_TOUCH: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_THROW: {
                "use_spatial_hash": True,
            },
        }
        self.map = arcade.load_tilemap(self.name, constants.TILE_SCALING, self.layer_options)

        self.end_map = self.map.tiled_map.map_size.width * constants.GRID_PIXEL_SIZE

    def set_background(self):
        """Set the scene background.
        Args: self (Map)
        """
        if self.map.tiled_map.background_color:
            arcade.set_background_color(self.map.tiled_map.background_color)

    def set_map(self):
        """Set the scene map.
        Args: self (Map)

        Return: arcade.load_tilemap
        """
        return arcade.load_tilemap(self.name, constants.TILE_SCALING, self.layer_options)

