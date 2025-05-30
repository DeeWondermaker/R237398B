def compute_hpc():
    # Input benchmark and backsight
    bm = float(input("bm: "))
    bs = float(input("Enter backsight reading: "))

    # Calculate HPC
    hpc = bm + bs

    # Input foresights
    inter_or_foresights = input("Enter intermediate sights or foresights (comma-separated): ")
    foresights = [float(x) for x in inter_or_foresights.split(",")]

    # Compute reduced levels
    reduced_levels = [hpc - fs for fs in foresights]


    print("\nReduced Levels:")
    for i, rl in enumerate(reduced_levels, 1):
        print(f"Point {i}: {rl:.3f}")


compute_hpc()