def passwords_match(password, verification):
    if password == verification:
        return True
    return False


def check_password_length(password):
    if len(password) >= 10:
        return True
    return False


if __name__ == "__main__":
    pass
