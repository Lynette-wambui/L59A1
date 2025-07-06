def space(n):
    if n == 0:
        print("🌌🌌 Reached the end! Time to go back up!")
        return
    print(f"Going deeper... Level {n}")

    space(n - 1)

    print(f"Coming back... Level  {n}")

# Start the journey
levels = int(input("Enter how many levels  deep we should go"))
space(levels)
    