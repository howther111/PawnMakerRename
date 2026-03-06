import os
import zipfile

# 対象フォルダ（このスクリプトと同じフォルダ）
folder = os.getcwd()

for file in os.listdir(folder):
    if file.endswith(".exe"):
        exe_path = os.path.join(folder, file)

        # zipファイル名（example.exe → example.zip）
        zip_name = os.path.splitext(file)[0] + ".zip"
        zip_path = os.path.join(folder, zip_name)

        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
            z.write(exe_path, arcname=file)

        print(f"{file} → {zip_name} を作成しました")

print("完了しました")