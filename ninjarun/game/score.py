import arcade

class Score:
    """A code for keep track score
    
    Stereotype:
        Information Holder

    Attributes:
        self (Self)               
    """   
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Score)
        """    
        self.score = 0

    def show_score(self):
        """Called to show the score on the screen.
        Args: 
           - self (Score)           
        Return:
            -  text (String)   
        """    
        text = f"Score: {self.score}"
        return text
        



