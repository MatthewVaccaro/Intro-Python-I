# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Class LatLon Works
# testClass = LatLon(22, 33)
# print(testClass.lon)

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    
    def __str__(self):
        return ' lat: {}, lon: {}, Name: {}'.format(self.lat, self.lon, self.name)

# Class Waypoints works
# testClass = Waypoint(66, 33, "doop")
# print(testClass.name)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size
    
    def __str__(self):
        return ' Name: {}, Difficulty: {}, Size: {}, lat: {}, lon: {}, '.format(self.name, self.difficulty, self.size, self.lat, self.lon) 

# Class Geocache works
# testClass = Geocache(66, 33, "Boopers", 10, "4000 Miles")
# print(testClass.size)


# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
point1 = Waypoint(41.70505, -121.51521, "Catacombs")
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(point1)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
newGeo = Geocache(44.052137,-121.41556, "Newberry Views", 1.5, 2 )

# Print it--also make this print more nicely
print(newGeo)
