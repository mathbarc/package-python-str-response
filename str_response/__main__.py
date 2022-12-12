import argparse
from importlib.machinery import SourceFileLoader

str_response = SourceFileLoader(
    "str_response", "./str_response/__init__.py"
).load_module()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", required=True)
    args = parser.parse_args()

    number = int(args.n)

    str_returned = str_response.get_str(n=number)
    print(str_returned)


if __name__ == "__main__":
    main()
