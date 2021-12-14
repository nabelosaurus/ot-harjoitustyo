def validate_input(login):
        valid = True
        error_msg = ""
        if not login.website:
            error_msg += "Website must be present. "
            valid = False
        if not login.password:
            error_msg += "Password must be present. "
            valid = False
        if not login.username and not login.email:
            error_msg += "Username and email can not both be empty. "
            valid = False
        if len(login.website) < 4:
            error_msg += "Website length must be greater than four characters. "
            valid = False
        if len(login.password) < 1:
            error_msg += "Password must be atleast one character. "
            valid = False
        if login.username:
            if 0 < len(login.username) < 2:
                print(login.username)
                error_msg += "The username must be longer than 1 character. "
                valid = False
        if login.email:
            if 0 < len(login.email) < 6:
                error_msg += "The email must be longer than 5 characters. "
                valid = False
        if not login.salt:
            valid = False
        return valid, error_msg