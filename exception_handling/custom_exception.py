class CustomException(Exception):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(message)
        self.message = message
        self.error = error

    def __str__(self):
        if self.error:
            return f"{self.message} | Original Error: {str(self.error)}"
        return self.message