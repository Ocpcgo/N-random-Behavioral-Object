import random

# Define the number of objects (n)
n = int(input('Input the number of object: '))

# Initialize the directions of the objects randomly
directions = [random.choice([-1, 1]) for i in range(n)]

# Define a function to update the directions of the objects based on their neighbors
def update_directions(directions):
    new_directions = directions.copy()
    for i in range(n):
        neighbor_indices = [(i-1)%n, (i+1)%n]  # get the indices of the two neighboring objects
        neighbor_directions = [directions[j] for j in neighbor_indices]  # get the directions of the neighboring objects
        if neighbor_directions[0] == neighbor_directions[1]:  # if the two neighboring objects are facing the same direction
            new_directions[i] = neighbor_directions[0]  # follow the direction of the neighboring object
    return new_directions

# Iterate the update process for a certain number of steps
num_steps = int(input('Input the number of step you like: '))
direction_change = 0
for i in range(num_steps):
    print(directions)
    directions = update_directions(directions)
directions_list = [directions]
