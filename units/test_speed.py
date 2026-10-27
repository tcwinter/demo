from units.speed import kmh_to_mph, mph_to_kmh


def test_kmh_to_mph():
    assert kmh_to_mph(0) == 0.0
    assert abs(kmh_to_mph(1.609344) - 1.0) < 1e-12
    assert abs(kmh_to_mph(100) - 62.1371192237) < 1e-10


def test_mph_to_kmh():
    assert mph_to_kmh(0) == 0.0
    assert abs(mph_to_kmh(1) - 1.609344) < 1e-12
    assert abs(mph_to_kmh(60) - 96.56064) < 1e-12


def test_roundtrip():
    for kmh in [0, 1, 5.5, 50, 100]:
        assert abs(mph_to_kmh(kmh_to_mph(kmh)) - kmh) < 1e-12

    for mph in [0, 1, 5.5, 50, 100]:
        assert abs(kmh_to_mph(mph_to_kmh(mph)) - mph) < 1e-12


if __name__ == "__main__":
    test_kmh_to_mph()
    test_mph_to_kmh()
    test_roundtrip()
    print("All speed conversion tests passed!")
