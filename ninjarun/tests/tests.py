import pytest
import arcade
from game import constants
from game.camera import Camera
from game.player import Player
from game.map import Map
from game.physics_engine import PhysicsEngine
from game.scene import Scene
from game.score import Score
from game.sound import Sound

def test_set_camera():
    """Called to test camera.set_camera method.
        Args: 
           -            
        Return:
            - assert camera.set_camera (arcade.Camera)     
    """        
    camera = Camera()
    assert camera.set_camera() == arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

def test_center_camera_to_player():
    """Called to test camera.center_camera_to_player method.
        Args: 
           -            
        Return:
            - assert screen_center_x: Int
            - assert screen_center_y: Int

    """    
    camera = Camera()
    player = Player()
    screen_center_x = player.center_x - (camera.camera_to_player.viewport_width / 2)
    screen_center_y = player.center_y - (camera.camera_to_player.viewport_height / 2)
    camera.center_camera_to_player(player)
    assert screen_center_x == 0
    assert screen_center_y == 0

def set_map_test():
    """Called to test map.set_map method.
        Args: 
           -            
        Return:
            - assert my_map: arcade.loadtilemap
    """ 
    map = Map()
    my_map = map.set_map()
    assert my_map == arcade.load_tilemap(map.name, constants.TILE_SCALING, map.layer_options)

def set_engine_test():
    """Called to test physics_engine.set_engine method.
        Args: 
           -            
        Return:
            - assert engine: arcade.PhysicsEnginePlatformer
    """ 
    player = Player()
    engine = PhysicsEngine()
    this_scene = Scene()
    engine.set_engine(player, this_scene.scene.get_sprite_list, this_scene.scene )
    assert engine == arcade.PhysicsEnginePlatformer(
            player,
            [
                this_scene.scene.get_sprite_list(constants.LAYER_NAME_PLATFORMS),
                this_scene.scene.get_sprite_list(constants.LAYER_NAME_MOVING_PLATFORMS),
            ],
            gravity_constant=constants.GRAVITY,
            ladders=this_scene.scene.get_sprite_list(constants.LAYER_NAME_LADDERS),
        )

def load_image_test():
    """Called to test player.load_image method.
        Args: 
           -            
        Return:
            -  assert len(walk_textures): int
    """ 
    player = Player()
    action = "walk"
    walk_textures = []
    for i in range(10):
            texture = player.get_image(f"{constants.IMAGE_DIR }\\boy\\run__00{i}.png")
            if action == "walk":
                walk_textures.append(texture)
    assert len(walk_textures) == 10

def show_score_test():
    """Called to test score.show_score method.
        Args: 
           -            
        Return:
            -  assert text: String
    """ 
    score_manager = Score()
    score_manager.score = 10

    text = score_manager.show_score()
    assert text == f"Score: {score_manager.score}" 

def get_sound_test():
    """Called to test sound.get_sound method.
        Args: 
           -            
        Return:
            -  assert sound_source: String
    """ 
    action = "coin" 

    if action == "coin":
        sound_source = f"{constants.SOUND_DIR}/money_1.mp3"
    elif action == "jump":
        sound_source = "/sounds/female_kiai_2.mp3"            
    elif action == "kunai":
        sound_source = ":resources:sounds/hurt4.wav"
    elif action == "gameover":
        sound_source = ":resources:sounds/gameover3.wav"
    else:
        sound_source = ""

    assert sound_source == f"{constants.SOUND_DIR}/money_1.mp3"

    




    

    
    

    









