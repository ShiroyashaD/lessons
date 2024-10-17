def test_function():
    def inner_function():
        return('Я в зоне видимости функции test_funtion')
    return(inner_function())
print(test_function())
print(inner_function())