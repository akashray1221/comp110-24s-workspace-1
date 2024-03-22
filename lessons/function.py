def bar(a: str) -> None:
    print(foo(1,a))

def foo(a: int, b: str) -> int:
    return a + len(b)

print(bar("Comp"))