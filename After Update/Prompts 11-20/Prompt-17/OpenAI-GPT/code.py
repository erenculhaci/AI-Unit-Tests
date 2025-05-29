# @Authors
# Student Names: Eren CULHACI, İrem TAZE, Kaan KARATAŞ
# Student IDs: 150220763, 150200086, 150200081

def bf(planet1, planet2):

    # List of planets in order of proximity to the Sun
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

    # Check if inputs are strings and valid planet names
    if not isinstance(planet1, str) or not isinstance(planet2, str):
        return ()
    if planet1 not in planets or planet2 not in planets:
        return ()

    # Get the indices of the two planets
    index1 = planets.index(planet1)
    index2 = planets.index(planet2)

    # Determine the range of planets between the two indices
    start, end = sorted([index1, index2])
    return tuple(planets[start + 1:end])