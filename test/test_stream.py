import unittest

from test.data.film import Film, Genre
from stream.stream import stream


class TestStream(unittest.TestCase):

    def setUp(self):
        # duplicate film
        toy_story = Film("Toy Story", Genre.ANIMATION, 10.00)

        self.films = [
            Film("Harry Potter", Genre.SCIENCE_FICTION, 10.50),
            Film("Iron Man", Genre.SCIENCE_FICTION, 11.00),
            Film("Spotlight", Genre.DRAMA, 8.50),
            Film("Mission Impossible", Genre.ACTION, 12.00),
            toy_story,
            Film("Winnie the Pooh", Genre.ANIMATION, 10.00),
            toy_story,
            Film("The Big Short", Genre.DRAMA, 8.50),
            Film("Fast and Furious", Genre.ACTION, 11.00),
            Film("Parasite", Genre.DRAMA, 13.00)
        ]

    def test_all(self):
        # when
        films_all_action = stream(self.films).all(lambda film: film.genre == Genre.ACTION)
        films_all_cost_more_than_5 = stream(self.films).all(lambda film: film.price > 5.00)

        # then
        self.assertFalse(films_all_action)
        self.assertTrue(films_all_cost_more_than_5)

    def test_any(self):
        # when
        includes_action = stream(self.films).any(lambda film: film.genre == Genre.ACTION)
        includes_cost_over_20 = stream(self.films).any(lambda film: film.price > 20.00)

        # then
        self.assertFalse(includes_cost_over_20)
        self.assertTrue(includes_action)

    def test_count(self):
        # when
        count = stream(self.films).count()

        # then
        self.assertEqual(count, 10)

    def test_find_first(self):
        # when
        first_action_film = stream(self.films).find_first(lambda film: film.genre == Genre.ACTION)

        # then
        self.assertEqual(first_action_film.name, "Mission Impossible")

    def test_for_each(self):
        # given
        action_films = []

        def add_action_film(film: Film) -> None:
            if film.genre == Genre.ACTION:
                action_films.append(film)

        # when
        stream(self.films).for_each(add_action_film)

        # then
        self.assertEqual(len(action_films), 2)

    def test_list(self):
        # when
        films = stream(self.films).list()

        # then
        self.assertEqual(len(films), 10)

    def test_max(self):
        # when
        maximum = stream([1, 2, 3, 4]).max()

        # then
        self.assertEqual(maximum, 4)

    def test_min(self):
        # when
        minimum = stream([1, 2, 3, 4]).min()

        # then
        self.assertEqual(minimum, 1)

    def test_sum(self):
        # when
        total = stream([1, 2, 3, 4]).sum()

        # then
        self.assertEqual(total, 10)

    def test_distinct(self):
        # when
        distinct_films = stream(self.films).distinct().list()

        # then
        self.assertEqual(len(distinct_films), 9)

    def test_filter(self):
        # when
        no_action_films = stream(self.films).filter(lambda film: film.genre != Genre.ACTION).list()

        # then
        self.assertEqual(len(no_action_films), 8)

    def test_map(self):
        # when
        prices = stream(self.films).map(lambda film: film.price).list()

        # then
        self.assertEqual(prices,  [10.5, 11, 8.5, 12, 10, 10, 10, 8.5, 11, 13])

    def test_limit(self):
        # when
        limited_films = stream(self.films).limit(8).list()

        # then
        self.assertEqual(len(limited_films), 8)

    def test_skip(self):
        # when
        films_with_skips = stream(self.films).skip(2).list()

        # then
        self.assertEqual(len(films_with_skips), 8)

    def test_sort(self):
        # when
        sorted_list = stream([5, 1, 3, 2, 4]).sort().list()

        # then
        self.assertEqual(sorted_list, [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()
