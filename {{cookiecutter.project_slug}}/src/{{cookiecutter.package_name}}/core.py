def greet(name: str) -> str:
    """Return a friendly greeting for ``name``."""
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"
