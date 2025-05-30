# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def eat(number, need, remaining):
    """
    You're a hungry rabbit, and you already have eaten a certain number of carrots, 
    but now you need to eat more carrots to complete the day's meals.
    
    You should return an array of [ total number of eaten carrots after your meals, 
    the number of carrots left after your meals ]
    
    If there are not enough remaining carrots, you will eat all remaining carrots, 
    but will still be hungry.
    
    Example:
    * eat(5, 6, 10) -> [11, 4]
    * eat(4, 8, 9) -> [12, 1]
    * eat(1, 10, 10) -> [11, 0]
    * eat(2, 11, 5) -> [7, 0]
    
    Variables:
    @number : integer - the number of carrots that you have eaten.
    @need : integer - the number of carrots that you need to eat.
    @remaining : integer - the number of remaining carrots that exist in stock
    
    Constrain:
    * 0 <= number <= 1000
    * 0 <= need <= 1000
    * 0 <= remaining <= 1000
    """
    # Check if there are enough remaining carrots
    if remaining >= need:
        # If there are enough carrots, eat what you need
        total_eaten = number + need
        carrots_left = remaining - need
    else:
        # If there aren't enough carrots, eat all remaining carrots
        total_eaten = number + remaining
        carrots_left = 0
    
    return [total_eaten, carrots_left]