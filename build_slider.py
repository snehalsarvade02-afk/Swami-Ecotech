import re
import os

html_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\index.html"
css_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\css\styles.css"
js_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\js\main.js"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

old_hero_regex = r'<!-- Stunning Full Screen Hero Section -->.*?</section>'
new_hero = """<!-- Stunning Full Screen Hero Slider Section -->
    <section class="hero-slider-container">
        
        <div class="hero-slide active" style="background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), url('assets/images/hero.png');">
            <div class="container hero-slide-content">
                <div class="badge hero-badge">Pioneering India's Circular Economy</div>
                <h1 class="hero-title">Transforming E-Waste into <br><span style="color: var(--primary);">Eco-Wealth</span></h1>
                <p class="hero-description">We provide comprehensive, secure, and environmentally responsible IT asset disposal and data destruction solutions for modern enterprises.</p>
                <div class="hero-buttons-flex">
                    <a href="contact.html" class="btn-primary hero-btn">Schedule a Pickup <i class="ph ph-arrow-right"></i></a>
                    <a href="solutions.html" class="btn-primary hero-btn-alt">Explore Corporate Solutions</a>
                </div>
            </div>
        </div>
        
        <div class="hero-slide" style="background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), url('assets/images/hero2.png');">
            <div class="container hero-slide-content">
                <div class="badge hero-badge">Zero Landfill Guarantee</div>
                <h1 class="hero-title">Advanced Recycling for a <br><span style="color: var(--primary);">Sustainable Future</span></h1>
                <p class="hero-description">We recover precious resources with state-of-the-art robotic sorting, maximizing your ROI while protecting the planet.</p>
                <div class="hero-buttons-flex">
                    <a href="process.html" class="btn-primary hero-btn">See Our Process <i class="ph ph-arrow-right"></i></a>
                    <a href="contact.html" class="btn-primary hero-btn-alt">Request Audit</a>
                </div>
            </div>
        </div>
        
        <div class="hero-slide" style="background-image: linear-gradient(rgba(15, 23, 42, 0.8), rgba(15, 23, 42, 0.8)), url('assets/images/hero3.png');">
            <div class="container hero-slide-content">
                <div class="badge hero-badge">100% Certified Destruction</div>
                <h1 class="hero-title">Military-Grade <br><span style="color: var(--primary);">Data Security</span></h1>
                <p class="hero-description">Your data security is our highest priority. We use internationally certified logical wiping and physical shredders.</p>
                <div class="hero-buttons-flex">
                    <a href="solution-sanitization.html" class="btn-primary hero-btn">View Security Solutions <i class="ph ph-arrow-right"></i></a>
                    <a href="contact.html" class="btn-primary hero-btn-alt">Contact Us</a>
                </div>
            </div>
        </div>
        
    </section>"""

html_content = re.sub(old_hero_regex, new_hero, html_content, flags=re.DOTALL)
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)


new_css = """
/* ==========================================================================
   Hero Slider Styles
   ========================================================================== */
.hero-slider-container {
    position: relative;
    width: 100%;
    height: 100vh;
    min-height: 700px;
    overflow: hidden;
    display: flex;
    align-items: center;
    justify-content: center;
}

.hero-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    opacity: 0;
    transition: opacity 1.5s ease-in-out;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
}

.hero-slide.active {
    opacity: 1;
    z-index: 2;
}

.hero-slide-content {
    position: relative;
    z-index: 10;
    text-align: center;
    width: 100%;
}

.hero-badge {
    background: rgba(255,255,255,0.1); 
    color: white; 
    border: 1px solid rgba(255,255,255,0.2); 
    margin-bottom: 2rem;
}

.hero-buttons-flex {
    display: flex; 
    gap: 1rem; 
    justify-content: center; 
    flex-wrap: wrap;
}

.hero-btn {
    font-size: 1.1rem; 
    padding: 1rem 2rem;
}

.hero-btn-alt {
    font-size: 1.1rem; 
    padding: 1rem 2rem; 
    background: white; 
    color: var(--bg-dark);
}
.hero-btn-alt:hover {
    background: #f0f0f0;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(new_css)

new_js = """
    // 5. Hero Slider Logic
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 5000);
    }
"""

with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

if "Hero Slider Logic" not in js_content:
    js_content = js_content.replace('// Preloader Logic', new_js + '\n// Preloader Logic')
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)

print("Build complete.")
