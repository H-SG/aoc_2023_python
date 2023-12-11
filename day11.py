from itertools import combinations

space_map: list[list[str]] = []
add_y_map: list[int] = []
add_x_map: list[int] = []

with open('data/day11.txt', 'r') as file:
    for y, line in enumerate(file):
        space_map.append([c for c in line.strip()])

        if '#' not in line:
            add_y_map.append(y)

for x in range(len(space_map[0])):
    col: list[str] = [line[x] for line in space_map]

    if '#' not in col:
        add_x_map.append(x)

galaxies: list[tuple[int]] = []

for y, row in enumerate(space_map):
    for x, char in enumerate(row):
        if char == '#':
            galaxies.append((x, y))

def get_galaxy_distances(galaxies: list[tuple[int]], expansion_factor: int) -> int:
    distances: int = 0
    for g1, g2 in combinations(galaxies, 2):
        expand_x: list[int] = [expansion_factor for x in add_x_map if (x > min(g1[0], g2[0])) and (x < max(g1[0], g2[0]))]
        expand_y: list[int] = [expansion_factor for y in add_y_map if (y > min(g1[1], g2[1])) and (y < max(g1[1], g2[1]))]
        distances += (abs(g1[0] - g2[0]) + abs(g1[1] - g2[1]) + sum(expand_y) + sum(expand_x))

    return distances

print(f'Day 11 - Part 1: {get_galaxy_distances(galaxies, 1)}')
print(f'Day 11 - Part 2: {get_galaxy_distances(galaxies, 1E6 - 1)}')
