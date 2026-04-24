import os


def write(fn: str, data: str):
    """Read local file

    If the target path is not within the pwd, the user will be prompted for confirmation.

    Args:
        fn: File name or path
        data: Content to write

    Returns:
        Error string may be returned
    """

    if fn.startswith("~"):
        fn = os.path.expanduser(fn)

    pwd = os.path.realpath(os.getcwd())
    target = os.path.realpath(fn)

    is_inside = os.path.commonpath([pwd, target]) == pwd

    # print(is_inside)

    if not is_inside:
        confirm = (
            input("Do you give write permission {" + fn + "} [y/n]: ").lower() == "y"
        )
        if not confirm:
            return "User did not give file write permission!"

    with open(fn, "w") as file:
        file.write(data)

    return "File write successful."

__all__ = ["write"]
