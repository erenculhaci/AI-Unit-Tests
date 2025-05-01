# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def bf(planet1, planet2):
    '''
    There are eight planets in our solar system: the closerst to the Sun 
    is Mercury, the next one is Venus, then Earth, Mars, Jupiter, Saturn, 
    Uranus, Neptune.
    Write a function that takes two planet names as strings planet1 and planet2. 
    The function should return a tuple containing all planets whose orbits are 
    located between the orbit of planet1 and the orbit of planet2, sorted by 
    the proximity to the sun. 
    The function should return an empty tuple if planet1 or planet2
    are not correct planet names. 
    Examples
    bf("Jupiter", "Neptune") ==> ("Saturn", "Uranus")
    bf("Earth", "Mercury") ==> ("Venus")
    bf("Mercury", "Uranus") ==> ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
    '''
    # Define the planets in order of proximity to the Sun
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")
    
    # Check if both planets are valid
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get the indices of the planets
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    # Determine the range (inclusive of endpoints would be wrong)
    start_idx = min(idx1, idx2) + 1
    end_idx = max(idx1, idx2)
    
    # Return the planets between planet1 and planet2
    return planets[start_idx:end_idx]