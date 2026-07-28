import glob
import os

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"
html_files = glob.glob(os.path.join(directory, "*.html"))

count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Look for the recycle icon we set in the previous step
    target_str = '<i class="ph-fill ph-recycle preloader-icon"></i>'
    replacement_str = '<img src="assets/images/recycle-symbol.svg" alt="Recycle Symbol" class="preloader-icon" style="width: 100px; height: auto;">'
    
    if target_str in content:
        content = content.replace(target_str, replacement_str)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1
    # Also check for leaf just in case
    elif '<i class="ph-fill ph-leaf preloader-icon"></i>' in content:
        content = content.replace('<i class="ph-fill ph-leaf preloader-icon"></i>', replacement_str)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated {count} HTML files to use the new recycle SVG image.")
