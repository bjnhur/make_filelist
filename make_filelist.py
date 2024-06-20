import os
import argparse
import fnmatch


def create_file_list(directory, output_file, file_filter=None):
    file_list = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file_filter and not fnmatch.fnmatch(file, file_filter):
                continue
            file_list.append(os.path.join(root, file))

        # for file in files:
        #     if name_filter and name_filter not in file:
        #         continue
        #     if extension_filter and not file.endswith(extension_filter):
        #         continue
        #     file_list.append(os.path.join(root, file))

    with open(output_file, "w") as f:
        for file in file_list:
            f.write(file + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a file list from a directory with optional filters.")
    parser.add_argument("directory", type=str, help="The directory to search for files")
    parser.add_argument("output_file", type=str, help="The output file to write the file list to")
    parser.add_argument(
        "--filter",
        type=str,
        help='Optional filter to include only files matching this pattern (e.g., "*.tcl", "example*.exe")',
    )
    # parser.add_argument(
    #     "--name_filter", type=str, help="Optional filter to include only files that contain this string in their name"
    # )
    # parser.add_argument(
    #     "--extension_filter", type=str, help="Optional filter to include only files with this extension"
    # )
    args = parser.parse_args()
    create_file_list(args.directory, args.output_file, args.filter)
    print(f"File list has been saved to {args.output_file}")
