import os


def read(fn: str) -> str:
    """Read local file

    Args:
    fn: File name or path

    Returns:
    The content of the requested file
    """

    if fn.startswith("~"):
        fn = os.path.expanduser(fn)

    # with open(fn, "r") as file:
    #     return file.read()

    confirm = input("Do you give permission [y/n]: ").lower() == "y"

    if confirm:
        with open(fn, "r") as file: 
            return file.read()

    else:
        return "User did not give permission to read this file!"


__all__ = ["read"]
