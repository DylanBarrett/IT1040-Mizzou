import math
def get_people():
    while True:
        try:
        # Get info from user.
            people = int(input('how many people will be at this event? '))
            if people >= 0:
                print('Great')
            else:
                print("you must choose a number greather than zero.")
        except ValueError:
            print("sorry you must chose a number greater than zero.")
            continue
        else:
            break
    return people

def get_ingredient_cost():
    while True:
        try:
            ingredient_cost = float(input('How much did the ingredients cost?$ '))
            if ingredient_cost > 0:
                print('Great')
            else:
                print("you must choose a number greather than zero.")
        except ValueError:
            print("sorry you must chose a number greater than zero.")
            continue
        else:
            break
    return ingredient_cost
    
def main():
        while True:
            people = get_people()
            ingredient_cost = get_ingredient_cost()
            total_cupcakes = people * 1.25
            batches_of_cupcakes = total_cupcakes / 12
            hours_of_labor = batches_of_cupcakes * 1.25
            cost_of_labor = hours_of_labor * 35
            cost_per_cupcake = total_cupcakes / ingredient_cost + cost_of_labor
            total_cost = cost_of_labor + ingredient_cost
            print(people)
            print(ingredient_cost)
            print(total_cupcakes)
            print(batches_of_cupcakes)
            print(hours_of_labor)
            print(cost_of_labor)
            print(cost_per_cupcake)
            print(total_cost)

            answer = input('would you like to do another estimate? (y/n): ')
            if answer in ('y', 'n'):
                break
            print('invalid input')
            if answer == 'y':
                continue
            else:
                print('Goodbye')
            break
    
main()

