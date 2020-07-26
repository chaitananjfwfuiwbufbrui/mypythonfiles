import sys

# the setrecursionlimit function is
# used to modify the default recursion
# limit set by python. Using this,
# we can increase the recursion limit
# to satisfy our needs

sys.setrecursionlimit(10 ** 6)


def dirReduc(arr):


    for i in range(len(arr)):
        if len(arr) == 1:
            break

        elif i == len(arr):
            break
        elif arr[i] == "NORTH":
            if IndexError:
                return arr
            elif i + 1 == len(arr):
                break
            elif arr[i + 1] == "SOUTH":
                arr.remove(arr[i+1])
                arr.remove(arr[i])
        elif arr[i] == "SOUTH":
            if i + 1 == len(arr):
                break
            elif arr[i + 1] == "NORTH":
                arr.remove(arr[i+1])
                arr.remove(arr[i])
        elif arr[i] == "EAST":
            if i + 1 == len(arr):
                break
            elif arr[i + 1] == "WEST":
                arr.remove(arr[i+1])
                arr.remove(arr[i])
        elif arr[i] == "WEST":
            if i + 1 == len(arr):
                break
            elif arr[i + 1] == "EAST":
                arr.remove(arr[i+1])
                arr.remove(arr[i])
    # second part
    for a in range(len(arr)):
        if a == len(arr):
            break
        elif arr[a] == "NORTH":
            if a + 1 == len(arr):
                break
            elif arr[a + 1] == "SOUTH":
                dirReduc(arr)
        elif arr[a] == "SOUTH":
            if a + 1 == len(arr):
                break
            elif arr[a + 1] == "NORTH":
                dirReduc(arr)
        elif arr[a] == "WEST":
            if a + 1 == len(arr):
                break
            elif arr[a + 1] == "EAST":
                dirReduc(arr)
        elif arr[a] == "EAST":
            if a + 1  == len(arr):
                break
            elif arr[a + 1] == "WEST":
                dirReduc(arr)
    return arr
a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
x = dirReduc(a)

print(dirReduc(x))
