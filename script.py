def greet(name):
        """This function greets the person passed in as a parameter"""
            print("Hello, " + name + ". How are you today?")

            def print_square(n):
                    """This function prints a square of asterisks of size n"""
                        for i in range(n):
                                    print("*" * n)

                                    person = input("Enter your name: ")
                                    greet(person)

                                    num = int(input("Enter the size of the square: "))
                                    print_square(num)

