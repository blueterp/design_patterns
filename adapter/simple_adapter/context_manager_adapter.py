from abc import ABC, abstractclassmethod


class ManagedWriterInterface(ABC):
    """
    Interface for connector that uses context manager to managed connections
    """

    @abstractclassmethod
    def __enter__(self):
        pass

    @abstractclassmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    @abstractclassmethod
    def write(self, text):
        pass


class UnmangedWriterInterface(ABC):
    """
    Interface for connector that manually manages connections
    """

    @abstractclassmethod
    def file_open(self):
        pass

    @abstractclassmethod
    def file_close(self):
        pass


class NewWriter(ManagedWriterInterface):
    """
    Simple writer that implements a context manager when writing to file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "a")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.file = None

    def write(self, text):
        try:
            self.file.write(text + "\n")
        except ValueError as e:
            print("Cannot write to closed file")


class OldWriter(UnmangedWriterInterface):
    """
    Simple writer that requires user to explicitly open and close file.
    """

    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def file_open(self):
        self.file = open(self.filename, "a")

    def file_close(self):
        self.file.close()
        self.file = None


class ContextManagerAdapter(ManagedWriterInterface):
    """
    Adapter to add context management interface for writers that
    explicitly call opening and closing to files.
    """

    def __init__(self, connector: UnmangedWriterInterface):
        self.connector = connector

    def __enter__(self):
        self.connector.file_open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connector.file_close()

    def write(self, text):
        self.connector.file.write(text + "\n")


class FileWriter:
    """
    Object that requires writer that conforms to ManagedWriterInterface.
    """

    def __init__(self, writer: ManagedWriterInterface):
        self.writer = writer

    def write(self, text):
        with self.writer:
            self.writer.write(text + "\n")


if __name__ == "__main__":
    # create old and new writers
    new_writer = NewWriter("new_writer.txt")
    old_writer = OldWriter("old_writer.txt")

    # adapt old writer to comply with ManagedWriterInterface
    adapted_writer = ContextManagerAdapter(old_writer)

    with new_writer as w:
        w.write("ABCEFG")

    with adapted_writer as w:
        w.write("HIJKLMNOP")
