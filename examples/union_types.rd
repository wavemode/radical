type A = { a: Int }
type B = { b: Int }
type C = { c: Int }

type ExampleUnion = A | B | C | Float

w: ExampleUnion = {
    a = 25
}

x: ExampleUnion = {
    b = 50
}

y: ExampleUnion = {
    c = 100
}

z: ExampleUnion = 10.5
