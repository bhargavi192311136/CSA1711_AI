import itertools

def map_coloring():
    regions = ['WA','NT','SA','Q','NSW','V']
    neighbors = {
        'WA':['NT','SA'],
        'NT':['WA','SA','Q'],
        'SA':['WA','NT','Q','NSW','V'],
        'Q':['NT','SA','NSW'],
        'NSW':['SA','Q','V'],
        'V':['SA','NSW']
    }
    colors = ['Red','Green','Blue']
    for assignment in itertools.product(colors, repeat=len(regions)):
        valid = True
        for r in regions:
            for n in neighbors[r]:
                if assignment[regions.index(r)] == assignment[regions.index(n)]:
                    valid = False
        if valid:
            print(dict(zip(regions,assignment)))
            break

map_coloring()
