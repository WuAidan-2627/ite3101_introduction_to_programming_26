def shut_down(yes) -> str:
    if sshut_down(yes):
        print("Shutting down")
    elif s == "no":
        print("Shutdown aborted")
    else:
        print("Sorry")
