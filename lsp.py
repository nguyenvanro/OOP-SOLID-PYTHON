"""
Liskov Substitution Principle
- Subtypes must be substitutatble for their base types.
"""

from abc import ABC, abstractmethod


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
    
    
class UserRepository(ABC):
    @abstractmethod
    def save_user(self, user):
        pass
    
    
class DatabaseUserRepository(UserRepository):
    def save_user(self, user):
        print(f"Saving user {user.username} to the database")
    

class SpecialDatabaseUserRepository(UserRepository):
    def save_user(self, user):
        print(f"Saving user {user.username} to a special database")
    
    
class EmailService(ABC):
    @abstractmethod
    def send_mail(self, user, message):
        pass
    
    
class SimpleEmailService(EmailService):
    def send_mail(self, user, message):
        print(f"Sending email to {user.email}: {message}")
    

class Logger(ABC):
    @abstractmethod
    def log_action(self, action):
        pass


class SimpleLogger(Logger):
    def log_action(self, action):
        print(f"Logging action: {action}")
    
            
# Usage
def save_user(user_repo: UserRepository, user: User):
    user_repo.save_user(user)
    
    
user = User(username="nguyenvana", email="nguyenvana@gmail.com")
user_repo = DatabaseUserRepository()
special_user_repo = SpecialDatabaseUserRepository()

# Both repositories should work without changing the behavior
save_user(user_repo, user)
save_user(special_user_repo, user)
