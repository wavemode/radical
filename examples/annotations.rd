-- any function can be used as an annotation
fun myAnnotation(param1: String, param2: Int): String =
    f"Annotation with param1={param1} and param2={param2}"

-- annotations can be applied to any declaration or field
-- annotations are stored as metadata of the module
@myAnnotation("test", 42)
fun annotatedFunction() = Null

anno1 = () -> 10.5

-- apply annotation without parameters
@anno1
var1 = "value"

anno2 = (param: String = "optional", flag: Bool): Null -> Null

@anno2(flag=True)
fun anno3(param: Int): Int =
    param * 2


-- apply annotation to a type declaration and its fields
@anno3(5)
type MyType = {
    @anno2("custom", False)
    field1: Int

    @anno3(10)
    field2: String
}
