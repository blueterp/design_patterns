The main use case of this pattern is to define several iteration strategies for a given collection so that the client can use the desired strategy as needed (for example think about iterating forward backwards or randomly).
Two interfaces are defined and implemented to allow for dependency inversion in the design.

Main components
Iterator interface: Interface that specifies methods required for interface. Note that in python the iterator protocol requires the **iter** method (must return an interator object- typically self) and **next** method (that returns the next valur or raises StopIterationError when done)
Concrete Iterator: Implements interface
IterableCollection: Interface that specifies methods for getting iterators that can be used on the collection
ConcreteCollection: Implements the methods for getting the iterators
