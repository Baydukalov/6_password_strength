import getpass
import passwordmeter


def get_password_strength(password_strength):
    password_grade, suggestions = password_strength
    password_grade = int(password_grade * 10)
    if password_grade > 1:
        print("Password strength {:d} out of 10".format(password_grade))
    else:
        print ('Your password is too weak.')


if __name__ == '__main__':
    user_password = getpass.getpass()
    password_strength = passwordmeter.test(user_password)
    get_password_strength(password_strength)