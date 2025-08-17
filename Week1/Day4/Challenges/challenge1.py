import math


class InvalidPageError(ValueError):
    pass


class Pagination:
    def __init__(self, items=None, page_size=10):
       
        self.items = items if items is not None else []
        self.page_size = int(page_size)  
        self.current_idx = 0  
        
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        """Return items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        """Go to the specified page (1-based indexing)."""
        if page_num < 1 or page_num > self.total_pages:
            raise InvalidPageError(f"Page {page_num} is out of range.")
        self.current_idx = page_num - 1
        return self  

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """Display current page items line by line."""
        return "\n".join(self.get_visible_items())



alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())


p.next_page()
print(p.get_visible_items())


p.last_page()
print(p.get_visible_items())


p.go_to_page(2).next_page().previous_page()
print(p.get_visible_items())


print(str(p))


print(p.current_idx + 1)


try:
    p.go_to_page(0)
except InvalidPageError as e:
    print("Error:", e)
