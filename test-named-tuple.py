# Source: https://levelup.gitconnected.com/python-features-you-probably-dont-know-about-but-should-a66c6b30c528

from collections import namedtuple

Coordinate = namedtuple("Coordinate", "longitude latitude")
location = Coordinate(90, 37.5)
print("location:", location)

# accessing attributes with dot notation
print(location.longitude, location.latitude)
