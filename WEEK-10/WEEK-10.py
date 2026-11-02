# Hashing using Separate Chaining, Linear Probing
# and Quadratic Probing

SIZE = 10

# Separate Chaining
def separate_chaining(keys):
    hash_table = [[] for _ in range(SIZE)]

    for key in keys:
        index = key % SIZE
        hash_table[index].append(key)

    print("\nSeparate Chaining:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])


# Linear Probing
def linear_probing(keys):
    hash_table = [-1] * SIZE

    for key in keys:
        index = key % SIZE

        while hash_table[index] != -1:
            index = (index + 1) % SIZE

        hash_table[index] = key

    print("\nLinear Probing:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])


# Quadratic Probing
def quadratic_probing(keys):
    hash_table = [-1] * SIZE

    for key in keys:
        index = key % SIZE
        j = 0

        while j < SIZE:
            new_index = (index + j * j) % SIZE

            if hash_table[new_index] == -1:
                hash_table[new_index] = key
                break

            j += 1

        if j == SIZE:
            print("Cannot insert", key, "- Table is full")

    print("\nQuadratic Probing:")
    for i in range(SIZE):
        print(i, ":", hash_table[i])


# Main Program
keys = [23, 43, 13, 27, 37, 33]

separate_chaining(keys)
linear_probing(keys)
quadratic_probing(keys)