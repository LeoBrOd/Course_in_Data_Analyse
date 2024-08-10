import string
import random
import datetime
import faker

# Exercise 1: Currencies


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f"{self.amount} {self.currency}`s"

    def __int__(self):
        return int(self.amount)

    def __repr__(self):
        return f"{self.amount} {self.currency}`s"

    def __add__(self, value):
        if isinstance(value, Currency):
            if self.currency != value.currency:
                raise ValueError("Can not add different curencies")
            return self.amount+value.amount
        else:
            return self.amount+value

    def __iadd__(self, value):
        if isinstance(value, Currency):
            if self.currency != value.currency:
                raise ValueError("Can not add different curencies")
            self.amount += value.amount
        else:
            self.amount += value
        return self


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1+c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
# c1+=c3
# print(c1)

# Exercise 3: String Module
chars = string.ascii_letters
random_string = ''.join(random.choice(chars) for i in range(5))
print(random_string)

# Exercise 4 : Current Date


def current_date():
    cd = datetime.date.today().strftime("%m/%d")
    return cd


print(current_date())

# Exercise 5 : Amount Of Time Left Until January 1st


def days_till_jan_first():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    next_jan = f"{datetime.date.today().year+1}-1-1 00:00:00"
    days_left_till = datetime.datetime.strptime(
        next_jan, '%Y-%m-%d %H:%M:%S')-datetime.datetime.strptime(current_date, '%Y-%m-%d %H:%M:%S')
    print(f"The 1st of January is in: {days_left_till}")


days_till_jan_first()

# Exercise 6 : Birthday And Minutes


def life_in_minutes(birthday):
    formated_birthday = datetime.datetime.strptime(birthday, "%Y-%m-%d")
    now = datetime.datetime.now()
    already_alive = now-formated_birthday
    life_in_minutes = int(already_alive.total_seconds()/60)
    print(f"You are {life_in_minutes} minutes old")


life_in_minutes("2023-10-12")

# Exercise 7 : Faker Module
users = []


def add_user():
    fake = faker.Faker()
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.locale()[:2]}
    users.append(user)


add_user()
add_user()
add_user()
add_user()
add_user()
print(users)
