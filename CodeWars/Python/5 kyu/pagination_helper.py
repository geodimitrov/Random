class PaginationHelper:

    def __init__(self, items, items_per_page):
        self.items = items
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.items)

    def page_count(self):
        if len(self.items) % self.items_per_page > 0:
            count = len(self.items) // self.items_per_page + 1
        else:
            count = len(self.items) // self.items_per_page
        return count

    def page_item_count(self, page_index):

        if page_index not in range(self.page_count()):
            return -1

        if not len(self.items) % self.items_per_page == 0:
            if page_index == self.page_count() - 1:
                return len(self.items) % self.items_per_page

        return self.items_per_page

    def page_index(self, item_index):

        if item_index not in range(len(self.items)):
            return -1

        return item_index // self.items_per_page



helper = PaginationHelper(['a', 'b', 'c', 'd', 'e', 'f'], 4)
print(helper.page_count())  # should == 2
print(helper.item_count())  # should == 6
print(helper.page_item_count(0))  # should == 4
print(helper.page_item_count(1)) # last page - should == 2
print(helper.page_item_count(2))
print(helper.page_index(5)) # should == 1 (zero based index)
print(helper.page_index(2)) # should == 0
print(helper.page_index(20)) # should == -1
print(helper.page_index(-10)) # should == -1

