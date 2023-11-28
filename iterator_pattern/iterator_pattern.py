"""
The python iterator interface requires the following methods
class Iterator:
    def __iter__(self, *args, **kwargs):
    '''
    must return self
    '''
    # do something
    return self

    def __next__(self):
    '''
    determines what to return or raises StopIterationError 
    '''

"""

from collections.abc import Iterable, Iterator

class OrderedIterator(Iterator):
    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self.index = -1 if reverse else 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self._collection) or -self.index > len(self._collection):
            raise StopIteration
        else:
            value = self._collection[self.index]
            self.index += -1 if self._reverse else 1
            return str(value)
        
class NumberCollection(Iterable):
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return OrderedIterator(self._collection)
    
    def get_reverse_iterator(self):
        return OrderedIterator(self._collection, reverse=True)
    
    def add_item(self, item):
        self._collection.append(item)


if __name__ == "__main__":
    numbers = [1,2,3,4,5]

    iterable = NumberCollection(numbers)

    print("".join(iterable))
    print("".join(iterable.get_reverse_iterator()))
