from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def access_page(self, page):
        if page in self.cache:
            self.cache.move_to_end(page)
            print(f"✅ Page {page} accessed (HIT)")
        else:
            print(f"⚠️ Page {page} loaded (MISS)")
            if len(self.cache) >= self.capacity:
                removed = self.cache.popitem(last=False)
                print(f"🔁 Removing least recently used page: {removed[0]}")
            self.cache[page] = True

    def display(self):
        print("📘 Current Cache State (Most → Least Recent):")
        for page in reversed(self.cache):
            print(f"  📄 {page}")

# 🔹 Sample test
if __name__ == "__main__":
    cache_size = 3
    lru = LRUCache(cache_size)

    test_pages = [1, 2, 3, 1, 4, 5]
    for page in test_pages:
        lru.access_page(page)
        lru.display()
        print("------")
