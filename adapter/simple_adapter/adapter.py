from abc import ABC, abstractclassmethod


class TargetInterface(ABC):
    """
    Interface that your program is currently using/needs to support.
    """

    @abstractclassmethod
    def open(self):
        """
        Must be implemented by subclass.
        """
        pass

    @abstractclassmethod
    def close(self):
        """
        Must be implemented by subclass.
        """
        pass


class ServiceInterface(ABC):
    """
    Legacy interface implemented by legacy code. Because it does not conform with
    the target interface an adapter will be needed to wrap around the existing object.
    """

    def connect(self):
        """
        Must be implemented by subclass.
        """
        pass

    def release(self):
        """
        Must be implemented by subclass.
        """
        pass


class NewConnector(TargetInterface):
    """
    Simplistic connector that implements TargetInterface
    """

    def __init__(self, id):
        """
        Simple initializer that ties id to object.
        """
        self.id = id

    def open(self):
        """
        Simple implemented interface method to show functionality when called.
        In real example might include a connection object.
        Note differt from ServiceInterface.
        """
        print(f"connection id: {self.id} is now open.")

    def close(self):
        """
        Simple implemented interface method to show functionality when called.
        In real example might include a connection object.
        Note differt from ServiceInterface.
        """
        print(f"connection id: {self.id} is now closed.")


class OldConnector(ServiceInterface):
    """
    Legacy connector that implements ServiceInterface.
    """

    def __init__(self, name):
        """
        Simple initializer that ties name to object.
        """
        self.name = name

    def connect(self):
        """
        Simple implemented interface method to show functionality when called.
        In real example might include a connection object.
        Note differt from TargetInterface.
        """
        print(f"Connection {self.name} is connected.")

    def release(self):
        """
        Simple implemented interface method to show functionality when called.
        In real example might include a connection object.
        Note differt from TargetInterface.
        """
        print(f"Connection {self.name} is released.")


class Adapter(TargetInterface):
    """
    Adapter that makes ServiceInterface based objects useable by TargetInterface based objects.
    """

    def __init__(self, legacy_object: ServiceInterface) -> None:
        """Requires object that adheres to ServiceInterface."""
        self.legacy_object = legacy_object

    def open(self):
        """Adheres to target interface, but uses legacy interface implementation"""
        self.legacy_object.connect()

    def close(self):
        """Adheres to target interface, but uses legacy interface implementation"""
        self.legacy_object.release()


class TargetInterfaceUser:
    """
    Object that uses a TargetInterface Object.
    """

    def __init__(self, connection_object: TargetInterface):
        """
        connection object must adhere to the TargetInterface.
        Existing ServiceInterface objects won't work.
        """
        self.connection_object = connection_object

    def open_connection(self):
        """
        Leverages interface of object for dependency inversion
        """
        self.connection_object.open()

    def close_connection(self):
        """
        Leverages interface of object for dependency inversion
        """
        self.connection_object.close()

    def test_connection(self):
        """
        Method to demonstrate use of other methods
        """
        self.open_connection()
        self.close_connection()


if __name__ == "__main__":
    # create connector objects - one old and one new
    target_connector = NewConnector(id=1)
    service_connector = OldConnector(name="old")

    # wrap old connector in adapter object
    adapter = Adapter(service_connector)

    # can now implement targetInterfaceUsers with both objects
    target1 = TargetInterfaceUser(target_connector)
    target2 = TargetInterfaceUser(adapter)

    target1.test_connection()
    target2.test_connection()
