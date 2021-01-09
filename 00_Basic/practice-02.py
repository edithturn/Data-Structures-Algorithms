# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    # Your code goes here!
    # Initializing the starting of i to count until 5
    i = 0
    # Declaring a string with a text , I am adding an extra expace at the end
    my_string = "I am super excited for this course!" + " "
    # Declaring a new empty variable, It will be the final string to return
    total_string = ""
    # Init the proces in zero, this will stop when i = 5
    while i < 5:
        # Concatenating my old strign with the new one (05 times)
        total_string += my_string
        # Increase the counter in one
        i += 1
    # Return the final concatenation of the 05 times the string
    return total_string
    
# Calling to the function who return the big string
print(show_excitement())