import random

def generate_random_number(start, end):
    '''
    Generates a random number between start and end.
    Args:
        start: int
        end: int
    Returns:
        int: A random number between start and end. 
    '''
    return random.randint(start, end)