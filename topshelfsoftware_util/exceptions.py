"""Custom exceptions defined here."""


class ModuleError(RuntimeError):
    """Raise to indicate a module error at runtime."""

    ...


class ValidationError(Exception):
    """Raise to indicate invalid user input."""

    ...
