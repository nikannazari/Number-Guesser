EXIT_COMMANDS = {
    "q",
    "quit",
    "exit",
}


def is_exit_command(command: str) -> bool:
    """Return True if the command is an exit command."""

    return command.strip().lower() in EXIT_COMMANDS