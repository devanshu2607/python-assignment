def test_calculator():
    print("Testing calculator functions...")

    assert add(2, 3)== 5,"Addition test failed"

    assert substract(5, 3) ==2, "Subtraction test failed"

    assert multiply(4, 5) == 20, "Multiplication test failed"

    assert divide(10, 2) == 5, "Division test failed"

    if __name__ == "__main__":
     from calculator import add,substract,multiply,divide
    test_calculator()