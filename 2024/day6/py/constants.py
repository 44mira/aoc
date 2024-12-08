from dataclasses import dataclass, replace

X_MAX, Y_MAX = 0, 0


@dataclass(frozen=True, slots=True)
class P:
    x: int
    y: int

    def __add__(self, obj):
        return P(self.x + obj.x, self.y + obj.y)


@dataclass(frozen=True, slots=True)
class D:
    x: int
    y: int

    def turn(self):
        return D(-self.y, self.x)


@dataclass(slots=True)
class G:
    direction: D
    coordinates: P

    def __hash__(self):
        return hash(str(self))

    def move(self):
        self.coordinates = self.coordinates + self.direction

    def turn(self):
        self.direction = self.direction.turn()

    def clone(self):
        return replace(self)
