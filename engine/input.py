class InputManeger:
    def __init__(self, pygame):
        self.pygame = pygame

        self.bindings = {
            "move_right": pygame.K_d,
            "move_left": pygame.K_a,
            "move_up": pygame.K_w,
            "move_down": pygame.K_s,
            "jump": pygame.K_SPACE,
            "confirm": pygame.K_RETURN,
            "cancel": pygame.K_ESCAPE,
        }
        self.key_states = {}
        self.key_pressed = set()
        self.key_released = set()
        self.last_key = None

    def bind_key(self, key, action):
        self.bindings[action] = key

    def update(self, events):
        self.key_pressed.clear()
        self.key_released.clear()

        for event in events:
            if event.type == self.pygame.KEYDOWN:
                key = event.key
                self.key_pressed.add(key)
                self.key_states[key] = True
                self.last_key = key
            
            elif event.type == self.pygame.KEYUP:
                key = event.key
                self.key_released.add(key)
                self.key_states[key] = False

    def is_key_pressed(self, action):
        if action not in self.bindings: return False
        key = self.bindings[action]
        return key in self.key_pressed
    
    def is_key_released(self, action):
        if action not in self.bindings: return False
        key = self.bindings[action]
        return key in self.key_released

    def is_key_held(self, action):
        if action not in self.bindings: return False
        key = self.bindings[action]
        return self.key_states.get(key, False)
    
    def is_raw_pressed(self, key):
        return key in self.key_pressed
    
    def is_raw_held(self, key):
        return self.key_states.get(key, False)
    
    def is_raw_released(self, key):
        return key in self.key_released