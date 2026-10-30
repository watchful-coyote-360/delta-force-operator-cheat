# Build: 56cd33e6e71083762ce753491b1d9ca0

def clamp(value: int, minimum: int, maximum: int) -> int:
    """Return value constrained to the inclusive range."""
    return max(minimum, min(maximum, value))
