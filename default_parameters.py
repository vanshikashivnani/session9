def greet4(first_name="John", last_name="Doe"):
    """
    Greet again
    :param first_name: default=John
    :param last_name: default=Doe
    :return: None
    """
    print(f"Hello {first_name} {last_name}, this is pretty cool, right?")

greet4('Vanshika', 'Shivnani')
greet4()
greet4('James')

greet4('Micheal', 'Jordan')
greet4(last_name='Jordan', first_name='Michael')

