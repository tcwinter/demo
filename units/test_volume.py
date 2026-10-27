from units.volume import liters_to_gallons, gallons_to_liters


def test_liters_to_gallons():
    assert liters_to_gallons(0) == 0.0
    assert abs(liters_to_gallons(3.785411784) - 1.0) < 1e-12
    assert abs(liters_to_gallons(10) - 10 / 3.785411784) < 1e-12


def test_gallons_to_liters():
    assert gallons_to_liters(0) == 0.0
    assert abs(gallons_to_liters(1) - 3.785411784) < 1e-12
    assert abs(gallons_to_liters(10) - 37.85411784) < 1e-12


def test_roundtrip():
    assert abs(gallons_to_liters(liters_to_gallons(5)) - 5.0) < 1e-12
    assert abs(liters_to_gallons(gallons_to_liters(50)) - 50.0) < 1e-12


if __name__ == "__main__":
    test_liters_to_gallons()
    test_gallons_to_liters()
    test_roundtrip()
    print("All volume conversion tests passed!")
