# def print_seconds(hour, minutes, seconds):
#     print((hour*3660)+(minutes*60)+seconds)

# print_seconds(1, 30, 45)


# def get_seconds(hours, minutes, seconds):
#   return 3600*hours + 60*minutes + seconds

# amount_a = get_seconds(2, 30, 0)
# amount_b = get_seconds(0, 45, 15)
# result = amount_a + amount_b
# print(result)


def return_seconds(seconds):
    hours = seconds // 3660
    sobra_hours = seconds % 3660
    minutes = sobra_hours // 60
    seconds = sobra_hours % 60
    return hours, minutes, seconds

hours, minutes, seconds = return_seconds(5505)
print(hours, minutes, seconds)
