enum A {
    X
    Y
    Z
}

enum B {
    FIRST = 1
    SECOND = 2
    THIRD = 3
}

enum C {
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
}

enum D {
    UP = (0, 1)
    DOWN = (0, -1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
}

enum E {
    FOURTH = 4
    FIFTH = 5
    & B
}

enum F {
    Point2D(x: float, y: float)
    Point3D(x: float, y: float, z: float)
}

b = B::SECOND
c = C::RED
d = D::LEFT
f2d = F::Point2D(3.0, 4.0)
