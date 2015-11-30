from models.business import Business
from models.user import User
business = Business("name", "id")
user = User("username", "usersID")
print(business.name)
print(user.name)