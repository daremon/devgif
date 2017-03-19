import os
import json
import random

GIFS = []
NOT_FOUND_GIFS = [
    'https://media.giphy.com/media/12zV7u6Bh0vHpu/giphy.gif',
    'https://media.giphy.com/media/12zV7u6Bh0vHpu/giphy.gif',
    'https://media.giphy.com/media/l0MYHq0IFikDrVQOc/giphy.gif',
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
    Returns a URL to the top ranked gif or one of the not-found gifs

    """
    _load()

    results = []
    for gif in GIFS:
        if q.lower() in gif[0].lower():
            results.append(gif[1])

    if not results:
        results = NOT_FOUND_GIFS

    return random.choice(results)
