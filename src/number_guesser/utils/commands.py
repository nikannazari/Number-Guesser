EXIT_COMMANDS = {
    "q",
    "quit",
    "exit",
}


def is_exit_command(value: str) -> bool:
    """Return True when the input represents an exit command."""
    return value.strip().lower() in EXIT_COMMANDS