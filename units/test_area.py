from units.area import square_meters_to_square_feet, square_feet_to_square_meters


def test_square_meters_to_square_feet():
    assert square_meters_to_square_feet(0) == 0.0
    assert abs(square_meters_to_square_feet(1) - (1 / (0.3048 ** 2))) < 1e-10
    assert abs(square_meters_to_square_feet(10) - (10 / (0.3048 ** 2))) < 1e-10


def test_square_feet_to_square_meters():
    assert square_feet_to_square_meters(0) == 0.0
    assert abs(square_feet_to_square_meters(1) - (0.3048 ** 2)) < 1e-12
    assert abs(square_feet_to_square_meters(100) - (100 * (0.3048 ** 2))) < 1e-12


def test_roundtrip():
    assert abs(square_feet_to_square_meters(square_meters_to_square_feet(5)) - 5.0) < 1e-12
    assert abs(square_meters_to_square_feet(square_feet_to_square_meters(50)) - 50.0) < 1e-10


if __name__ == "__main__":
    test_square_meters_to_square_feet()
    test_square_feet_to_square_meters()
    test_roundtrip()
    print("All area conversion tests passed!")
