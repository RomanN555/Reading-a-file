def full_files(file_paths, output_file):
    files_info = []

    for file_path in file_paths:
        with open(file_path, encoding='utf-8') as f:
            content = f.readlines()  
            line_count = len(content)  
            files_info.append((file_path, line_count, content))  

    files_info.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as out_file:
        for file_path, line_count, content in files_info:
            out_file.write(f"{file_path}\n{line_count}\n")  
            out_file.writelines(content) 

file_paths = ["1.txt", "2.txt", "3.txt"]
output_file = "full.txt"

full_files(file_paths, output_file)
print(f"Файлы были объединены в {output_file}")