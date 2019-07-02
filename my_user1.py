from admin import Admin

andy = Admin('andy','nahayo','naandy','naandy@gmail.com', 'Bujumbura')
andy.describe_user()

andy_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
andy.privileges.privileges = andy_privileges

print("\nThe admin " + andy.username + " has these privileges: ")
andy.privileges.show_privileges()