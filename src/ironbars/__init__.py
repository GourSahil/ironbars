from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("ironbars")
except PackageNotFoundError:
    # Fallback for local development
    __version__ = "0.0.0"