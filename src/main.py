from chandas import (
    generate_patterns,
    pattern_to_binary,
    pattern_to_decimal,
    total_patterns,
)


def display_patterns(n):
    patterns = generate_patterns(n)

    print("\nPingala's Chandaḥśāstra")
    print("Binary Encoding and Combinatorial Generation")
    print("-" * 55)

    print(f"Number of syllables : {n}")
    print(f"Total patterns      : {total_patterns(n)}")

    print("\nPattern        Binary        Decimal")
    print("-" * 40)

    for item in patterns:
        print(
            f"{item['pattern']:<15}"
            f"{item['binary']:<14}"
            f"{item['decimal']}"
        )


def search_pattern():
    pattern = input(
        "\nEnter Laghu-Guru pattern (e.g. LGLG): "
    )

    try:
        binary = pattern_to_binary(pattern)
        decimal = pattern_to_decimal(pattern)

        print("\nPattern Information")
        print("-" * 30)
        print(f"Pattern : {pattern.upper().replace(' ', '')}")
        print(f"Binary  : {binary}")
        print(f"Decimal : {decimal}")

    except ValueError as error:
        print(f"Error: {error}")


def main():
    while True:
        print("\n" + "=" * 55)
        print("PINGALA'S CHANDAŚĀSTRA")
        print("=" * 55)

        print("1. Generate all patterns")
        print("2. Search a pattern")
        print("3. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            try:
                n = int(input("Enter number of syllables: "))
                display_patterns(n)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            search_pattern()

        elif choice == "3":
            print("Program terminated.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
