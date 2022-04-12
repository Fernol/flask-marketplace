import unittest
from marketplace import User, db
from werkzeug.security import generate_password_hash, check_password_hash


class MyTestCase(unittest.TestCase):
    email = "alexey.hmelenko@gmail.com"
    password = "Aaasdasd"
    passwordHash = generate_password_hash(password)

    def test_password(self):
        self.assertEqual(True, check_password_hash(MyTestCase.passwordHash, MyTestCase.password))

    def test_register(self):
        user = User.query.filter_by(email=MyTestCase.email).first()
        self.assertEqual(user.email, MyTestCase.email)


if __name__ == '__main__':
    unittest.main()
