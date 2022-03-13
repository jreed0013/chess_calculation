def factorial(n: int) -> int:
    """Calculate a factorial."""
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


def main() -> int:
    """"Calculate a rough estimation of all possible moves made in a game of chess."""
    spaces: int = 64
    pieces: int = 32
    s: float = 0
    while pieces >= 2:
        permutation: int = factorial(spaces)/factorial(spaces - pieces)
        i = pieces - 1
        while i >= 1:
            options: float = pieces - i
            moves: float = 3*permutation*options
            s += moves
            i -= 1
        pieces -= 1
    print(f"Estimate: {s}")
    return s

main()