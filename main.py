import numpy as np


data = input("Enter a list of numbers separated by spaces: ")
user_data = data.split()
int_data = map(int, user_data)
data_array = np.array(list(int_data))

def calculate_mode(data_array):
    values , counts = np.unique(data_array, return_counts = True)
    mode_index = np.argmax(counts)
    mode = values[mode_index]
    return mode

print("The following statistics can be calculated:")
print(" 1. Mean \n 2. Median \n 3. Mode \n 4. Standard Deviation \n 5. Variance \n 6. Maximum \n 7. Minimum")
selection = input("Choose a statistic to calculate(1-7): ")

if selection == "1":
    mean = np.mean(data_array)
    print(f"The mean is: {mean}")

elif selection == "2":
    median = np.median(data_array)
    print(f"The median is: {median}")

elif selection == "3":  
    mode = calculate_mode(data_array)
    print(f"The mode is: {mode}") 

elif selection == "4":
    std_dev = np.std(data_array)
    print(f"The standard deviation is: {std_dev}")

elif selection == "5":
    variance = np.var(data_array)
    print(f"The variance is: {variance}")

elif selection == "6":
    maximum = np.max(data_array)
    print(f"The maximum is: {maximum}")

elif selection == "7":
    minimum = np.min(data_array)
    print(f"The minimum is: {minimum}")
