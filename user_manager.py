import bcrypt
from models import User

class UserManager:
    def __init__(self, session):
        self.session = session

    def create_user(self, username, email, password):
        # Check if a user with the provided email already exists
        existing_user = self.session.query(User).filter_by(email=email).first()
        if existing_user:
            return False, "User with this email already exists.", None

        # Hash the password using bcrypt
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

        # Create a new User object with the hashed password
        new_user = User(username=username, email=email, password=hashed_password)

        # Add the new_user object to the session
        self.session.add(new_user)
        
        # Commit the transaction to save the changes to the database
        self.session.commit()

        return True, "User created successfully.", new_user.id

    def authenticate_user(self, email, password):
        # Find the user with the provided email
        user = self.session.query(User).filter_by(email=email).first()

        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return True, "User authenticated successfully.", user.id
        else:
            return False, "Authentication failed. Invalid email or password.", None
