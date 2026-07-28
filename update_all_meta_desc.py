import glob
import os
import re

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"
html_files = glob.glob(os.path.join(directory, "*.html"))

suffix = " We provide secure ITAD, data destruction, and sustainable electronic waste management solutions across India."

count = 0
for file_path in html_files:
    if "index.html" in file_path:
        continue # Already updated correctly

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract current meta description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE | re.DOTALL)
    if not desc_match:
        continue
    
    old_desc = desc_match.group(1).strip()
    
    if len(old_desc) < 130:
        new_desc = old_desc + suffix
        if len(new_desc) > 160:
            new_desc = new_desc[:157] + "..." # keep it under 160
            
        content = content.replace(f'content="{old_desc}"', f'content="{new_desc}"')
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        count += 1

print(f"Expanded short meta descriptions in {count} other HTML files.")
