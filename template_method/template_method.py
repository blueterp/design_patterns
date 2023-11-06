from abc import ABC, abstractclassmethod
import pandas as pd
import json


class Preprocessor(ABC):
    """
    Superclass that defines the template_method and subtasks for preprocessing data.
    """

    def pre_process(self):
        """
        Template method
        """
        self.load_data()
        self.manage_missing_data()
        self.presist_preprocessed_data()
        self.hook()

    @abstractclassmethod
    def load_data(self):
        """
        Load data from source
        """
        pass

    def manage_missing_data(self):
        """
        Ientify missing datapoints and apply technique for managing records with missing fields
        """
        pass

    def persist_preprocessed_data(self):
        """
        Persist data to storage. Can be to disk or database for example.
        """
        pass

    def hook(self):
        """
        Optional method to be implemented by subclass.
        """
        return


class ExcelPreprocessor(Preprocessor):
    def __init__(self, filename):
        if ".xlsx" not in filename or ".xls" not in filename:
            raise FileNotFoundError("ExcelPreprocessor can only process Excel files.")

    def load_data(self):
        """
        Read data into pandas dataframe
        """
        self.data = pd.read_excel(self.filename)

    def manage_missing_data(self):
        """
        Drop all records that include a missing field
        """
        return self.data.dropna(inplace=True).reset_index(inplace=True)

    def persist_preprocessed_data(self):
        """
        Write preprocessed file to disk. File name prefaced with preprocessed
        to distinguish from original file.
        """
        pd.to_excel(f"preprocessed_{self.filename}")

    def hook(self):
        """
        Overridden method.
        """
        self.notify_user("fake@hotmail.com")

    def notify_user(email: str):
        """
        Dummy method to demonstrate notifying user via email. In real implementation could use SMTP
        to send email to user to notify them of preprocessing.
        """
        print(f"Sending email to {email}. Preprocessing complete.")


class JsonPreprocessor(Preprocessor):
    def __init__(self, filename):
        if ".json" not in filename:
            raise FileNotFoundError("JsonPreprocessor can only process Json files.")
        self.filename = filename

    def load_data(self):
        """
        Read data into pandas.
        """
        self.data = pd.read_json(self.filename, orient="records")

    def manage_missing_data(self):
        """
        Drop all records that include a missing field
        """
        return self.data.fillna()

    def persist_preprocessed_data(self):
        """
        Write preprocessed file to disk. File name prefaced with preprocessed
        to distinguish from original file.
        """
        pd.to_json(f"preprocessed_{self.filename}", orient="records")


if __name__ == "__main__":
    excel_data = ExcelPreprocessor("data.xlsx")
    json_data = JsonPreprocessor("data.json")

    excel_data.pre_process()
    json_data.pre_process()
