# Python Streams

In Java, the [Streams API](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/stream/Stream.html) provides
a convenient way to operate on collections of elements in a functional / declarative manner. This project is an attempt 
to create a Python equivalent. 

There are two key operations that can be performed on a stream:
- Intermediate operations - act on the underlying elements in the stream and return a stream. These methods can therefore 
be chained together.
- Terminal operations - act on the elements of the stream to return a final result.

Note: Python's list comprehension offers a concise syntax to work with lists, however streams offer a functional syntax that allows the chaining of multiple operations.

## Usage Example
Consider the following film class.
```python
class Film:
    def __init__(self, name: str, genre: str, price: float):
        self.name = name
        self.genre = genre
        self.price = price
```
Given a list of film objects, find the total cost of all films with the genre "HORROR" using `stream()`.
```python
# films is a list of Film objects

total_cost = stream(films) \
    .filter(lambda film: film.genre == 'HORROR') \
    .map(lambda film: film.price) \
    .sum()
```
Given a list of film objects, return the unique genres ordered alphabetically using `stream()`.
```python
# films is a list of Film objects

genres = stream(films) \
    .map(lambda film: film.genre) \
    .distinct() \
    .sort() \
    .list()
```
In the examples above, the intermediate methods are `filter()`, `map()`, `distinct()` and `sort()`. The terminal operations are `sum()` and `list()`.


