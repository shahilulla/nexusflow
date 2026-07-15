class DatasetNotFoundException(Exception):
    def __init__(self):
        self.message = "Dataset not found"
        super().__init__(self.message)