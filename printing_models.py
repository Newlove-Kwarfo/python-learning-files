# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Printing unprinted designs
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Current design: {current_design}')
    completed_models.append(current_design)

#Printing completed models
for model in completed_models:
    print(f'Completed design: {model}')