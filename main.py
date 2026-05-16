from __future__ import annotations

def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2), or None."""
    seen = {}

    for k, v in mapping.items():
        if v in seen:
            return (seen[v], k)
        seen[v] = k

    return None


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element not in range, or None."""
    values = set(mapping.values())

    for item in target:
        if item not in values:
            return item

    return None


def my_floor(x: float) -> int:
    """Return floor(x) without math.floor."""
    n = int(x)

    if x >= 0 or x == n:
        return n
    else:
        return n - 1


def my_ceil(x: float) -> int:
    """Return ceil(x) without math.ceil."""
    n = int(x)

    if x == n:
        return n
    elif x > 0:
        return n + 1
    else:
        return n