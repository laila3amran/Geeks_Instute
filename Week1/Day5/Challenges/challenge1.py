import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        """Initialize Circle with radius or diameter."""
        if radius is not None:
            self._radius = float(radius)
        elif diameter is not None:
            self._radius = float(diameter) / 2
        else:
            raise ValueError("You must provide either a radius or a diameter.")

   
    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    
    def area(self):
        """Return area of the circle."""
        return math.pi * (self._radius ** 2)

    
    def __str__(self):
        """Return readable description of the circle."""
        return f"Circle(radius={self.radius:.2f}, diameter={self.diameter:.2f}, area={self.area():.2f})"

    def __add__(self, other):
        """Add two circles: new radius = sum of radii."""
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __eq__(self, other):
        """Check equality based on radius."""
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        """Less than, based on radius."""
        if isinstance(other, Circle):
            return self.radius < other.radius
        return NotImplemented

    def __gt__(self, other):
        """Greater than, based on radius."""
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented
