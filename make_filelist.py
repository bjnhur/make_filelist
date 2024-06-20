import os
import argparse
import fnmatch


def create_file_list(directory, output_file, file_filter=None, recursive=False):
    file_list = []

    if recursive:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file_filter and not fnmatch.fnmatch(file, file_filter):
                    continue
                file_list.append(os.path.join(root, file))
    else:
        for file in os.listdir(directory):
            if os.path.isfile(os.path.join(directory, file)):
                if file_filter and not fnmatch.fnmatch(file, file_filter):
                    continue
                file_list.append(os.path.join(directory, file))

    with open(output_file, "w") as f:
        for file in file_list:
            f.write(file + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a file list from a directory with an optional filter.")
    parser.add_argument("directory", type=str, help="The directory to search for files")
    parser.add_argument("output_file", type=str, help="The output file to write the file list to")
    parser.add_argument(
        "--filter",
        type=str,
        help='Optional filter to include only files matching this pattern (e.g., "*.tcl", "example*.exe")',
    )
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively search files in the directory")

    args = parser.parse_args()

    create_file_list(args.directory, args.output_file, args.filter, args.recursive)
    print(f"File list has been saved to {args.output_file}")
