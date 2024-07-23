def test_function():
    print("Вызов test_function")

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

    try:
        inner_function()
    except NameError as e:
        print(f"Ошибка при вызове inner_function: {e}")

if __name__ == "__main__":
    test_function()
