""" Return the number of orbits which the satelite is connected to

This recursive function finds the number of direct and indirect orbits
which have the outermost point of the reference_pairing, including itself.
"""
def count_orbits(reference_pairing):
    total = 0
    for pairing in all_pairings:
        if (
            pairing[1] == reference_pairing[0] and  # Another pairing excists
            pairing[1] != reference_pairing[1]      # It's not the reference pairing
            ):
            total += count_orbits(pairing)
    return total + 1    # Need to add 1 to count for the reference pairing

""" Return a list of all object/satelite pairings from encoded file

There are two elements per list item. ID of object and
the ID of its satelite it's paired with.
"""
def return_task_input():
    all_pairings = []
    open_file = open("6_1.txt", "r")

    for line in open_file:
        # ) is used as the seperator per line between object and satelite
        all_pairings.append(line.rstrip("\n").split(")")) 

    open_file.close()
    return all_pairings

total = 0
all_pairings = return_task_input()

for connection in all_pairings:
    total += count_orbits(connection)
    
print(total)