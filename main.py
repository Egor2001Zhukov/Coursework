from utils.functions import load_jsonfile, last_five_operations


def main():
    operations = load_jsonfile("operations.json")
    result = last_five_operations(operations)
    return result


if __name__ == '__main__':
    print(main())
