# import random

# items = ['apple', 'banana', 'orange', 'grape']
# item_weights = [10, 20, 30, 5] # Banana is twice as likely as apple, orange is three times, grape is half as likely as apple

# # Select 5 items based on their weights
# weighted_selection = random.choices(items, weights=item_weights, k=5)
# print(weighted_selection)


"""
import numpy as np
from decimal import Decimal, getcontext
getcontext().prec = 8  # Set precision for Decimal operations 

sequence = []
start_weights = [Decimal(0.3), Decimal(0.3), Decimal(0.2), Decimal(0.2)]
weight_deltas = [Decimal(i/2) for i in start_weights]
character_types = ["Uppercase", "Lowercase", "Number", "Special"]
character_length = 8

char = 0
while char < character_length:
    while char >= character_length - 2:
        while len(set(sequence)) < 4:
            selected_type = np.random.choice(list({"Uppercase", "Lowercase", "Number", "Special"} - set(sequence))).item()
            sequence.append(selected_type)
            char += 1
        break

    selected_type = np.random.choice(character_types, p=start_weights).item()
    print(char, start_weights, selected_type, weight_deltas[character_types.index(selected_type)], "\n")
    sequence.append(selected_type)

    # for type in character_types:
    #     if type == selected_type:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] -= start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
    #         else:
    #             start_weights[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
    #     else:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] += (start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)])/3
    #         else:
    #             start_weights[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3

    for type in character_types:
        if type == selected_type:
            if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights[character_types.index(type)] = start_weights[character_types.index(type)] - start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
                print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights[character_types.index(type)] = start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
                print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
        else:
            if start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights[character_types.index(type)] = start_weights[character_types.index(type)] + (start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)])/3
                print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights[character_types.index(type)] = start_weights[character_types.index(type)] + weight_deltas[character_types.index(selected_type)]/3
                print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
    char += 1
    print("\n", char, start_weights, selected_type, weight_deltas[character_types.index(selected_type)], "\n")
"""

"""
import numpy as np

sequence = []
start_weights = [0.3, 0.3, 0.2, 0.2]
start_weights_whole = [i*100 for i in start_weights]
weight_deltas = [i/2 for i in start_weights_whole]
character_types = ["Uppercase", "Lowercase", "Number", "Special"]
character_length = 8

char = 0
while char < character_length:
    while char >= character_length - 2:
        while len(set(sequence)) < 4:
            selected_type = np.random.choice(list({"Uppercase", "Lowercase", "Number", "Special"} - set(sequence))).item()
            sequence.append(selected_type)
            char += 1
        break

    selected_type = np.random.choice(character_types, p=start_weights).item()
    print(char, start_weights, selected_type, weight_deltas[character_types.index(selected_type)])
    sequence.append(selected_type)

    # for type in character_types:
    #     if type == selected_type:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] -= start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
    #         else:
    #             start_weights[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
    #     else:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] += (start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)])/3
    #         else:
    #             start_weights[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3

    for type in character_types:
        if type == selected_type:
            if start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights_whole[character_types.index(type)] = start_weights_whole[character_types.index(type)] - start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
            else:
                start_weights_whole[character_types.index(type)] = start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
        else:
            if start_weights_whole[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights_whole[character_types.index(type)] = start_weights_whole[character_types.index(type)] + (start_weights_whole[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)])/3
            else:
                start_weights_whole[character_types.index(type)] = start_weights_whole[character_types.index(type)] + weight_deltas[character_types.index(selected_type)]/3
    char += 1
    start_weights = [i/100 for i in start_weights_whole] / np.sum([i/100 for i in start_weights_whole], dtype=np.float64)
    print(char, start_weights, sum(start_weights), selected_type, weight_deltas[character_types.index(selected_type)])
"""

"""
import numpy as np

sequence = []
start_weights = [0.3, 0.3, 0.2, 0.2]
start_weights_whole = [i*100 for i in start_weights]
weight_deltas = [i/2 for i in start_weights_whole]
character_types = ["Uppercase", "Lowercase", "Number", "Special"]
character_length = 8

char = 0
while char < character_length:
    while char >= character_length - 2:
        while len(set(sequence)) < 4:
            selected_type = np.random.choice(list({"Uppercase", "Lowercase", "Number", "Special"} - set(sequence))).item()
            sequence.append(selected_type)
            char += 1
        break

    selected_type = np.random.choice(character_types, p=start_weights).item()
    print(char, start_weights_whole, selected_type, weight_deltas[character_types.index(selected_type)], "\n")
    sequence.append(selected_type)

    for type in character_types:
        if type == selected_type:
            if start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights_whole[character_types.index(type)] -= start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
                print(char, start_weights_whole, selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights_whole[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
                print(char, start_weights_whole, selected_type, type, weight_deltas[character_types.index(selected_type)])
        else:
            if start_weights_whole[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights_whole[character_types.index(type)] += (start_weights_whole[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)])/3
                print(char, start_weights_whole, selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights_whole[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3
                print(char, start_weights_whole, selected_type, type, weight_deltas[character_types.index(selected_type)])

    # for type in character_types:
    #     if type == selected_type:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] = start_weights[character_types.index(type)] - start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
    #             print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
    #         else:
    #             start_weights[character_types.index(type)] = start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
    #             print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
    #     else:
    #         if start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] = start_weights[character_types.index(type)] + (start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)])/3
    #             print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
    #         else:
    #             start_weights[character_types.index(type)] = start_weights[character_types.index(type)] + weight_deltas[character_types.index(selected_type)]/3
    #             print(char, start_weights, selected_type, type, weight_deltas[character_types.index(selected_type)])
    char += 1
    start_weights = [i/100 for i in start_weights_whole] / np.sum([i/100 for i in start_weights_whole], dtype=np.float64)
    print("\n", char, start_weights, selected_type, weight_deltas[character_types.index(selected_type)], "\n")
"""


import numpy as np

sequence = []
start_weights = [0.3, 0.3, 0.2, 0.2]
weight_deltas = [i/2 for i in start_weights]
character_types = ["Uppercase", "Lowercase", "Number", "Special"]
character_length = 16

char = 0
while char < character_length:
    while char >= character_length - 2:
        while len(set(sequence)) < 4:
            selected_type = np.random.choice(list({"Uppercase", "Lowercase", "Number", "Special"} - set(sequence))).item()
            sequence.append(selected_type)
            char += 1
        break

    selected_type = np.random.choice(character_types, p=start_weights).item()
    print(char, start_weights, selected_type, weight_deltas[character_types.index(selected_type)])
    sequence.append(selected_type)

    # for type in character_types:
    #     if type == selected_type:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] -= start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)]
    #         else:
    #             start_weights[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
    #     else:
    #         if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
    #             start_weights[character_types.index(type)] += (start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)])/3
    #         else:
    #             start_weights[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3

    for type in character_types:
        if type == selected_type:
            if start_weights[character_types.index(type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights[character_types.index(type)] -= start_weights[character_types.index(type)] 
                print(char, start_weights, sum(start_weights), selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights[character_types.index(type)] -= weight_deltas[character_types.index(selected_type)]
                print(char, start_weights, sum(start_weights), selected_type, type, weight_deltas[character_types.index(selected_type)])
        else:
            if start_weights[character_types.index(selected_type)] - weight_deltas[character_types.index(selected_type)] < 0:
                start_weights[character_types.index(type)] += start_weights[character_types.index(selected_type)]/3
                print(char, start_weights, sum(start_weights), selected_type, type, weight_deltas[character_types.index(selected_type)])
            else:
                start_weights[character_types.index(type)] += weight_deltas[character_types.index(selected_type)]/3
                print(char, start_weights, sum(start_weights), selected_type, type, weight_deltas[character_types.index(selected_type)])
    char += 1
    start_weights = start_weights / np.sum(start_weights, dtype=np.float64)
    weight_deltas = [i/2 for i in start_weights]
    print(char, start_weights, sum(start_weights), selected_type, type, weight_deltas[character_types.index(selected_type)])
print("\nFinal sequence:", sequence)