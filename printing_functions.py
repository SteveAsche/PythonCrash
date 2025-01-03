def print_models(unprinted_designs, completed_models):
    '''Takes the current list and prints one at a time'''
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    '''shows the list of completed models'''
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
