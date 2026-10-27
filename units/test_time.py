from units.time import hours_to_minutes, minutes_to_hours


def test_hours_to_minutes():
    assert hours_to_minutes(0) == 0.0
    assert hours_to_minutes(1) == 60.0
    assert hours_to_minutes(2.5) == 150.0
    assert hours_to_minutes(0.25) == 15.0


def test_minutes_to_hours():
    assert minutes_to_hours(0) == 0.0
    assert minutes_to_hours(60) == 1.0
    assert minutes_to_hours(150) == 2.5
    assert minutes_to_hours(15) == 0.25


def test_roundtrip():
    for hours in [0, 1, 2.5, 0.25, 12.75]:
        assert minutes_to_hours(hours_to_minutes(hours)) == hours

    for minutes in [0, 1, 15, 60, 150, 765]:
        assert hours_to_minutes(minutes_to_hours(minutes)) == minutes


if __name__ == "__main__":
    test_hours_to_minutes()
    test_minutes_to_hours()
    test_roundtrip()
    print("All time conversion tests passed!")
