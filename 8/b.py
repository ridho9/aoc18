from collections import defaultdict

data = [int(x) for x in input().split()]


def recurse(data, index):
    # return (value, index after last)

    print("recurse ", index)
    child_num = data[index]
    metadata_num = data[index + 1]
    print("cn {} mn {}".format(child_num, metadata_num))

    index += 2
    result = 0

    child_value = defaultdict(int)

    for i in range(1, child_num + 1):
        r = recurse(data, index)
        index = r[1]
        child_value[i] = r[0]

    print(child_value)

    for _ in range(metadata_num):
        if child_num == 0:
            result += data[index]
            index += 1
        else:
            m = data[index]
            result += child_value[m]
            index += 1

    return (result, index)


print(recurse(data, 0))
