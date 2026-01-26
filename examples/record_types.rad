type ExampleRecord = {
  a: Int
  b: Float
  c: String
}

f1: ExampleRecord = {
  a = 40
  b = 50.0
  c = "sixty"
}

-- equivalent to f1, due to structural typing:
f2 = {
  a = 40
  b = 50.0
  c = "sixty"
}

-- type embedding
type ChildRecord = {
  ...ExampleRecord
  d: Float
  e: String
}

n : ChildRecord = {
  d = 60.0
  e = "seventy"

  -- embed the contents of f1
  ...f1
}

-- records allow extra fields
type RecordAllowingExtraFields = {
  a: Int
}

-- satisfies the type bound
h1 : RecordAllowingExtraFields = {
  a = 20
  extraField1 = "hello"
  extraField2 = 30.5
}

-- fields containing non-word characters
type RecordWithSpecialFieldNames = {
  `field with spaces`: Int
  `field-with-dash`: Float
  `field.with.dot`: String
}

i1 : RecordWithSpecialFieldNames = {
  `field with spaces` = 1
  `field-with-dash` = 2.5
  `field.with.dot` = "three"
}
