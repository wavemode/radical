example1(x: Int, y: Int) -> Int =
    x + y

-- alternative syntax
example2 : (Int, Int) -> Int
example2 = (x, y) -> x + y

-- variadic function
sumAll : (...Int) -> Int
sumAll = (...nums) ->
    -- simpler would be nums.fold(0, _ + _)
    let helper(index, acc) =
        if index >= nums.length then
            acc
        else
            helper(index + 1, acc + nums[index])
    in
        helper(0, 0)

-- generic function
sumAllGeneric : [T]((T, T) -> T, ...T) -> T
sumAllGeneric[T](combiner: fun(T, T) -> T, ...items: T) -> T =
    let helper(index: Int, acc: T): T =
        if index >= items.length then
            acc
        else
            helper(index + 1, combiner(acc, items[index]))
    in
        helper(1, items[0])

sumAllGenericConstrained : [T : Numeric](...T) -> T
sumAllGenericConstrained[T : Numeric](...items: T) -> T =
    sumAllGeneric[T](_ + _, ...items)
