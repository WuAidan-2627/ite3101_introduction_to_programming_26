def shut_down(s: str) -> str:
    if shut_down("yes"):
        return "Shutting down"
    elif shut_down("no"):
        return "Shutdown aborted"
    else:
        print("Sorry")
