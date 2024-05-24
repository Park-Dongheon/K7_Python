class Setting:
    def __init__(self):
        self.config = {
            'right_pressed':False,
            'left_pressed':False,
            'ship_image_path':'0524_alien_invasion_review/images/ship.bmp',
            'alien_image_path':'0524_alien_invasion_review/images/alien.bmp',
            'ship_speed':10,
        }


    def get(key):
        return self.config(key)
    
    def set(self, key, value):
        self.config[key] = value