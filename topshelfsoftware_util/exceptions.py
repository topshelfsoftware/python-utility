"""Custom exceptions defined here."""


class ModuleError(RuntimeError):
    """Raised to indicate a module failure."""

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
