import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
import sys

root=tk.Tk()
root.withdraw()

selected_dir = filedialog.askdirectory(title="選擇你想要整理的資料夾位置")

if not selected_dir:
    messagebox.showinfo("提示", "未選擇資料夾，程式將退出。")
    sys.exit()

current_script_name = os.path.basename(__file__)
current_script_path = os.path.abspath(__file__)

print(f"選擇的資料夾位置: {selected_dir}")

counter = 0

for filename in os.listdir(selected_dir):
    file_path = os.path.join(selected_dir, filename)
    
    if os.path.isfile(file_path) and filename != current_script_name:
        file_extension = os.path.splitext(filename)[1][1:] 
        if not file_extension: 
            file_extension = "no_extension"
        
        target_dir = os.path.join(selected_dir, file_extension)
        
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        
        shutil.move(file_path, os.path.join(target_dir, filename))
        counter += 1

print(f"共整理了 {counter} 個檔案。")

messagebox.showinfo("整理完成", f"成功整理資料夾：\n{selected_dir}\n\n共自動分類了 {counter} 個檔案！")