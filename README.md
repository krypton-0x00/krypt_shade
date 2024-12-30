# ColorLib

ColorLib is a Python library that provides utilities for color manipulation, including:

- Conversion between HEX and RGB
- Brightness adjustment
- Generation of color shades

## Installation

You can install the library using pip:

```bash
pip install krypt_shade
```
## Usage
```python
from krypt_shade import Color

# Create a Color object from a HEX color
color = Color.from_hex("#ff5733")

# Generate 5 shades of the color
shades = color.generate_shades()
for shade in shades:
    print(shade)

```
