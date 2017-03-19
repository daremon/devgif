import os
import json
import random

# title, url, likes
GIFS = []
NOT_FOUND_GIFS = [
    ['Nothing found', 'https://media.giphy.com/media/12zV7u6Bh0vHpu/giphy.gif', 0],
    ['Nothing found', 'https://media.giphy.com/media/l0MYHq0IFikDrVQOc/giphy.gif', 0],
]


def _load():
    """
    Load all gifs from json in a global var.
    """
    global GIFS
    if not GIFS:
        path = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(path, 'gifs.json'), 'r') as infile:
            GIFS = json.load(infile)


def get(q):
    """
    :: q What to search for
    Returns [title, URL, likes] for the top ranked gif (or a not-found gif)

    """
    _load()

    # rank gifs by number of words included in title
    gif_ranking = {}
    max_score = 0
    words = q.lower().split()
    for i, gif in enumerate(GIFS):
        for word in words:
            if word in gif[0].lower():
                gif_ranking[i] = gif_ranking.get(i, 0) + 1
                if gif_ranking[i] > max_score:
                    max_score = gif_ranking[i]

    # nothing matched
    if not gif_ranking:
        return random.choice(NOT_FOUND_GIFS)

    # return random result of max scorers
    results = [GIFS[x] for x in gif_ranking if gif_ranking[x] == max_score]
    return random.choice(results)
