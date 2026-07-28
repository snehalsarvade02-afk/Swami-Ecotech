import glob
import os

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"
html_files = glob.glob(os.path.join(directory, "*.html"))

count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "ph-leaf preloader-icon" in content:
        content = content.replace("ph-leaf preloader-icon", "ph-recycle preloader-icon")
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files to use ph-recycle in the preloader.")
