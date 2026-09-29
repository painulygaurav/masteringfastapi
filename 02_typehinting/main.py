
text: str = "value"
percentage: int = 90
temp: float = 37.5

# if we can have potentially two types
number: int | float = 12

digits: list[int] = [1,2,3,4,5]

table_5: tuple[int] = (5,10,15,20,25)

def root(num: int | float, exp: float | None = .5) -> float:
  return pow(number, exp)

optional: str | None

optional = "value"

root_25 = root(25)







