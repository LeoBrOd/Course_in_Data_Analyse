# ### Question: Implement a `Time` class
# Create a Python class named `Time` that represents a time of day, with the following requirements:
# #### Class Details:
# 1. **Attributes:**
#    - `hours` (int): Represents the hour component of the time (0-23).
#    - `minutes` (int): Represents the minute component of the time (0-59).
#    - `seconds` (int): Represents the second component of the time (0-59).
# 2. **Initialization:**
#    - The `__init__` method should initialize the `hours`, `minutes`, and `seconds` attributes. If no values are passed, default to 0 for each.
# 3. **Class Method:**
#    - `from_string`: Accepts a time as a string formatted as "HH:MM:SS" and returns an instance of `Time`.
# 4. **Static Method:**
#    - `validate_time`: Accepts three parameters `hours`, `minutes`, and `seconds` and returns `True` if the time is valid (within the correct range) or `False` otherwise.
# 5. **Properties and Setter:**
#    - Use properties for `hours`, `minutes`, and `seconds` that validate the time whenever they are set. Raise a `ValueError` if a value outside the allowed range is set.
# 6. **Special Methods:**
#    - Implement the `__str__` method to return the time formatted as "HH:MM:SS".
#    - Implement the `__eq__` method to allow comparison of two `Time` instances based on their time values.
# #### Example Usage:
# t1 = Time(14, 30, 0)
# print(t1)  # Output: "14:30:00"
# t2 = Time.from_string("03:45:15")
# print(t2)  # Output: "03:45:15"
# print(t1 == t2)  # Output: False
# try:
#     t1.hours = 25
# except ValueError as e:
#     print(e)  # Output: "Invalid hour: 25"

# class Time:
#     hours = range(23)
#     minutes = range(59)
#     seconds = range(59)

#     def __init__(self, hours=0, minutes=0, seconds=0):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         if self.validate_time() == False:
#             raise ValueError("value outside the allowed range is set")

#     def from_string(self, str):
#         str_to_list = list(str.split(":"))
#         return Time(str_to_list[0], str_to_list[1], str_to_list[2])

#     def validate_time(self):
#         if self.hours in Time.hours and self.minutes in Time.minutes and self.seconds in Time.seconds:
#             return True
#         return False

#     def __str__(self):
#         print(f"{self.hours}:{self.minutes}:{self.seconds}")

#     def __eq__(self, another_instance):
#         if self.hours == another_instance.hours and self.minutes and self.hours == another_instance.hours == another_instance.minutes and self.seconds == another_instance.seconds:
#             return True
#         return False


# t1 = Time(14, 30, 0)
# print(t1)
# t2 = Time.from_string("03:45:15")
# print(t2)
# print(t1 == t2)
# try:
#     t1.hours = 25
# except ValueError as e:
#     print(e)

class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self.validate_time(self._hours, self._minutes, self._seconds)

    @classmethod
    def from_string(cls, time_str):
        hours, minutes, seconds = map(int, time_str.split(':'))
        return cls(hours, minutes, seconds)

    @staticmethod
    def validate_time(hours, minutes, seconds):
        if not (0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59):
            raise ValueError(f"Invalid time: {hours:02}:{
                             minutes:02}:{seconds:02}")

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        if 0 <= value <= 23:
            self._hours = value
        else:
            raise ValueError("Invalid hour: {}".format(value))

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value):
        if 0 <= value <= 59:
            self._minutes = value
        else:
            raise ValueError("Invalid minute: {}".format(value))

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value):
        if 0 <= value <= 59:
            self._seconds = value
        else:
            raise ValueError("Invalid second: {}".format(value))

    def __str__(self):
        return f"{self._hours:02}:{self._minutes:02}:{self._seconds:02}"

    def __eq__(self, other):
        if isinstance(other, Time):
            return (self._hours, self._minutes, self._seconds) == (other.hours, other.minutes, other.seconds)
        return False


# Example usage:
t1 = Time(14, 30, 0)
print(t1)  # Output: "14:30:00"
t2 = Time.from_string("03:45:15")
print(t2)  # Output: "03:45:15"
print(t1 == t2)  # Output: False
try:
    t1.hours = 25
except ValueError as e:
    print(e)  # Output: "Invalid hour: 25"
