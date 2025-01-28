class User:
    boardgame_library = []

    def __init__(self, username):
        self.username = username


    def add_game_to_boardgame_library(self, game: object):
        self.boardgame_library.append(game)


    # @staticmethod
    # def save_user(user: object):
    #     USER.append(user)