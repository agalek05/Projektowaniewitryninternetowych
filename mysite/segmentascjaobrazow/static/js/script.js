document.addEventListener('DOMContentLoaded', () => {
    const hamburgerBtn = document.getElementById('hamburger-btn');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // 1. Obsługa otwierania i zamykania menu mobilnego
    if (hamburgerBtn && navMenu) {
        hamburgerBtn.addEventListener('click', () => {
            const isExpanded = hamburgerBtn.getAttribute('aria-expanded') === 'true';

            // Przełączanie klas i atrybutów dostępności (WCAG)
            hamburgerBtn.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('active');

            // Animacja ikony hamburgera (opcjonalna)
            hamburgerBtn.classList.toggle('open');
        });
    }

    // 2. Automatyczne zamykanie menu mobilnego po kliknięciu w link nawigacyjny
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (navMenu && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                hamburgerBtn.setAttribute('aria-expanded', 'false');
                hamburgerBtn.classList.remove('open');
            }
        });
    });
});
