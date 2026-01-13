import std::math

data Point2D(x: float, y: float)
data Point3D(x: float, y: float, z: float)

fun distance_from(a: Point2D, b: Point2D): float {
    return math::sqrt(math::pow(a.x - b.x, 2) + math::pow(a.y - b.y, 2))
}

a = Point2D(3.0, 4.0)
b = Point2D(0.0, 0.0)
distance = distance_from(a, b)

c = Point3D(1.0, 2.0, 3.0)
d = Point3D(
    x = 4.0,
    y = 5.0,
    z = 6.0,
)

