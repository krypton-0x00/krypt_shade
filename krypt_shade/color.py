class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @classmethod
    def from_hex(cls, hex_color):
        """Create a Color object from a HEX color code."""
        hex_color = hex_color.lstrip('#')
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
        return cls(r, g, b)

    def to_hex(self):
        """Convert RGB to HEX format."""
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    def adjust_brightness(self, factor):
        """Adjust the brightness by multiplying RGB values by a factor."""
        self.r = min(255, max(0, int(self.r * factor)))
        self.g = min(255, max(0, int(self.g * factor)))
        self.b = min(255, max(0, int(self.b * factor)))

    def generate_shades(self, num_shades=5):
        """Generate shades by adjusting the brightness of the color."""
        shades = [self.to_hex()]
        for i in range(1, num_shades):
            factor = 1 - (i / (num_shades * 2))  # Gradually darken the color
            shade = Color(self.r, self.g, self.b)
            shade.adjust_brightness(factor)
            shades.append(shade.to_hex())
        return shades
