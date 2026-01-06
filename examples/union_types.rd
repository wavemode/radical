type A { a: int }
type B { b: int }
type C { c: int }

type ExampleUnion = A | B | C | float
// alternatively (since equals sign is optional):
// type ExampleUnion A | B | C | float

X: ExampleUnion {
    b = 50
}

Y: ExampleUnion {
    c = 100
}

Z: ExampleUnion = 10.5
// alternatively:
// Z 10.5
