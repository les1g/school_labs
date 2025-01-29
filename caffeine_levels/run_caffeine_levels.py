def caffeine_levels():
    """------------------------------------------------------
    A program that calculates the half-life of caffeine after
    6, 12, and 24 hours.
    """
    print(caffeine_levels.__doc__)

    caffeine_mg = float(input('Enter the caffeine in mg: '))
    half_life = 6

    caffeine_level_hour6 = caffeine_mg * 0.5 ** (6 / half_life)
    caffeine_level_hour12 = caffeine_mg * 0.5 ** (12 / half_life)
    caffeine_level_hour24 = caffeine_mg * 0.5 ** (24 / half_life)

    print(f'After 6 hours: {caffeine_level_hour6:.2f} mg')
    print(f'After 12 hours: {caffeine_level_hour12:.2f} mg')
    print(f'After 24 hours: {caffeine_level_hour24:.2f} mg')

    print('------------------------------------------------------')
