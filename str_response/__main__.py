import argparse
import str_response


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", required=True)
    args = parser.parse_args()

    number = int(args.n)

    str_returned = str_response.get_str(n=number)
    # print(str_returned)


if __name__ == "__main__":
    main()
