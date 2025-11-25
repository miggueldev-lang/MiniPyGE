import os

class AssetsManeger:
    def __init__(self, pygame):
        self.pygame = pygame
        self.base_path = "assets/"

        self.images = {}
        self.sounds = {}
        self.fonts = {}

        self.images_path = os.path.join(self.base_path, "images/")
        self.sounds_path = os.path.join(self.base_path, "sounds/")
        self.music_path = os.path.join(self.base_path, "music/")
        self.fonts_path = os.path.join(self.base_path, "fonts/")

    def load_image(self, name):
        if name in self.images:
            return self.images[name]
        
        path = os.path.join(self.images_path, name)
        
        try: 
            image = self.pygame.image.load(path).convert_alpha()
            self.images[name] = image
            return image
        except Exception as e:
            print(f"Error loading image {name}: {e}")
            return None
    
    def image(self, name):
        return self.load_image(name)
    
    def load_sound(self, name):
        if name in self.sounds:
            return self.sounds[name]
        
        path = os.path.join(self.sounds_path, name)

        try:
            sound = self.pygame.mixer.Sound(path)
            self.sounds[name] = sound
            return sound
        except Exception as e:
            print(f"Error loading sound {name}: {e}")
            return None
        
    def sound(self, name):
        return self.load_sound(name)
    
    def music(self, name):
        path = os.path.join(self.music_path, name)

        try:
            self.pygame.mixer.music.load(path)
        except Exception as e:
            print(f"Error loading music {name}: {e}")

    def play_music(self, name, loops=0):
        self.music(name)
        self.pygame.mixer.music.play(loops=loops)

    def load_font(self, name, size):
        key = (name, size)

        if key in self.fonts:
            return self.fonts[key]
        
        path = os.path.join(self.fonts_path, name)

        try:
            font = self.pygame.font.Font(path, size)
            self.fonts[key] = font
            return font
        except Exception as e:
            print(f"Error loading font {name} with size {size}: {e}")
            return None
    
    def font(self, name, size):
        return self.load_font(name, size)