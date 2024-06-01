import markdown
import sys


def validate_args():
    num_args = len(sys.argv)
    command = sys.argv[1]

    if num_args < 4:
        print('Not enough arguments')
        sys.exit(1)
    if command != 'markdown':
        print('Invalid command')
        sys.exit(1)
    if num_args != 4:
        print('Wrong markdown method usage!')
        print('Usage: file-converter.py markdown inputfile outputfile')
        sys.exit(1)


def main():
    validate_args()

    input_file_path = sys.argv[2]
    output_file_path = sys.argv[3]

    with open(input_file_path, 'r', encoding="utf-8") as f:
        markdown_file = f.read()

    # Markdownの拡張機能を使用してテーブルのサポートを有効にする
    converted_file = markdown.markdown(markdown_file, extensions=['extra'])
    with open(output_file_path, 'w', encoding="utf-8") as f:
        f.write(converted_file)


if __name__ == "__main__":
    main()