def read_to_array(path: str, strip: bool = True) -> list[str]:
    with open(path) as f:
        lines: list[str] = f.readlines()

    # let's always clean up
    if strip:
        return [x.strip() for x in lines]
    else:
        return lines

def read_to_2d_array(path: str) -> list[list[str]]:
    raw_array: list[str] = read_to_array(path)

    return [[y for y in x] for x in raw_array]