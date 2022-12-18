
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

seen = {}

def summarize():
    o = [-20]*7

    for x in solid:
        r = int(x.real)
        i = int(x.imag)
        o[r] = max(o[r], i)

    top = max(o)
    return tuple([x-top for x in o])

    

rock_count = 0
rock_index = 0

rock = {x + 2 + (height + 3) * 1j for x in rocks[rock_index]} # Two from the left three about stack

T = 1000000000000

while rock_count < T:
    for ji, jet in enumerate(jets):
        
        moved = {x + jet for x in rock} # Shifts rock by jet value (1 or -1)

        if all(0 <= x.real < 7 for x in moved) and not moved & solid: # If intersected with walls or the stack
            rock = moved

        moved = {x - 1j for x in rock} # Moves down

        if moved & solid:
            solid |= rock
            rock_count += 1
            height = max(x.imag for x in solid) + 1
            if rock_count >= T:
                break
            rock_index = (rock_index + 1) % 5 # Get new rock
            rock = {x + 2 + (height + 3) *1j for x in rocks[rock_index]}
            key = (ji, rock_index, summarize())
            if key in seen:
                lrc, lh = seen[key]
                rem = T - rock_count
                rep = rem // (rock_count - lrc)
                offset = rep * (height - lh)
                rock_count += rep * (rock_count-lrc)
                seen = {}
            seen[key] = (rock_count, height)
        else:
            rock = moved

print(int(height + offset))