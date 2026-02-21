/**
 * ==============================================================================
 * 📊 DATA SCIENCE PORTFOLIO - MAIN JAVASCRIPT
 * ==============================================================================
 */

document.addEventListener('DOMContentLoaded', function() {

    // =========================================================================
    // NAVIGATION
    // =========================================================================

    const navbar = document.getElementById('navbar');
    const navMenu = document.getElementById('nav-menu');
    const navToggle = document.getElementById('nav-toggle');

    // Mobile menu toggle
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.style.overflow = navMenu.classList.contains('active') ? 'hidden' : '';
        });

        // Close menu when clicking a link
        navMenu.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (!navMenu.contains(e.target) && !navToggle.contains(e.target)) {
                navToggle.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }

    // Navbar scroll effect
    if (navbar) {
        let lastScroll = 0;

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;

            // Add scrolled class
            if (currentScroll > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }

            lastScroll = currentScroll;
        });
    }

    // =========================================================================
    // SMOOTH SCROLL
    // =========================================================================

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            if (href === '#') return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();
                const offsetTop = target.offsetTop - 80;

                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // =========================================================================
    // SCROLL ANIMATIONS (Simple AOS Alternative)
    // =========================================================================

    const animatedElements = document.querySelectorAll('[data-aos]');

    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add delay if specified
                const delay = entry.target.getAttribute('data-aos-delay') || 0;

                setTimeout(() => {
                    entry.target.classList.add('aos-animate');
                }, delay);

                // Unobserve after animation
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => {
        observer.observe(el);
    });

    // =========================================================================
    // FLASH MESSAGES AUTO-HIDE
    // =========================================================================

    const flashMessages = document.querySelectorAll('.flash-message');

    flashMessages.forEach(message => {
        // Auto-hide after 5 seconds
        setTimeout(() => {
            message.style.animation = 'slideOut 0.3s ease forwards';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });

    // Add slideOut animation
    if (flashMessages.length > 0) {
        const style = document.createElement('style');
        style.textContent = `
            @keyframes slideOut {
                to {
                    transform: translateX(100%);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }

    // =========================================================================
    // FORM VALIDATION
    // =========================================================================

    const contactForm = document.querySelector('.contact-form');

    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;

            // Get form fields
            const name = this.querySelector('#name');
            const email = this.querySelector('#email');
            const message = this.querySelector('#message');

            // Clear previous errors
            clearErrors(this);

            // Validate name
            if (name && name.value.trim().length < 2) {
                showError(name, 'Name must be at least 2 characters');
                isValid = false;
            }

            // Validate email
            if (email && !isValidEmail(email.value)) {
                showError(email, 'Please enter a valid email');
                isValid = false;
            }

            // Validate message
            if (message && message.value.trim().length < 10) {
                showError(message, 'Message must be at least 10 characters');
                isValid = false;
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    function isValidEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }

    function showError(input, message) {
        const formGroup = input.closest('.form-group');

        // Add error styles
        input.style.borderColor = '#EF4444';

        // Create error message
        const error = document.createElement('span');
        error.className = 'form-error';
        error.textContent = message;
        error.style.cssText = `
            display: block;
            color: #EF4444;
            font-size: 0.85rem;
            margin-top: 0.5rem;
        `;

        formGroup.appendChild(error);
    }

    function clearErrors(form) {
        // Remove error messages
        form.querySelectorAll('.form-error').forEach(error => error.remove());

        // Reset input styles
        form.querySelectorAll('input, textarea').forEach(input => {
            input.style.borderColor = '';
        });
    }

    // =========================================================================
    // IMAGE ERROR HANDLING
    // =========================================================================

    document.querySelectorAll('img').forEach(img => {
        img.addEventListener('error', function() {
            // Check if there's a placeholder sibling
            const placeholder = this.nextElementSibling;
            if (placeholder && placeholder.classList.contains('project-card-placeholder')) {
                this.style.display = 'none';
                placeholder.style.display = 'flex';
            }
        });
    });

    // =========================================================================
    // PROJECTS FILTER (if on projects page)
    // =========================================================================

    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            // Update active state immediately for better UX
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
        });
    });

    // =========================================================================
    // TYPING EFFECT (Optional - for hero section)
    // =========================================================================

    const typingElement = document.querySelector('.typing-text');

    if (typingElement) {
        const texts = JSON.parse(typingElement.getAttribute('data-texts') || '[]');
        let textIndex = 0;
        let charIndex = 0;
        let isDeleting = false;

        function type() {
            const currentText = texts[textIndex];

            if (isDeleting) {
                typingElement.textContent = currentText.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typingElement.textContent = currentText.substring(0, charIndex + 1);
                charIndex++;
            }

            let typeSpeed = isDeleting ? 50 : 100;

            if (!isDeleting && charIndex === currentText.length) {
                typeSpeed = 2000; // Pause at end
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                textIndex = (textIndex + 1) % texts.length;
                typeSpeed = 500; // Pause before next word
            }

            setTimeout(type, typeSpeed);
        }

        if (texts.length > 0) {
            type();
        }
    }

    // =========================================================================
    // COUNTER ANIMATION
    // =========================================================================

    const counters = document.querySelectorAll('.stat-number');

    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counter = entry.target;
                const target = counter.textContent;

                // Extract number from text (e.g., "5+" -> 5)
                const match = target.match(/(\d+)/);
                if (match) {
                    const num = parseInt(match[1]);
                    const suffix = target.replace(/\d+/, '');

                    animateCounter(counter, num, suffix);
                }

                counterObserver.unobserve(counter);
            }
        });
    }, { threshold: 0.5 });

    counters.forEach(counter => {
        counterObserver.observe(counter);
    });

    function animateCounter(element, target, suffix) {
        let current = 0;
        const increment = target / 50;
        const duration = 1500;
        const stepTime = duration / 50;

        const timer = setInterval(() => {
            current += increment;

            if (current >= target) {
                element.textContent = target + suffix;
                clearInterval(timer);
            } else {
                element.textContent = Math.floor(current) + suffix;
            }
        }, stepTime);
    }

    // =========================================================================
    // CONSOLE MESSAGE
    // =========================================================================

    console.log(
        '%c📊 Portfolio loaded successfully!',
        'color: #4361EE; font-size: 16px; font-weight: bold;'
    );
    console.log(
        '%cBuilt with Flask & Python 🐍',
        'color: #6B7280; font-size: 12px;'
    );

});