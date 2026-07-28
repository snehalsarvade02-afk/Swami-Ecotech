import glob
import os

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"
html_files = glob.glob(os.path.join(directory, "*.html"))

# 1. Inject missing Open Graph tags in all HTML files
og_tags_to_add = """    <meta property="og:site_name" content="Swami Ecotech">
    <meta property="og:locale" content="en_IN">
"""

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    if "og:site_name" not in content:
        # Insert after <meta property="og:type" content="website">
        if '<meta property="og:type" content="website">' in content:
            content = content.replace(
                '<meta property="og:type" content="website">',
                '<meta property="og:type" content="website">\n' + og_tags_to_add
            )
        else:
            # Fallback: just insert before </head>
            content = content.replace('</head>', og_tags_to_add + '</head>')
            
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

# 2. Inject Schema.org data in index.html
schema_data = """
    <!-- Schema.org JSON-LD -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "LocalBusiness",
      "name": "Swami Ecotech",
      "image": "https://www.swamiecotech.com/assets/images/og-image.jpg",
      "@id": "https://www.swamiecotech.com/",
      "url": "https://www.swamiecotech.com/",
      "telephone": "",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "",
        "addressLocality": "",
        "postalCode": "",
        "addressCountry": "IN"
      }
    }
    </script>
"""

index_path = os.path.join(directory, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

if "application/ld+json" not in index_content:
    index_content = index_content.replace('</head>', schema_data + '</head>')
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)

print("Successfully injected missing Open Graph tags and Schema.org data.")
