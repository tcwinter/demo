from units.temp import celsius_to_fahrenheit, fahrenheit_to_celsius


def test_celsius_to_fahrenheit():
    # 0°C = 32°F
    assert celsius_to_fahrenheit(0.0) == 32.0
    # 100°C = 212°F
    assert celsius_to_fahrenheit(100.0) == 212.0
    # -40°C = -40°F
    assert celsius_to_fahrenheit(-40.0) == -40.0
    # 37°C ≈ 98.6°F
    assert celsius_to_fahrenheit(37.0) == 98.6


def test_fahrenheit_to_celsius():
    # 32°F = 0°C
    assert fahrenheit_to_celsius(32.0) == 0.0
    # 212°F = 100°C
    assert fahrenheit_to_celsius(212.0) == 100.0
    # -40°F = -40°C
    assert fahrenheit_to_celsius(-40.0) == -40.0
    # 98.6°F ≈ 37°C
    assert fahrenheit_to_celsius(98.6) == 37.0


def test_roundtrip():
    for val in [0.0, 100.0, -40.0, 37.0, 212.0, 32.0]:
        assert fahrenheit_to_celsius(celsius_to_fahrenheit(val)) == val
        assert celsius_to_fahrenheit(fahrenheit_to_celsius(val)) == val


if __name__ == "__main__":
    test_celsius_to_fahrenheit()
    test_fahrenheit_to_celsius()
    test_roundtrip()
    print("All tests passed!")