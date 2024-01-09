def read_file(HumptyDumpty):
    try:
        with open(HumptyDumpty, 'r') as file:
            content = file.read(HumptyDumpty)
            return content
    except FileNotFoundError:
        return f"Tập tin '{HumptyDumpty}' không tồn tại."
    except Exception as e:
        return f"Có lỗi xảy ra: {e}"

# Nhập tên tập tin từ người dùng
file_path = input("Nhập tên tập tin cần đọc: ")

# Gọi hàm để đọc nội dung của tập tin
file_content = read_file(file_path)

# In nội dung của tập tin (hoặc thông báo lỗi)
print(file_content)

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

# Sử dụng phương thức
file_path = 'D:\THỰC HÀNH KHCS\BÀI TẬP\Chương 13\HumptyDumpty.txt'  
result = read_report_file(file_path)

if 'error' in result:
    print(f"Error: {result['error']}")
else:
    print(f"Content:\n{result['content']}")
    print(f"Number of lines: {result['line_count']}")
    print(f"Number of words: {result['word_count']}")
    print(f"Number of characters: {result['character_count']}")
