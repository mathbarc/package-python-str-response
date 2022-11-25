import argparse
from . import str_response

def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--image", required=True)
    # parser.add_argument("--num_clusters", required=False)
    # parser.add_argument("--show", required=False, default=1)
    args = parser.parse_args()

    str_returned = str_response.get_str(n=1)
    print(str_returned)

if __name__ == "__main__":
    main()
