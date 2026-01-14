import std.math
import std.io

data Point2D(x: Float, y: Float)

data Point3D(x: Float, y: Float, z: Float):
    fun toPoint2D(): Point2D =
        Point2D(x, y)
    
    fun +(other: Point3D): Point3D =
        Point3D(x + other.x, y + other.y, z + other.z)

fun distanceFrom(a: Point2D, b: Point2D, &IO): Float =
    io.println(f"Calculating distance between points: {a} and {b}")
    let dx = a.x - b.x
    let dy = a.y - b.y
    let distSquared = math.pow(dx, 2) + math.pow(dy, 2)
    math.sqrt(distSquared)

-- alternative syntax
distanceFrom2 : (Point2D, Point2D, &IO) -> Float
distanceFrom2 = (a, b) ->
    io.println(f"Calculating distance between points: {a} and {b}")
    let dx = a.x - b.x
        dy = a.y - b.y
        distSquared = math.pow(dx, 2) + math.pow(dy, 2)
    in math.sqrt(distSquared)

a = Point2D(3.0, 4.0)
b = Point2D(0.0, 0.0)
distance = distanceFrom(a, b)

c = Point3D(1.0, 2.0, 3.0)
d = Point3D(
    ..c
    z = 6.0
)
