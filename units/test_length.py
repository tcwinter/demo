from units.length import meters_to_feet, feet_to_meters


def test_meters_to_feet():
    assert meters_to_feet(0) == 0.0
    assert abs(meters_to_feet(1) - 3.28084) < 1e-10
    assert abs(meters_to_feet(10) - 32.8084) < 1e-10
    assert abs(meters_to_feet(100) - 328.084) < 1e-10


def test_feet_to_meters():
    assert feet_to_meters(0) == 0.0
    assert abs(feet_to_meters(1) - 0.3048) < 1e-10
    assert abs(feet_to_meters(10) - 3.048) < 1e-10
    assert abs(feet_to_meters(100) - 30.48) < 1e-10


def test_roundtrip():
    assert abs(feet_to_meters(meters_to_feet(5)) - 5.0) < 1e-6
    assert abs(meters_to_feet(feet_to_meters(50)) - 50.0) < 1e-6


if __name__ == "__main__":
    test_meters_to_feet()
    test_feet_to_meters()
    test_roundtrip()
    print("All length conversion tests passed!")