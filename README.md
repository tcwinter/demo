# Units

`units` is a dependency-free Python package for common unit conversions. Import a module directly to use its conversion functions:

```python
from units.length import meters_to_feet, feet_to_meters

print(meters_to_feet(1))
```

## Modules

- `units.length`: `meters_to_feet`, `feet_to_meters`
- `units.mass`: `kg_to_lb`, `lb_to_kg`
- `units.temp`: `celsius_to_fahrenheit`, `fahrenheit_to_celsius`
- `units.volume`: `liters_to_gallons`, `gallons_to_liters` (US liquid gallon = 3.785411784 liters)
- `units.speed`: `kmh_to_mph`, `mph_to_kmh` (mile = 1.609344 km)

Each module includes plain-assert tests. Run a module's tests from the repository root with:

```sh
python -B -m units.test_MODULE
```

Replace `MODULE` with the module name, such as `length`, `mass`, `temp`, `volume`, or `speed`.
