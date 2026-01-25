import Core.Math
import Core.System


strSum(s) = s |> words |> map(parseInt, ~) |> sum

data Obj()

data Point2D(x: Float, y: Float)
data Point3D(x: Float, y: Float, z: Float)
type Point = Point2D | Point3D

proc distanceFrom(a: Point2D, b: Point2D) -> Float of
    let
        sub(a: Float, b: Float) -> Float =
            let
                -- even though we're in the body of the function sub, we can still call
                -- effectful procedures because of the surrounding proc environment
                _ = System.println(f"Calculating distance between points: {a} and {b}")

                difference = a - b
            in
                difference
        dx = sub(a.x, b.x)
        dy = sub(a.y, b.y)
        distSquared = Math.pow(dx, 2) + Math.pow(dy, 2)
    in
        Math.sqrt(distSquared)

distanceFrom2 : proc(Point2D, Point2D) -> Float
distanceFrom2 = proc(a, b) of
    System.println(f"Calculating distance between points: {a} and {b}")

    -- sub, dx, and dy have no actual type, and for now are just templates.
    -- upon use, a type for their arguments and return value will be inferred
    -- (or, an error will be raised if a specific type cannot be inferred).
    let sub(a, b) = a - b
    let dx(a, b) = sub(a.x, b.x)
    let dy(a, b) = sub(a.y, b.y)

    -- dxab, dyab and distSquared are variables, so a concrete type must now be inferred.
    -- since a and b are known to be Point2D, template evaluation will infer that dx and dy
    -- both return Float, since Point2D.x and Point2D.y are both Float, and thus distSquared
    -- is also Float.
    let dxab = dx(a, b)
        dyab = dy(a, b)
        distSquared = Math.pow(dxab, 2) + Math.pow(dyab, 2)

    -- the last expression of a proc is its return value
    Math.sqrt(distSquared)

a = Point2D(3.0, 4.0)
b = Point2D(0.0, 0.0)
distance = distanceFrom(a, b)

c = Point3D(1.0, 2.0, 3.0)
d = Point3D(
    ...c
    z = 6.0
)

proc main() of
    System.println(f"Distance between a and b: {distance}")
    System.println(f"Point d: {d}")
