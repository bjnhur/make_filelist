# Make File List Script

This project provides a Python script to generate a list of files from a specified directory. The script can filter files based on a given pattern, such as file name or extension.

## Prerequisites

Before you begin, ensure you have the following installed on your machine:
- Python 3.x

## Installation

1. **Clone the repository or download the script files.**

2. **Install required Python libraries:**
   ```sh
   pip install argparse fnmatch
   ```

## Usage

### Generating a File List

Use the following command to generate a file list from a specified directory:

```sh
python make_filelist.py /path/to/directory filelist.f
```

This command will search the specified directory and save the list of all files to `filelist.f`.

### Filtering by Pattern

To include only files that match a specific pattern, use the `--filter` option. The pattern can include wildcards such as `*` and `?`.

#### Examples

1. **폴더 내 모든 파일 리스트 저장 (재귀적 검색)**:
   ```sh
   python create_file_list.py /path/to/directory filelist.f -r
   ```

2. **폴더 내 특정 확장자의 파일만 필터링 (재귀적 검색)**:
   ```sh
   python create_file_list.py /path/to/directory filelist.f --filter "*.tcl" -r
   ```

3. **폴더 내 특정 이름 패턴의 파일만 필터링 (재귀적 검색)**:
   ```sh
   python create_file_list.py /path/to/directory filelist.f --filter "example*.exe" -r
   ```

4. **폴더 내 모든 파일 리스트 저장 (비재귀적 검색)**:
   ```sh
   python create_file_list.py /path/to/directory filelist.f
   ```

`-r` 옵션을 사용하여 디렉토리를 재귀적으로 검색하도록 할 수 있습니다. 이 옵션을 사용하지 않으면, 스크립트는 기본적으로 현재 디렉토리에서만 파일을 검색합니다.

### Output

The script will generate a file list and save it to the specified output file. Each line in the output file represents the path to a file that matches the given criteria.

### Error Handling

If the specified directory does not exist or is not accessible, the script will print an error message and exit.

## Example Directory Structure

```
project/
│
├── make_filelist.py
├── filelist.f
└── example_directory/
    ├── example1.tcl
    ├── example2.tcl
    └── txt_example1.txt
```

## Contributing

If you would like to contribute to this project, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, feel free to contact [your contact information].
