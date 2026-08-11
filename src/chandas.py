def generate_patterns(n):
    """Generate all Laghu-Guru patterns for n syllables."""

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of syllables must be a positive integer.")

    total_patterns = 2 ** n
    patterns = []

    for number in range(total_patterns):
        binary = format(number, f"0{n}b")

        pattern = "".join(
            "L" if bit == "0" else "G"
            for bit in binary
        )

        patterns.append({
            "pattern": pattern,
            "binary": binary,
            "decimal": number
        })

    return patterns


def pattern_to_binary(pattern):
    """Convert a Laghu-Guru pattern to binary."""

    if not isinstance(pattern, str):
        raise ValueError("Pattern must be a string.")

    pattern = pattern.upper().replace(" ", "")

    if not pattern:
        raise ValueError("Pattern cannot be empty.")

    if any(symbol not in "LG" for symbol in pattern):
        raise ValueError("Pattern can contain only L and G.")

    return "".join(
        "0" if symbol == "L" else "1"
        for symbol in pattern
    )


def pattern_to_decimal(pattern):
    """Convert a Laghu-Guru pattern to decimal."""

    binary = pattern_to_binary(pattern)
    return int(binary, 2)


def total_patterns(n):
    """Return the number of possible patterns."""

    if not isinstance(n, int) or n <= 0:
        raise ValueError("Number of syllables must be a positive integer.")

    return 2 ** n


