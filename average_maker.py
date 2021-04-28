def find_average():
    numbers = input('Enter each number with a space without comma >>> ')
    print("\n")
    number_list = numbers.split()
    number_list = list(map(int, number_list)) 
    len_list = len(number_list)
    sum_list = sum(number_list)
    average = sum_list / len_list
    print(f"Average Value: {average}")
    