def make_bricks(small, big, goal):
    """
    We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
    """
    max_big = big * 5
    if small + max_big < goal:
        return False
    
    if max_big >= goal:
        return goal % 5 <= small
    
    return (goal - max_big) <= small