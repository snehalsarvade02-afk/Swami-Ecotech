import re

css_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\css\styles.css"
js_path = r"c:\Users\sneha\OneDrive\Desktop\Swami Ecotech\swami-ecotech-static-web\js\main.js"

# Update CSS
with open(css_path, "r", encoding="utf-8") as f:
    css_content = f.read()

old_css_slide = """.hero-slide {
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
}"""

new_css_slide = """.hero-slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: transform 1.2s cubic-bezier(0.645, 0.045, 0.355, 1);
    transform: translateX(100%);
    z-index: 1;
}

.hero-slide.active {
    transform: translateX(0);
    z-index: 2;
}

.hero-slide.prev {
    transform: translateX(-100%);
    z-index: 1;
}

.hero-title {
    color: #ffffff !important;
    text-shadow: 0 4px 15px rgba(0,0,0,0.9);
}

.hero-description {
    color: #f1f5f9 !important;
    text-shadow: 0 2px 10px rgba(0,0,0,0.9);
    font-weight: 500;
}"""

if ".hero-slide.prev" not in css_content:
    css_content = css_content.replace(old_css_slide, new_css_slide)
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)


# Update JS
with open(js_path, "r", encoding="utf-8") as f:
    js_content = f.read()

old_js = """    // 5. Hero Slider Logic
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        setInterval(() => {
            slides[currentSlide].classList.remove('active');
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 5000);
    }"""

new_js = """    // 5. Hero Slider Logic
    const slides = document.querySelectorAll('.hero-slide');
    if (slides.length > 0) {
        let currentSlide = 0;
        
        slides.forEach((slide, index) => {
            if (index === currentSlide) {
                slide.classList.add('active');
            } else if (index === slides.length - 1) {
                slide.classList.add('prev');
            }
        });

        setInterval(() => {
            const prevSlide = document.querySelector('.hero-slide.prev');
            if (prevSlide) prevSlide.classList.remove('prev');
            
            slides[currentSlide].classList.remove('active');
            slides[currentSlide].classList.add('prev');
            
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
        }, 5000);
    }"""

if ".classList.add('prev')" not in js_content:
    js_content = js_content.replace(old_js, new_js)
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
