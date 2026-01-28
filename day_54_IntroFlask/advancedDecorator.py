'''
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def _is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper

@_is_authenticated_decorator
def create_blog_post(user):
    print(f'this is {user.name} new blog post')

new_user = User('renato')
new_user.is_logged_in = True
create_blog_post(new_user)'''


def is_feet_on_tail(function):
    def wrapper(*args, **kwargs):
        self = args[0]

        if not self.feet_on_tail:
            return "failed: feet not on tail"

        return function(*args, **kwargs)

    return wrapper

class Skatista:
    def __init__(self, name, base):
        self.name = name
        self.base = base
        self.feet_on_tail = False

    @is_feet_on_tail
    def hit_a_flip(self):
        return 'did a kickflip'

skatista = Skatista('renato', 'regular')
skatista.feet_on_tail = True
print(skatista.hit_a_flip())