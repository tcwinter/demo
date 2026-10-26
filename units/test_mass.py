from units.mass import kg_to_lb, lb_to_kg


def test_kg_to_lb():
    assert kg_to_lb(0) == 0.0
    assert abs(kg_to_lb(1) - 2.20462) < 1e-10
    assert abs(kg_to_lb(5) - 11.0231) < 1e-12
    assert abs(kg_to_lb(100) - 220.462) < 1e-12


def test_lb_to_kg():
    assert lb_to_kg(0) == 0.0
    assert abs(lb_to_kg(1) - 0.453592) < 1e-10
    assert abs(lb_to_kg(10) - 4.53592) < 1e-12
    assert abs(lb_to_kg(220.462) - 100.0) < 1e-6


def test_roundtrip():
    """Converting kg->lb->kg should give back the original value."""
    for kg in [0, 1, 2.5, 10, 50, 100]:
        assert abs(lb_to_kg(kg_to_lb(kg)) - kg) < 1e-12

    for lb in [0, 1, 5, 20.5, 200]:
        assert abs(kg_to_lb(lb_to_kg(lb)) - lb) < 1e-12


if __name__ == "__main__":
    test_kg_to_lb()
    test_lb_to_kg()
    test_roundtrip()
    print("All tests passed.")