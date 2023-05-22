# def check_values_existence(input_values, tuple_of_subtuples):
#     # Create a set of values from the tuple_of_subtuples
#     tuple_values = set(subtuple[0] for subtuple in tuple_of_subtuples)

#     # Check if all input_values exist in tuple_values
#     for value in input_values:
#         if value not in tuple_values:
#             return False

#     return True

# # Define your tuple of sub-tuples
# tuple_of_subtuples = ((1, 3), (2, 2), (3, 1))

# # Get user input values
# user_input = []
# for i in range(6):
#     value = input(f"Enter value {i + 1}: ")
#     user_input.append(value)

# # Call the function to check if all input values exist
# all_exist = check_values_existence(user_input, tuple_of_subtuples)

# # Print the result
# if all_exist:
#     print("All input values exist in the tuple!")
# else:
#     print("Not all input values exist in the tuple.")




# def check_values_existence(input_values, tuple_of_subtuples):
#     # Create a set of values from the tuple_of_subtuples
#     tuple_values = set(subtuple[0] for subtuple in tuple_of_subtuples)

#     # Check if all input_values exist in tuple_values
#     for value in input_values:
#         if value not in tuple_values:
#             return False

#     return True

# # Define your tuple of sub-tuples
# tuple_of_subtuples = ((1, 3), (2, 2), (3, 1))

# # Get user input values
# user_input = []
# for i in range(6):
#     value = input(f"Enter value {i + 1}: ")
#     user_input.append(value)

# # Call the function to check if all input values exist
# all_exist = check_values_existence(user_input, tuple_of_subtuples)

# # Print the result
# if all_exist:
#     print("All input values exist in the tuple!")
# else:
#     print("Not all input values exist in the tuple.")

def check_user_inputs(input_values, tuple_of_subtuples):
    # Create a dictionary to store the values and their counters
    tuple_dict = dict(tuple_of_subtuples)

    # Check if all input_values exist in tuple_dict and if the counters are valid
    for value in input_values:
        if value in tuple_dict[value] :
            tuple_dict[value] -= 1
        

        


        # if value not in tuple_dict or tuple_dict[value] <= 0:
        #     return False

        # tuple_dict[value] -= 1

    return True


# Define your tuple of sub-tuples
tuple_of_subtuples = ((1, 3), (2, 2), (3, 1))

# Get user input values
user_input = []
for i in range(6):
    value = input(f"Enter value {i + 1}: ")
    user_input.append(value)

# Call the function to check user inputs and detect cheating
valid_inputs = check_user_inputs(user_input, tuple_of_subtuples)

# Print the result
if valid_inputs:
    print("All input values are valid and exist in the tuple!")
else:
    print("Invalid input values or cheating detected.")
