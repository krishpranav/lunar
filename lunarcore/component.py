from lunarcore.tailwind import Tailwind

class Component(Tailwind):
    """
    keep track of ids an instances
    """
    next_id = 1
    instances = {}    