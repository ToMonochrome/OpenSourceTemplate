import argparse

from {{ cookiecutter.package_name }}.core import greet


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="{{ cookiecutter.package_name }}",
        description="{{ cookiecutter.project_description }}",
    )
    parser.add_argument("name", nargs="?", default="world", help="Who to greet.")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
