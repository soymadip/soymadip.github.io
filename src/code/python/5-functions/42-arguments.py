# chai = "ginger chai"


# # function defination
# def prepare_chai(order):  # parameters (declaration)
#     print(f"preparing: {order}")


# prepare_chai(chai) # doesnt change the orignal one. just passes copy


chai = [1, 2, 3]


def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)  # changes orignal object/variable
print(chai)


# 2 types or args.
# args, *kwargs (keyworded args)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("Darjeeling", "milk", "Low")  # positional args
make_chai(tea="green", sugar="medium", milk="no")  # Keywords, no need to maintain order


def special_chai(*ingredients, **extras):
    print(ingredients)
    print(extras)


special_chai("cardimum", "ginger", sweetner="honey", foam="yes")

# ingredients get list, kwargs get dict


# we can give default values
def chai(type="lemon"):
    print(chai)


# default trap
def chai_order(order=[]):
    order.append("Masala")
    print(order)


chai_order()
chai_order()  # appended 2 times

# Fix


def chai_order(order=None):
    if order is None:  # append only if provided
        order = []
        print(order)


chai_order()
chai_order()
