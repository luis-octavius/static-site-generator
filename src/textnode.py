from enum import Enum 

class Bender(Enum):
    AIR_BENDER = "air"
    WATER_BENDER = "water"
    EARTH_BENDER = "earth"
    FIRE_BENDER = "fire"


class TextNode():
    def __init__(self, text, text_type, url):
        self.text = text 
        self.text_type = text_type
        self.url = url 

    def __eq__(self, other):
        if isistance(other, TextNode):
            return self.text_type == other.text_type
        

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
