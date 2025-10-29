import hashlib
def main():
    hash_set = {}
    with open('hashes.txt', 'r') as h:
        for line in h:
            hash_set.append(line.strip("\n"))
            print(hash_set)

# if "__name__" == "__main__":
    main()