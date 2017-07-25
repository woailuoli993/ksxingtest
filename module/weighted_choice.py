import random

def weighted_choice(dict_choice_to_weight):
    if not isinstance(dict_choice_to_weight, dict):
        raise TypeError("Entry arg must be a dict")
    total = sum(weight for choice, weight in dict_choice_to_weight.items())
    roll = random.uniform(0, total)  # return a choice weight hope
    upto = 0
    for choice, weight in dict_choice_to_weight.items():
        if upto + weight >= roll:
            return choice
        upto += weight
    
    assert False, "Bad happend"


def main():
    choicestoweight = {
        "I": 2,
        "hehe": 2,
        "time": 2
    }
    for i in range(22):
        print(weighted_choice(choicestoweight))


if __name__ == '__main__':
    main()