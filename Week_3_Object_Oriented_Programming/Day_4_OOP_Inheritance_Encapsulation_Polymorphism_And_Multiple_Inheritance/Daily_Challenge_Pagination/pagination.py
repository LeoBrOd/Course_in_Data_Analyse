class Pagination:
    def __init__(self, items=None, pageSize=10):
        self.items = [items[i:i+int(pageSize)]
                      for i in range(0, len(items), int(pageSize))]
    current_item_index = 0

    def totalPages(self):
        print(f"You have {len(self.items)} pages in total")

    def currentPage(self):
        print(f"Current page is: {self.current_item_index+1}")

    def getVisibleItems(self):
        print(self.items[self.current_item_index])

    def prevPage(self):
        if self.current_item_index > 0:
            self.current_item_index -= 1
        else:
            print("This is first page:")
            return

    def nextPage(self):
        if self.current_item_index < (len(self.items)-1):
            self.current_item_index += 1
        else:
            print("This is last page:")
            return

    def firstPage(self):
        self.current_item_index = 0

    def lastPage(self):
        self.current_item_index = len(self.items)-1

    def goToPage(self, pageNum):
        x = int(pageNum)-1
        if x >= 0 and x <= len(self.items)-1:
            self.current_item_index = x
        elif x > len(self.items)-1:
            self.current_item_index = len(self.items)-1
        else:
            self.current_item_index = 0


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)
p.getVisibleItems()
p.nextPage()
p.getVisibleItems()
p.lastPage()
p.getVisibleItems()
p.goToPage(3.4)
p.getVisibleItems()
p.totalPages()
p.currentPage()
