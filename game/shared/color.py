class Color:
    # A color.

    # The responsibility of Color is to hold and provide information about itself. Color has a few 
    # convenience methods for comparing them and converting to a tuple.

    # Attributes:
    #     _red (int): The red value.
    #     _green (int): The green value.
    #     _blue (int): The blue value.
    #     _alpha (int): The alpha or opacity.
    
    
    def __init__(self, red, yellow, blue, alpha = 255):
        # Constructs a new Color using the specified red, yellow, blue and alpha values. The alpha 
        # value is the color's opacity.
        
        # Args:
        #     red (int): A red value.
        #     yellow (int): A yellow value.
        #     blue (int): A blue value.
        #     alpha (int): An alpha or opacity.
        
        self._red = red
        self._yellow = yellow
        self._blue = blue 
        self._alpha = alpha

    def to_tuple(self):
        # Gets the color as a tuple of four values (red, yellow, blue, alpha).

        # Returns:
        #     Tuple(int, int, int, int): The color as a tuple.
        
        return (self._red, self._yellow, self._blue, self._alpha)   