data = [int(x) for x in input().split()]


def recurse(data, index):
    # return (value, index after last)

    print("recurse ", index)
    child_num = data[index]
    metadata_num = data[index + 1]
    print("cn {} mn {}".format(child_num, metadata_num))

    index += 2
    result = 0

    for _ in range(child_num):
        r = recurse(data, index)
        index = r[1]
        result += r[0]

    for _ in range(metadata_num):
        result += data[index]
        index += 1

    return (result, index)


print(recurse(data, 0))
