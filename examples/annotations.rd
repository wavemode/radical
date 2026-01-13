// any value can be used as an annotation
fun my_annotation(param1: string, param2: int) -> string {
    return f"Annotation with param1={param1} and param2={param2}"
}

// annotations can be applied to any declaration or field
// the annotation becomes a dynamic property of the key (not of the value)
@my_annotation("test", 42)
fun annotated_function() {
    // function body
}

anno1 = 10.5

@anno1
var1 = "value"

anno2 = fun(param: string, flag: bool) -> null {
    return null
}
@anno2(param="example", flag=true)

fun anno3(param: int) -> int {
    return param * 2
}

@anno3(5)
type MyType {
    field1: int
    field2: string
}
