import os

target_dir = "./test_workspace"

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

test_files = {
    "mp3": ["test1.mp3", "test2.mp3", "test3.mp3"], 
    "jpg": ["test1.jpg", "test2.jpg", "test3.jpg"],
    "png": ["test1.png", "test2.png", "test3.png"], 
    "pdf": ["test1.pdf", "test2.pdf", "test3.pdf"], 
    "zip": ["test1.zip", "test2.zip", "test3.zip"],
    "exe": ["test1.exe", "test2.exe", "test3.exe"]
}

print(f"開始創建檔案，目錄： {target_dir}")

for file_type, files in test_files.items():
    for file_name in files:
        file_path = os.path.join(target_dir, file_name)
        with open(file_path, 'w') as f:
            f.write(f"This is a test {file_type} file named {file_name}.")
        print(f"已創建檔案: {file_path}")