
path = "Day17//Day17.txt"

rocks = [
    [0, 1, 2, 3],   # Bar shape
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],     # Cross shape
    [0, 1, 2, 2 + 1j, 2 + 2j],   # Backwards L shape
    [0, 1j, 2j, 3j],             # Standing bar shape
    [0, 1, 1j, 1 + 1j]      # Square shape
]

jets = [1 if x == ">" else -1 for x in open(path).read()]
solid = {x - 1j for x in range(7)}
height = 0

rock_count = 0
rock_index = 0

rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]} # Two from the left three about stack

while rock_count < 2022:
    for jet in jets:
        
        moved = {x + jet for x in rock} # Shifts rock by jet value (1 or -1)

        if all(0 <= x.real < 7 for x in moved) and not moved & solid: # If intersected with walls or the stack
            rock = moved

        moved = {x - 1j for x in rock} # Moves down

        if moved & solid:
            solid |= rock
            rock_count += 1
            height = max(x.imag for x in solid) + 1
            if rock_count >= 2022:
                break
            rock_index = (rock_index + 1) % 5 # Get new rock
            rock = {x + 2 + (height + 3) *1j for x in rocks[rock_index]}
        else:
            rock = moved

print(height)