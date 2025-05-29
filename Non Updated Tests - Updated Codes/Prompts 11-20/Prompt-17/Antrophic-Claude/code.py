# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def bf(planet1, planet2):
    # List of planets in order from the Sun
    planets = ("Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune")

    # Input validation
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 not in planets or planet2 not in planets:
        return ()
    
    # Get indices
    idx1 = planets.index(planet1)
    idx2 = planets.index(planet2)
    
    # Get planets strictly between them (regardless of order)
    start = min(idx1, idx2) + 1
    end = max(idx1, idx2)
    
    return planets[start:end]
