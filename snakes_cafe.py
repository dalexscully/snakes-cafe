from textwrap import dedent


def decor(fx):
    def wrap():
        print('***********************************')
        fx()
        print('***********************************')

    return wrap


def print_welcome():
    print('*** Welcome to the Snakes Cafe! ***')
    print('***Please see our Menu Below.   ***')
    print('***                             ***')


def order_prompt():
    print('** What would you like to order **')


food_dict = {
    'Wings': 0,
    'Cookies': 0,
    'Spring Rolls': 0,
    'Salmon': 0,
    'Steak': 0,
    'Meat Tornado': 0,
    'A literal Garden': 0,
    'Ice Cream': 0,
    'Cake': 0,
    'Pie': 0,
    'Coffee': 0,
    'Tea': 0,
    'Unicorn Tears': 0
}

# variables for decor

decorated_welcome = decor(print_welcome)

decorated_order_prompt = decor(order_prompt)

# function welcome call
decorated_welcome()

# menu to render on run
menu_items = dedent("""
Appetizers
----------
{}
{}
{}

Entrees 
----------
{}
{}
{}
{}

Desserts
----------
{}
{}
{}

Drinks
------
{}
{}
{}
""".format(*food_dict)
                    )
print(menu_items)

# calls user order
decorated_order_prompt()  # calls what you would like to order

user = input('> ')

food_dict = {}
while user != "quit":
    if user not in food_dict:
        food_dict[user] = 0
    food_dict[user] += 1
    print(user)
    print(food_dict[user])
    print(f"** {food_dict[user]} order of {user} have been added to your meal")
    user = input('> ')

# increment repeated items

