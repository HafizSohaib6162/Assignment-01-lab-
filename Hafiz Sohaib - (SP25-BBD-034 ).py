
print('''______---------****************** Choose one option (1-10)
1 - Print all even numbers from 2 to 20
2 - Print each name in uppercase
3 - Print numbers from 10 to 1 in reverse order
4 - Print numbers divisible by 3
5 - Print squares of numbers from 1 to 10
6 - Convert Celsius to Fahrenheit
7 - Multiplication table of 5
8 - Sum of all numbers in a list
9 - Iterate through a string and print each character
10 - Print words with more than 5 letters____------------*****************************
''')

# Take user input
choice = int(input("Enter your choice (1-10): "))

# Match case statement to handle the user's choice
match choice:
    case 1:
        # Print all even numbers from 2 to 20
        for i in range(2, 21, 2):
            print(i)

    case 2:
        # Print each name in uppercase
        names = ["azaam", "alI", "emaan", "sohaib"]
        for name in names:
            print(name.upper())

    case 3:
        # Print numbers from 10 to 1 in reverse order
        for i in range(10, 0, -1):
            print(i)

    case 4:
        # Print numbers divisible by 3
        numbers = [12, 34, 9, 27, 18]
        for num in numbers:
            if num % 3 == 0:
                print(num)

    case 5:
        # Print squares of numbers from 1 to 10
        for i in range(1, 11):
            print(i ** 2)

    case 6:
        # Convert Celsius to Fahrenheit
        temp_cels = [0, 20, 30, 40, 50]
        temp_fahren = []
        for temp in temp_cels:
            fahren = (temp * 9/5) + 32
            temp_fahren.append(fahren)
        print(temp_fahren)

    case 7:
        # Multiplication table of 5
        for i in range(1, 11):
            print(f"5 x {i} = {5 * i}")

    case 8:
        # Sum of all numbers in a list
        nums = [3, 7, 12, 19, 6]
        total_sum = 0
        for num in nums:
            total_sum += num
        print(f"Sum: {total_sum}")

    case 9:
        # Iterate through a string and print each character
        string = "hayyyyyyyyyyyyyyyyyyyyyyyyyyyyy, I AM STUDENT"
        for char in string:
            print(char)

    case 10:
        # Print words with more than 5 letters
        words = ["elephant", "cat", "giraffe", "dog", "hippopotamus"]
        for word in words:
            if len(word) > 5:
                print(word)

    case _:
        print("Invalid choice! Please select a number between 1 and 10.")
