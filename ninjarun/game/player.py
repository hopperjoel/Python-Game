import arcade
from game import constants
from pathlib import Path

class Player(arcade.Sprite):
    """A code template for a person who player the game.
    
    Stereotype:
        Information Holder

    Attributes:
        self (Sprite)        
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player)
        """        
        super().__init__()        

        self.gender = "girl"
        self.weapon = None        
        self.scale = constants.SCALE
        self.direction = constants.RIGHT  
        self.present_texture = 0 
        self.center_x = constants.PLAYER_START_X
        self.center_y = constants.PLAYER_START_Y
        self.root = Path(__file__).parent
        self.attack = False
        self.climb = False
        self.dead = False
        self.glide = False
        self.idle = False
        self.jump = False
        self.jump_attack = False
        self.jump_throw = False
        self.slide = False
        self.is_on_ladder = False

        self.image_attack = self.get_image(f"{self.root}/images/{self.gender}/attack__000.png")
        self.image_climb = self.get_image(f"{self.root}/images/{self.gender}/climb__000.png")
        self.image_dead = self.get_image(f"{self.root}/images/{self.gender}/dead__000.png")
        self.image_glide = self.get_image(f"{self.root}/images/{self.gender}/glide__000.png")        
        self.image_idle = self.get_image(f"{self.root}/images/{self.gender}/idle__000.png")
        self.image_jump = self.get_image(f"{self.root}/images/{self.gender}/jump__000.png")
        self.image_jump_attack = self.get_image(f"{self.root}/images/{self.gender}/jump_attack__000.png")
        self.image_jump_throw = self.get_image(f"{self.root}/images/{self.gender}/throw__000.png")
        self.image_jump_slide = self.get_image(f"{self.root}/images/{self.gender}/slide__000.png")
        
        self.attack_textures = []
        self.climb_textures = []
        self.dead_textures = []
        self.glide_textures = []
        self.idle_textures = []
        self.jump_textures = []
        self.jump_attack_textures = []
        self.jump_throw_textures = []
        self.slide_textures = []
        self.walk_textures = [] 

        for i in range(2):    
            texture = arcade.load_texture(f"{self.root}/images/{self.gender}/climb__00{i}.png")
            self.climb_textures.append(texture)
        for i in range(10):            
            texture = self.get_image(f"{self.root}/images/{self.gender}/idle__00{i}.png")
            self.idle_textures.append(texture)
        for i in range(10):            
            texture = self.get_image(f"{self.root}/images/{self.gender}/run__00{i}.png")
            self.walk_textures.append(texture) 
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/run__00{i}.png")
            self.attack_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/jump__00{i}.png")
            self.jump_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/jump_throw__00{i}.png")
            self.jump_throw_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/jump_attack__00{i}.png")
            self.jump_attack_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/slide__00{i}.png")
            self.slide_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/glide__00{i}.png")
            self.glide_textures.append(texture)
        for i in range(10):           
            texture = self.get_image(f"{self.root}/images/{self.gender}/dead__00{i}.png")
            self.dead_textures.append(texture)

        self.texture = self.image_idle[0]
        self.hit_box = self.texture.hit_box_points        

    def get_image(self, filename):
        """Called to get images to the player.
        Args: 
           - self (Player)
           - filename (String) 
        Return:
            - arcade.load_texture     
        """        
        return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
        ]
    
    def load_image(self, action):  
        """Called to load the images to the player.
        Args: 
           - self (Player)
           - action (String) 
        Return:
            -     
        """     
        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\run__00{i}.png")
            if action == "walk":
                self.walk_textures.append(texture)

    def update_animation(self, delta_time: float = 1 / 60):
        """Called to update animatios to sprite player.
        Args: 
           - self (Player)
           - delta_time (Arcade)
        Return:
            -     
        """  
        if self.change_y == 20:
            self.texture = self.image_jump[self.direction]
            return


        if self.is_on_ladder:
            self.climb = True
        if not self.is_on_ladder and self.climb:
            self.climb = False
        if self.climb and abs(self.change_y) > 1:
            self.present_texture += 1
            if self.present_texture > 7:
                self.present_texture = 0
        if self.climb:
            self.texture = self.climb_textures[self.present_texture // 5]            
            return
      
        if self.change_x < 0 and self.direction == constants.RIGHT:
            self.direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.direction == constants.LEFT_FACING:
            self.direction = constants.RIGHT 

        if self.is_on_ladder:
            self.climb = True
        if not self.is_on_ladder and self.climb:
            self.climb = False
        if self.climb and abs(self.change_y) > 1:
            self.present_texture += 1
            if self.present_texture > 9:
                self.present_texture = 0
        if self.climb:
            self.texture = self.climb_textures[self.present_texture // 4]
            return

        if self.change_x == 0:
            self.texture = self.image_idle[self.direction]
            return

        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.image_jump[self.direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.image_dead[self.direction]
            return

        self.present_texture += 1
        if self.present_texture > 9:
            self.present_texture = 0
        self.texture = self.attack_textures[self.present_texture][
            self.direction
        ]


    

        
