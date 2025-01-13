class Boardgame:
    def __init__(self, game_name, image, image_small, description, year_published, min_players, max_players, min_playtime, max_playtime, min_age, designers, artists, publishers):
        self.game_name = game_name
        self.image = image
        self.image_small = image_small
        self.description = description
        self.year_published = year_published
        self.min_players = min_players
        self.max_players = max_players
        self.min_playtime = min_playtime
        self.max_playtime = max_playtime
        self.min_age = min_age
        self.designers = designers
        self.artists = artists
        self.publishers = publishers