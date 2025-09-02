### Imports ###

import pandas as pd
import numpy as np
import math as m

### Functions ###

# Function to produce character list to use in password generation
def char_list_gen():
    characters = ""
    separated_characters = ""
    for i in range(33,123):
        characters += chr(i)
    for char in "`.,-_[]{}<>()|'\"\\/":
        characters = characters.replace(char, '')
    for char in characters:
        char += ' '
        separated_characters += char
    character_list = separated_characters.split(' ')
    character_list.remove('')
    return character_list

# Function to give types of characters to each character in the list
def give_type(character):
    if character.isnumeric():
        return 'Number'
    elif character.islower():
        return 'Lowercase'
    elif character.isupper():
        return 'Uppercase'
    else:
        return 'Special'
    
# Function to create a dataframe to display the Manhattan distance between all possible characters
def make_matrix(list, array):
    start_chars = []
    end_chars = []
    distances = []
    for char in list:
        for compchar in list:
            if char == compchar:
                continue
            start_chars.append(char)
            end_chars.append(compchar)
            distances.append(abs(np.where(array == char)[0][0].item() - np.where(array == compchar)[0][0].item()) + abs(np.where(array == char)[1][0].item() - np.where(array == compchar)[1][0].item()))
    return pd.DataFrame({'Start Character': start_chars, 'End Character': end_chars, 'Distance': distances})

# Function to generate sequence of character types that random password generator will use for password generation
def generate_character_type_sequence(character_length):
    sequence = []
    start_weights = [0.3, 0.3, 0.2, 0.2]
    weight_deltas = [i/2 for i in start_weights]
    character_types = ["Uppercase", "Lowercase", "Number", "Special"]

    char = 0
    while char < character_length:
        while char >= character_length - 2:
            while len(set(sequence)) < 4:
                selected_type = np.random.choice(list({"Uppercase", "Lowercase", "Number", "Special"} - set(sequence))).item()
                sequence.append(selected_type)
                char += 1
            break

        selected_type = np.random.choice(character_types, p=start_weights).item()
        sequence.append(selected_type)

        for type in character_types:
            if type == selected_type:
                if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                    start_weights[character_types.index(type)] -= start_weights[character_types.index(type)] 
                else:
                    start_weights[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
            else:
                if start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)] < 0:
                    start_weights[character_types.index(type)] += start_weights[character_types.index(selected_type)]/3
                else:
                    start_weights[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3
        char += 1
        start_weights = start_weights / np.sum(start_weights, dtype=np.float64)
        weight_deltas = [i/2 for i in start_weights]
    return sequence

# Function to calculate the probability of selecting a possible Manhattan distance between available characters in an altered skew normal distribution
def pdf(x, location, scale):
    return 0.4*m.exp(-((x-location)**2)/(2*scale**2))/scale if x == 0 or x > 6 else 0.8*m.exp(-((x-location)**2)/(2*scale**2))/scale + 0.053*m.exp(-((x-location)**2)/(2*scale**2))/scale

# Function to generate a random password that follows a given sequence of character types
def generate_random_password(sequence):
    password = ""
    probability_distribution = [pdf(i, 1, 7) for i in range(0, 15)]
    current_chartype = sequence[0]
    current_character = np.random.choice(character_type_df[character_type_df['Character Type'] == current_chartype]['Character'])
    password += current_character
    for i in range(1, len(sequence)):
        filtered_df = character_info_df[(character_info_df['Start Character'] == current_character) & (character_info_df['Character Type'] == sequence[i])]
        chosen_distance = np.random.choice(list(set(filtered_df['Distance'])), p=[probability_distribution[i] for i in list(set(filtered_df['Distance']))]/np.sum([probability_distribution[i] for i in list(set(filtered_df['Distance']))])).item()
        last_filtered_df = filtered_df[filtered_df['Distance'] == chosen_distance]
        current_character = np.random.choice(last_filtered_df['End Character'])
        while current_character in password:
            if len(last_filtered_df) > 1 and current_character not in password:
                current_character = np.random.choice(last_filtered_df[last_filtered_df['End Character'] != current_character]['End Character'])
            else:
                chosen_distance = np.random.choice(list(set(filtered_df['Distance'])), p=[probability_distribution[i] for i in list(set(filtered_df['Distance']))]/np.sum([probability_distribution[i] for i in list(set(filtered_df['Distance']))])).item()
                last_filtered_df = filtered_df[filtered_df['Distance'] == chosen_distance]
                current_character = np.random.choice(last_filtered_df['End Character'])
        password += current_character
    return password

def password_length_input():
    while True:
        try:
            length = int(input("Enter desired password length (Between 8 and 40 characters): "))
            if length < 8 or length > 40:
                print("Password length must be between 8 and 40 characters. Please try again.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid integer for password length.")

### Main Code ###

def main(length):
    global character_info_df
    global character_type_df

    # Generate character list and corresponding 2D array
    character_list = char_list_gen()
    keyboard_matrix = np.array([[['1','!'], ['2','@'], ['3','#'], ['4','$'], ['5','%'], ['6','^'], ['7','&'], ['8','*'], ['9','('], ['0',')'], ['-','_'], ['=','+']],
                 [['q','Q'], ['w','W'], ['e','E'], ['r','R'], ['t','T'], ['y','Y'], ['u','U'], ['i','I'], ['o','O'], ['p','P'], ['[','{'], [']','}']],
                 [['a','A'], ['s','S'], ['d','D'], ['f','F'], ['g','G'], ['h','H'], ['j','J'], ['k','K'], ['l','L'], [';',':'], ['\'','"'], ['\\','|']],
                 [['z','Z'], ['x','X'], ['c','C'], ['v','V'], ['b','B'], ['n','N'], ['m','M'], [',','<'], ['.','>'], ['?','/'], ['|','|'], ['|','|']]])

    # Create dataframe with Manhattan distances between all possible characters
    character_distance_df = make_matrix(character_list, keyboard_matrix)

    # Create dataframe with character types for each character
    character_type_df = pd.DataFrame({'Character': character_list})
    character_type_df['Character Type'] = character_type_df['Character'].apply(give_type)

    character_info_df = character_distance_df.merge(character_type_df, left_on='End Character', right_on='Character', how='left')

    # Generate random password of selected length
    return generate_random_password(generate_character_type_sequence(length))

if __name__ == "__main__":
    print(main(password_length_input())) 

