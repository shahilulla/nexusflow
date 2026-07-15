class DatasetNotFoundException(Exception):
    def __init__(self):
        self.message = "Dataset not found"
        super().__init__(self.message)


class DatasetAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.message = f"Dataset '{name}' already exists."
        super().__init__(self.message)