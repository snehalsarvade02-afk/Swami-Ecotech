import glob
import os

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"
html_files = glob.glob(os.path.join(directory, "*.html"))

old_desc = "Swami Ecotech - Your trusted partner in electronic waste management, ITAD, and sustainable recycling solutions in India."
new_desc = "Swami Ecotech is India's premium e-waste recycling partner. We provide secure ITAD, data destruction, and sustainable electronic waste management solutions."

count = 0
for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if old_desc in content:
        content = content.replace(old_desc, new_desc)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Updated meta description in {count} HTML files.")
