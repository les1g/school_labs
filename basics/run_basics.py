def basics():
    """------------------------------------------------------
    The assignment is to get an integer from input, and
    output that integer squared, ending with newline.
    """
    print(basics.__doc__)
    user_num = int(input('Enter a number: '))
    num_squared = user_num * user_num

    print(f'{user_num} squared is {num_squared}.')
    print('------------------------------------------------------')
