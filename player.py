from abc import ABC, abstractmethod


class Player(ABC):

    def __init(self, id: int):
        self._id = id

    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def update_game(self, game):
        pass

    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def destroy(self):
        pass

