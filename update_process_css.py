import os

css_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\css\styles.css"

new_css = """
/* ==========================================================================
   Process Grid Styles (Redesign)
   ========================================================================== */
.process-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 2rem;
    margin-top: 3rem;
}

.process-card {
    background: var(--bg-white);
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    transition: var(--transition);
    display: flex;
    flex-direction: column;
    height: 100%;
}

.process-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 35px rgba(0,0,0,0.1);
}

.process-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-bottom: 4px solid var(--primary);
}

.process-content {
    padding: 1.5rem;
    flex-grow: 1;
}

.process-content h3 {
    font-size: 1.25rem;
    margin-bottom: 1rem;
    color: var(--secondary);
}

.process-content p {
    color: var(--text-muted);
    font-size: 0.95rem;
}
"""

with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

if ".process-card {" not in css_content:
    # Insert before responsive media queries
    marker = "/* ==========================================================================\n   Responsive Media Queries"
    if marker in css_content:
        css_content = css_content.replace(marker, new_css + "\n" + marker)
    else:
        css_content += "\n" + new_css
        
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    print("Added process grid CSS.")
else:
    print("CSS already present.")
