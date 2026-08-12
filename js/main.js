document.addEventListener('DOMContentLoaded', () => {
    // 1. Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileLinks = document.querySelectorAll('.mobile-link');
    
    let isMenuOpen = false;

    function toggleMenu() {
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            mobileMenu.classList.add('active');
            mobileMenuBtn.innerHTML = '<i class="ph ph-x"></i>';
        } else {
            mobileMenu.classList.remove('active');
            mobileMenuBtn.innerHTML = '<i class="ph ph-list"></i>';
        }
    }

    mobileMenuBtn.addEventListener('click', toggleMenu);

    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (isMenuOpen) toggleMenu();
        });
    });

    // 2. Sticky Navbar & Scroll Effects
    const navbar = document.getElementById('navbar');
    
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // 3. Number Counter Animation for Impact Section
    const counters = document.querySelectorAll('.counter');
    const speed = 200; // The lower the slower

    const animateCounters = () => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText.replace(/,/g, '');
                
                // Lower inc to slow and higher to fast
                const inc = target / speed;

                if (count < target) {
                    counter.innerText = Math.ceil(count + inc).toLocaleString();
                    setTimeout(updateCount, 15);
                } else {
                    counter.innerText = target.toLocaleString() + (target > 1000 ? '+' : '');
                }
            };
            updateCount();
        });
    }

    // Use Intersection Observer to trigger counter animation when visible
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    let animationTriggered = false;

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !animationTriggered) {
                animateCounters();
                animationTriggered = true;
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const statsContainer = document.getElementById('stats-container');
    if (statsContainer) {
        observer.observe(statsContainer);
    }

});


    // 5. Hero Slider Logic
    const slides = document.querySelectorAll('.hero-slide');
    const indicators = document.querySelectorAll('.indicator');
    if (slides.length > 0) {
        let currentSlide = 0;
        let slideInterval;
        
        const initSlides = () => {
            slides.forEach((slide, index) => {
                slide.classList.remove('active', 'prev');
                if (indicators[index]) indicators[index].classList.remove('active');
                
                if (index === currentSlide) {
                    slide.classList.add('active');
                    if (indicators[index]) indicators[index].classList.add('active');
                } else if (index === (currentSlide === 0 ? slides.length - 1 : currentSlide - 1)) {
                    slide.classList.add('prev');
                }
            });
        };
        
        initSlides();

        const goToNextSlide = () => {
            const prevSlide = document.querySelector('.hero-slide.prev');
            if (prevSlide) prevSlide.classList.remove('prev');
            
            slides[currentSlide].classList.remove('active');
            slides[currentSlide].classList.add('prev');
            if (indicators[currentSlide]) indicators[currentSlide].classList.remove('active');
            
            currentSlide = (currentSlide + 1) % slides.length;
            slides[currentSlide].classList.add('active');
            if (indicators[currentSlide]) indicators[currentSlide].classList.add('active');
        };

        const goToSlide = (index) => {
            if (index === currentSlide) return;
            
            const prevSlide = document.querySelector('.hero-slide.prev');
            if (prevSlide) prevSlide.classList.remove('prev');
            
            slides[currentSlide].classList.remove('active');
            slides[currentSlide].classList.add('prev');
            if (indicators[currentSlide]) indicators[currentSlide].classList.remove('active');
            
            currentSlide = index;
            slides[currentSlide].classList.add('active');
            if (indicators[currentSlide]) indicators[currentSlide].classList.add('active');
            
            resetInterval();
        };

        const startInterval = () => {
            slideInterval = setInterval(goToNextSlide, 8000); // Increased time from 5000ms to 8000ms
        };

        const resetInterval = () => {
            clearInterval(slideInterval);
            startInterval();
        };

        startInterval();
        
        indicators.forEach((indicator, index) => {
            indicator.addEventListener('click', () => {
                goToSlide(index);
            });
        });

        const prevArrow = document.querySelector('.prev-arrow');
        const nextArrow = document.querySelector('.next-arrow');

        if (prevArrow) {
            prevArrow.addEventListener('click', () => {
                const prevIndex = (currentSlide - 1 + slides.length) % slides.length;
                goToSlide(prevIndex);
            });
        }

        if (nextArrow) {
            nextArrow.addEventListener('click', () => {
                goToNextSlide();
                resetInterval();
            });
        }
    }

// Preloader Logic
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        // Add a slight delay so the user actually sees the beautiful animation for a moment
        setTimeout(() => {
            preloader.classList.add('fade-out');
            setTimeout(() => {
                preloader.style.display = 'none';
            }, 500); // Matches the CSS transition time
        }, 800);
    }
});

// Process Carousel Logic
document.addEventListener('DOMContentLoaded', () => {
    const track = document.getElementById('process-carousel-track');
    const nextBtn = document.getElementById('process-next');
    const prevBtn = document.getElementById('process-prev');
    
    if (track && nextBtn && prevBtn) {
        let currentIndex = 0;
        const totalCards = 6;
        
        const updateCarousel = () => {
            let cardsPerView = 1;
            
            const maxIndex = Math.max(0, totalCards - cardsPerView);
            if (currentIndex > maxIndex) currentIndex = maxIndex;
            
            // Calculate percentage to translate. 
            // Gap is 2rem. To perfectly snap we can use offsetWidth.
            // But since cards are roughly flex 1, translation by 100% / cardsPerView * index works approximately if gap is handled.
            // A more robust way is querying card width:
            const card = track.querySelector('.carousel-card');
            if (card) {
                const cardWidth = card.offsetWidth;
                const gap = 32; // 2rem = 32px
                const slideAmount = (cardWidth + gap) * currentIndex;
                track.style.transform = `translateX(-${slideAmount}px)`;
            }
            
            // Update button states
            prevBtn.style.opacity = currentIndex === 0 ? '0.5' : '1';
            prevBtn.style.pointerEvents = currentIndex === 0 ? 'none' : 'auto';
            
            nextBtn.style.opacity = currentIndex === maxIndex ? '0.5' : '1';
            nextBtn.style.pointerEvents = currentIndex === maxIndex ? 'none' : 'auto';
        };
        
        nextBtn.addEventListener('click', () => {
            let cardsPerView = 1;
            
            const maxIndex = Math.max(0, totalCards - cardsPerView);
            if (currentIndex < maxIndex) {
                currentIndex++;
                updateCarousel();
            }
        });
        
        prevBtn.addEventListener('click', () => {
            if (currentIndex > 0) {
                currentIndex--;
                updateCarousel();
            }
        });
        
        window.addEventListener('resize', updateCarousel);
        // Initialize
        setTimeout(updateCarousel, 100);
    }
});
