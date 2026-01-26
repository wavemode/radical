a : Int
a = 5

b : Float
b = 5.0

c : String
c = "five"

c2 : Char
c2 = 'f'

c3 : Char
c3 = c[0]

d : Bool
d = true

e : List[Int]
e = [1, 2, 3, 4, 5]

-- equivalent to e (commas are optional in lieu of newlines)
e2 = [
    1
    2
    3
    4
    5
]

f : (Int, Float, String)
f = (10, 20.0, "thirty")

-- dictionary / map
g : Map[String, Int]
g = {
    one = 1
    two = 2
    three = 3
}

-- equivalent to g (bracket syntax)
g2 = {
    ["one"] = 1
    ["two"] = 2
    ["three"] = 3
}

h : Set[Int]
h = {1, 2, 3, 4, 5, 4, 3, 2, 1}  -- duplicates will be ignored

-- equiavlent to h (commas are optional in lieu of newlines)
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

i : Tree[("name", String) | ("other_name", Tree[("child1", Int), ("child2", Float)])]
i = {
    name "value"
    name "value2"
    name "value3"
    other_name {
        child1 10
        child2 20.0
    }
}

-- equivalent to i.to_list()
i2 = [
    ("name", "value")
    ("name", "value2")
    ("name", "value3")
    ("other_name", {
        ("child1", 10)
        ("child2", 20.0)
    })
]

-- equivalent to i.to_map()
i3 : { name : String, other_name : { child1 : Int, child2 : Float } }
i3 = {
    -- since this is a hashmap, only the last "name" entry would be kept
    name = "value3"
    other_name = {
        child1 = 10
        child2 = 20.0
    }
}

j : Null
j = null

-- nullable value
j2 : Int | Null
j2 = null

k : Any
k = "can be anything"
