#!/usr/bin/env python3
"""
`mapadt` driver

@authors: Roman Yasinovskyy
@version: 2021.3
"""

from mapadt import HashMap


def main():
    map = HashMap(5)
    print("Map (empty)")
    print("Expected output: {}")
    print(f"Produced output: {map}")

    print("Adding items")
    map[18] = "ant"
    map[61] = "bee"
    map.put(20, "cat")
    map.put(21, "deer")

    print("Retrieval")
    print("Expected output: ant")
    print(f"Produced output: {map[18]}")
    print("Expected output: deer")
    print(f"Produced output: {map[21]}")

    print("Updating")
    map[21] = "dog"
    print("Expected output: dog")
    print(f"Produced output: {map[21]}")

    print("Map (str)")
    print("Expected output: {20: 'cat', 61: 'bee', 21: 'dog', 18: 'ant'}")
    print(f"Produced output: {map}")

    print("Contains")
    print("Expected output: True")
    print(f"Produced output: {18 in map}")
    print("Expected output: False")
    print(f"Produced output: {81 in map}")

    print("Size")
    print("Expected output: 4")
    print(f"Produced output: {len(map)}")

    print("Keys (raw)")
    print("Expected output: [20, 61, 21, 18, None]")
    print(f"Produced output: {map._keys}")

    print("Keys (raw)")
    print("Expected output: [20, 61, 21, 18, None]")
    print(f"Produced output: {map._keys}")

    print("Keys (method)")
    print("Expected output: [20, 61, 21, 18]")
    print(f"Produced output: {map.keys()}")

    print("Values (raw)")
    print("Expected output: ['cat', 'bee', 'dog', 'ant', None]")
    print(f"Produced output: {map._values}")

    print("Values (method)")
    print("Expected output: ['cat', 'bee', 'dog', 'ant']")
    print(f"Produced output: {map.values()}")

    print("Items (method)")
    print("Expected output: [(20, 'cat'), (61, 'bee'), (21, 'dog'), (18, 'ant')]")
    print(f"Produced output: {map.items()}")


if __name__ == "__main__":
    main()
