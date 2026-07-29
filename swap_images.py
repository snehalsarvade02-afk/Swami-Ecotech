import os

html_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\process.html"

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace('src="assets/images/service-pickup.png"', 'src="assets/images/process-1.png"')
content = content.replace('src="assets/images/waste-it.jpg"', 'src="assets/images/process-2.png"')
content = content.replace('src="assets/images/solution-sanitization.jpg"', 'src="assets/images/process-3.png"')
content = content.replace('src="assets/images/service-recycling.png"', 'src="assets/images/process-4.png"')
content = content.replace('src="assets/images/waste-battery.jpg"', 'src="assets/images/process-5.png"')
content = content.replace('src="assets/images/service-compliance.png"', 'src="assets/images/process-6.png"')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Swapped old images for new custom generated ones in process.html")
