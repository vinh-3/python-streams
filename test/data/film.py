from enum import Enum


class Genre(Enum):
    ACTION = 1
    ANIMATION = 2
    DRAMA = 3
    SCIENCE_FICTION = 4


class Film:
    def __init__(self, name: str, genre: Genre, price: float):
        self.name = name
        self.genre = genre
        self.price = price

    def __repr__(self):
        return self.name

