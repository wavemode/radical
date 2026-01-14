type A =
    "X"
    | "Y"
    | "Z"

let first = 1
let second = 2
let third = 3
type B =
    first
    | second
    | third

let red = "red"
let green = "green"
let blue = "blue"
type C =
    red
    | green
    | blue


let up = (0, 1)
let down = (0, -1)
let left = (-1, 0)
let right = (1, 0)
type D = up | down | left | right

let type FOURTH = 4
let type FIFTH = 5
type E =
    FOURTH
    | FIFTH
    | B

let data Point2D(x: Float, y: Float)
let data Point3D(x: Float, y: Float, z: Float)
type F = Point2D | Point3D
