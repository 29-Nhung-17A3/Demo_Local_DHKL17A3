def read_report_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            words = content.split()
            characters = sum(len(word) for word in words)

            return {
                'content': content,
                'line_count': len(lines),
                'word_count': len(words),
                'character_count': characters
            }

    except FileNotFoundError:
        return {'error': 'File not found.'}
    except Exception as e:
        return {'error': f'Error reading file: {str(e)}'}

def main():
    try:
        file_name = input("Nhập tên tập tin: ")
        result = read_report_file(file_name)

        if 'error' in result:
            print(f"Lỗi: {result['error']}")
        else:
            print(f"Nội dung:\n{result['content']}")
            print(f"Số dòng: {result['line_count']}")
            print(f"Số từ: {result['word_count']}")
            print(f"Số kí tự: {result['character_count']}")

    except Exception as e:
        print(f"Lỗi không xác định: {e}")

if __name__ == "__main__":
    main()
