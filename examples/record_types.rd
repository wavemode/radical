type ExampleRecord {
  a: int
  b: float
  c: str

  D: list[int] = [1, 2, 3, 4]
  E: (int, float, str) = (10, 20.0, "thirty")
}

F1 = {
  a = 40
  b = 50.0
  c = "sixty"
}

// equivalent to F1:
F2: ExampleRecord {
  a = 40
  b = 50.0
  c = "sixty"
}

// also equivalent to F1, due to structural typing:
F3 {
  a = 40
  b = 50.0
  c = "sixty"
}

// type embedding
type ChildRecord {
  & ExampleRecord
  d: float
  e: str
}

N: ChildRecord {
  d = 60.0
  e = "seventy"

  # embed the contents of F1
  & F1
}

// optional fields
type RecordWithNullableField {
  a?: int
  b: float
}

// satisfies the type bound
G1: RecordWithNullableField {
  b = 10.0
}

// extra fields
type RecordAllowingExtraFields {
  a: int
  & any
}

// satisfies the type bound
H1: RecordAllowingExtraFields {
  a = 20
  extra_field_1 = "hello"
  extra_field_2 = 30.5
}

// fields containing non-word characters
type RecordWithSpecialFieldNames {
  `field with spaces`: int
  `field-with-dash`: float
  `field.with.dot`: str
}

I1: RecordWithSpecialFieldNames {
  `field with spaces` = 1
  `field-with-dash` = 2.5
  `field.with.dot` = "three"
}
