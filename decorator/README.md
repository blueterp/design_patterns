Decorator / Wrapper Pattern

Client - invokes the deocrated object
Component interface - interface for both wrappers and wrapped objects
Concrete components - class of objects being wrapped. Implements behavior specified in interface
Base decorator (superclass for decorators) - has reference to wrapped object. The decorator delegates operations to the wrapped object
Concrete decorators (Subclass for decorators) - Define extra behavior to be added to wrapped object by overriding methods of the base decorator.

Useful method to avoid class explosion.
