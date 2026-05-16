from __future__ import annotations


def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2) and x1!=x2, or None if injective."""
    # === TODO ===
    seen = {}

    for k, v in mapping.items():
        if v in seen:
            return (seen[v], k)
        seen[v] = k

    return None
    
    # === END TODO ===


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element with no input mapping to it, or None if surjective."""
    # === TODO ===
    def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element not in range, or None."""
    values = set(mapping.values())

    for item in target:
        if item not in values:
            return item

    return None
    # === END TODO ===


def my_floor(x: float) -> int:
    """Return floor(x) without using math.floor."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===


def my_ceil(x: float) -> int:
    """Return ceil(x) without using math.ceil."""
    # === TODO ===
    # Your code here
    pass
    # === END TODO ===
