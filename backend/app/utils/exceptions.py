class NexusFlowError(Exception):
    """Base exception for NexusFlow."""


class NotFoundError(NexusFlowError):
    """Raised when a resource is not found."""
