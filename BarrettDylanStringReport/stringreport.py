# This program is designed to create a report	
# about a string entered by the user at a prompt.	

# Establish a count.
count = 0

# Ask the user for the string.
get_string = (input("Enter a string: "))

# Determine if the string is 0 characters in length.
if not get_string:
    print("You did not enter anything!")
    

else:    
    for line in get_string:
        # Count the characters in the string.
        count += 1

        # Identify the first character of the string.
        first_character = get_string[0:1]

        # Identify the last character of the string.
        last_character = get_string[-1:]
        
    # Indicate if the string contains the word open.
    if 'open' in get_string:
        contain_open = "yes"
    else:
        contain_open = "no"
        
    # Indicate if the string contains only aphabetic letters AND spaces.
    if (any(x.isalpha() for x in get_string)
        and any(x.isspace() for x in get_string)
        and all(x.isalpha() or x.isspace() for x in get_string)):
        alpha_space = "yes"
    else:
        alpha_space = "no"
    
    # Indicate if the string contains only numeric digits.
    if get_string.isdigit():
        digit = "yes"
    else:
        digit = "no"
    
    # Indicate if the entire string is lower case.
    if get_string.islower():
        lowercase = "yes"
    else:
        lowercase = "no"
    
    # Indicate if the entire string is upper case.
    if get_string.isupper():
        uppercase = "yes"
    else:
        uppercase = "no"
    
    
    # Print the character count.    
    print("Length: ", count)

    # Print the first character.
    print("First character: ", first_character)

    # Print the last character.
    print("Last character: ", last_character)

    # Print whether or not the string contains open.
    print("Contains open: ", contain_open)
    
    # Print if the string contains only alphaetic letters and spaces.
    print("Only alphabetic letters and spaces: ", alpha_space)
    
    # Print if the string contains only numeric digits.
    print("Only numeric digits: ", digit)
    
    # Print if the string is lower case.
    print("All lower case: ", lowercase)
    
    # Print if the string is upper case.
    print("All upper case: ", uppercase)


