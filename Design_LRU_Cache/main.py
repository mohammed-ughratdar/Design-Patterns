
from cache.lru_cache import LRUCache


if __name__ == "__main__":
    print("=== LRU Cache ===\n")

    cache = LRUCache(2)

    print("Put (1, 1)")
    cache.put(1, 1)
    print("Put (2, 2)")
    cache.put(2, 2)

    print(f"\nGet(1): {cache.get(1)}")

    print("\nPut (3, 3) - should evict (2, 2)")
    cache.put(3, 3)

    print(f"Get(2): {cache.get(2)}")
    print(f"Get(3): {cache.get(3)}")

    print("\nPut (3, 4) - update existing key")
    cache.put(3, 4)
    print(f"Get(3): {cache.get(3)}")

    print("\n=== Testing with capacity 1 ===")
    cache2 = LRUCache(1)
    cache2.put(1, 1)
    print(f"Get(1): {cache2.get(1)}")
    cache2.put(2, 2)
    print(f"Get(1): {cache2.get(1)}")
    print(f"Get(2): {cache2.get(2)}")
