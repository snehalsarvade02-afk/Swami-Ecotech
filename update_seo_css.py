import os
import glob
import re

directory = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web"

# --- CSS Mobile Responsiveness Update ---
css_file = os.path.join(directory, "css", "styles.css")
media_queries = """
/* ==========================================================================
   Responsive Media Queries
   ========================================================================== */

@media (max-width: 991px) {
    /* Navigation */
    .nav-links { display: none; }
    .mobile-menu-btn { display: block; }
    
    /* Grids & Layouts */
    .waste-grid, .services-grid, .features-grid, .stats-grid, .process-grid {
        grid-template-columns: 1fr;
    }
    
    .zigzag-container, .contact-container, .about-container, .solution-container {
        flex-direction: column !important;
        grid-template-columns: 1fr !important;
    }
    
    /* Make zigzag-reverse stack correctly on mobile */
    .zigzag-reverse .zigzag-container {
        flex-direction: column !important;
    }

    /* Typography & Spacing */
    .hero-title, h1 { font-size: 2.5rem !important; }
    .section-title, h2 { font-size: 2rem !important; }
    .section { padding: 4rem 0; }
    .hero { padding: 8rem 1rem 3rem; }
    .footer-grid { grid-template-columns: 1fr; }
}

@media (max-width: 768px) {
    .container { padding: 0 1.5rem; }
    .hero-title, h1 { font-size: 2rem !important; }
    .section-title, h2 { font-size: 1.75rem !important; }
}
"""

with open(css_file, "r", encoding="utf-8") as f:
    css_content = f.read()

if "Responsive Media Queries" not in css_content:
    with open(css_file, "a", encoding="utf-8") as f:
        f.write(media_queries)
    print("Added responsive media queries to styles.css")
else:
    print("Media queries already present in styles.css")

# --- HTML SEO Injection ---
html_files = glob.glob(os.path.join(directory, "*.html"))

seo_keywords = "e-waste recycling, electronic waste management, ITAD, data destruction, Swami Ecotech, India e-waste"
domain = "https://www.swamiecotech.com"
og_image = "https://www.swamiecotech.com/assets/images/og-image.jpg"

updated_files_count = 0

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract title
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1).strip() if title_match else "Swami Ecotech"
    title = title.replace('"', '&quot;')
    
    # Extract description
    desc_match = re.search(r'<meta\s+name="description"\s+content="(.*?)"', content, re.IGNORECASE | re.DOTALL)
    description = desc_match.group(1).strip() if desc_match else "Swami Ecotech - Your trusted partner in electronic waste management."
    description = description.replace('"', '&quot;')
    
    filename = os.path.basename(file_path)
    url = f"{domain}/{filename}" if filename != "index.html" else f"{domain}/"
    
    # Tags to append
    tags_to_add = "\n    <!-- SEO and Social Meta Tags -->\n"
    if 'name="keywords"' not in content:
        tags_to_add += f'    <meta name="keywords" content="{seo_keywords}">\n'
    if 'name="robots"' not in content:
        tags_to_add += '    <meta name="robots" content="index, follow">\n'
    if 'property="og:title"' not in content:
        tags_to_add += f'    <meta property="og:title" content="{title}">\n'
        tags_to_add += f'    <meta property="og:description" content="{description}">\n'
        tags_to_add += '    <meta property="og:type" content="website">\n'
        tags_to_add += f'    <meta property="og:url" content="{url}">\n'
        tags_to_add += f'    <meta property="og:image" content="{og_image}">\n'
    if 'name="twitter:card"' not in content:
        tags_to_add += '    <meta name="twitter:card" content="summary_large_image">\n'
        tags_to_add += f'    <meta name="twitter:title" content="{title}">\n'
        tags_to_add += f'    <meta name="twitter:description" content="{description}">\n'
        tags_to_add += f'    <meta name="twitter:image" content="{og_image}">\n'
    if 'rel="canonical"' not in content:
        tags_to_add += f'    <link rel="canonical" href="{url}">\n'
        
    if "<!-- SEO and Social Meta Tags -->" not in content and 'name="robots"' not in content:
        content = content.replace("</head>", f"{tags_to_add}</head>")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        updated_files_count += 1

print(f"Added SEO tags to {updated_files_count} HTML files.")
