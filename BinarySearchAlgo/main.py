class BinarySearchAlgo:
    def __init__(self, list_array, number_to_search):
        self.list = list_array
        self.number_to_search = number_to_search

    def BinarySearch(self):
        while True:
            mid = (0 + len(self.list))//2
            if self.number_to_search == self.list[mid]:
                return print("Found number")
            elif self.list[mid] > self.number_to_search:
                self.list = self.list[:mid]
            else:
                self.list = self.list[mid:]

            if len(self.list)==1  and self.list[0] != self.number_to_search :
                return print("Number not in list")

if __name__ == "__main__":
    list_array = [1,4,5,6,7,8,10,11,33]
    number_to_search = 100
    x = BinarySearchAlgo(list_array, number_to_search)
    x.BinarySearch()


