import arcade
from pathlib import Path
from game import constants

class Sound:
    """A code template for get the sounds used in the game.
    
    Stereotype:
        Information Holder
        Service Provider

    Attributes:
        self (Sound)        
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Sound)
        """    
        self.sound = None

        self.root = Path(__file__).parent

    def get_sound(self, action=None):
        """Called to play sounds in the game.
        Args: 
           - self (Sound)
           - action (String) 
        Return:
            - arcade.play_sound     
        """     
        if action == "coin":
            sound_source = f"{constants.SOUND_DIR}/money_1.mp3"
        elif action == "jump":
            sound_source = f"{self.root}/sounds/female_kiai_2.mp3"
            #sound_source = ":resources:sounds/jump1.wav"
        elif action == "kunai":
            sound_source = f"{self.root}/sounds/arrow_hit_3.mp3"
        elif action == "gameover":
            sound_source = f"{self.root}/sounds/hard_hit_2.mp3"
        elif action == "throw":
            sound_source = f"{self.root}/sounds/shuriken_throw_1.mp3"
        elif action == "stick":
            sound_source = f"{self.root}/sounds/shuriken_stick.mp3"
            sound_source = ":resources:sounds/gameover3.wav"
        elif action == "win":
            sound_source = constants.WIN_SOUND
        else:
            sound_source = ""
        self.sound = arcade.load_sound(sound_source)
        return arcade.play_sound(self.sound)
        


         

        