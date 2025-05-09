document.addEventListener("DOMContentLoaded", function () {
    const nav = document.querySelector(".navbar");
    const menuToggle = document.querySelector(".menu-toggle");
    const navLinks = document.querySelector(".nav-links");

    // Smooth color shift on scroll
    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) {
            nav.style.background = "linear-gradient(to right, #ff6b81, #ff7f50)";
        } else {
            nav.style.background = "linear-gradient(to right, #ff7f50, #ff6b81)";
        }
    });

    // Mobile menu toggle
    menuToggle.addEventListener("click", function () {
        navLinks.classList.toggle("active");
    });
});
