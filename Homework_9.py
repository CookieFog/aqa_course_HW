# hw_1
def generator(start: int, stop: int, step: int = 1):
    value = start
    while value <= stop:
        yield value
        value += step


for index in generator(0, 10):
    print("generator", index)

for index in range(0, 10):
    print("range", index)

# # hw_2


# def generator():
#     counter = 0
#     while True:
#         yield counter
#         counter += 1
#
#
# # gen = generator()
# for index in generator():
#     print(index)
#     if index == 10:
#         break
