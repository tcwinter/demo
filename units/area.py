def square_meters_to_square_feet(square_meters: float) -> float:
    """Convert square meters to square feet using 0.3048 meters per foot."""
    return square_meters / (0.3048 ** 2)


def square_feet_to_square_meters(square_feet: float) -> float:
    """Convert square feet to square meters using 0.3048 meters per foot."""
    return square_feet * (0.3048 ** 2)
