# import sys
# import time

# KEYWORD ARGUMENTS


def add_profile(index: str, ix: float, iy: float) -> None:
    print(f"Adding profile {index} with amounts of inertia ix={ix} cm1, iy={iy} cm")


add_profile("test", 25.9, 82.1)

# DEFAULT ARGUMENTS
print("1_line", "Hello", sep="", end=" ")
print("2_line", "Hello", sep=" ")

print("1_line", "Hello", end="|")
print("2_line", "Hello")


def add_item(item_name: str, quantity: int = 1) -> None:
    print(f"{quantity:,} units of {item_name.capitalize()} were added.")


add_item("bread")
add_item("apples", 20_000)

# FLUSH PARAMETER
# terminal output is buffered by default, because printing each individual character is expensive
# if you forcibly flush stdout, everything will be printed instantly, which is useful for debugging
# std::cout = buffered
# std::clog = buffered
# std::cerr = unbuffered


# ARGS
def print_numbers(*numbers) -> None:
    for n in numbers:
        print(n)


def summarize(*numbers) -> int:
    sum: int = 0
    for n in numbers:
        sum += n
    return sum


print(f"The sum of the numbers is {summarize(1, 2, 3, 4, 5)}.")


# KWARGS
def add_user(**user):
    print(user)  # dictionary


def print_user(**user):
    for key, value in user.items():
        print(f"{key} = {value}")


add_user(id=1, name="John", surname="Kowalski", age=25)
print_user(id=1, name="John", surname="Kowalski", age=25)

###

users: list[dict] = list()


def add_user_to_dict(**user) -> None:
    users.append(user)


add_user_to_dict(id=1, name="John", surname="Kowalski", age=25)
add_user_to_dict(id=1, name="Jessica", surname="Supergirl", age=26)
print(users)
