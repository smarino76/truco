from player import Player


class AI_Agent(Player):


    def __init__(self, id, model=None):
        super().__init__(id)
        if model is not None:
            self.model = model
            self.required_trainig = False
        else:
            self.required_trainig = True


    def reset(self):
        pass

    
    def update_game(self, game):
        pass

    
    def play(self):
        pass
    

    def destroy(self):
        pass