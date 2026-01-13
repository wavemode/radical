a: int = 5

b: float = 5.0

c: str = "five"

d: bool = true

// list
e: list[int] = [1, 2, 3, 4, 5]

// equivalent to e (commas are optional in lieu of newlines)
e2 = [
    1
    2
    3
    4
    5
]

// tuple
f: (int, float, str) = (10, 20.0, "thirty")

// dictionary / map
g: map[str, int] = {
    one = 1
    two = 2
    three = 3
}

// equivalent to g (bracket syntax)
["g2"] = {
    ["one"] = 1
    ["two"] = 2
    ["three"] = 3
}

// set
h: set[int] = {1, 2, 3, 4, 5, 4, 3, 2, 1}  // duplicates will be ignored

// equiavlent to h (commas are optional in lieu of newlines)
h2 = {
    1
    2
    3
    4
    5
    4
    3
    2
    1
}

// tree
i: tree[('name', str) | ('other_name', tree[('child1', int), ('child2', float)])] = {
    name "value"
    name "value2"
    name "value3"
    other_name {
        child1 10
        child2 20.0
    }
}

// equivalent to i.to_list()
["i2"] = [
    ("name", "value")
    ("name", "value2")
    ("name", "value3")
    ("other_name", {
        ("child1", 10)
        ("child2", 20.0)
    })
]

// equivalent to i.to_map()
i3: { 'name': str, 'other_name': { 'child1': int, 'child2': float } } = {
    // since this is a hashmap, only the last 'name' entry would be kept
    name = "value3"
    other_name = {
        child1 = 10
        child2 = 20.0
    }
}

j: null = null
j2: int | null = null  // nullable value

k: any = "can be anything"
