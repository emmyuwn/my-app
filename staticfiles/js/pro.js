document.addEventListener('DOMContentLoaded', () => {
    const containers = document.querySelectorAll('.carousel-container');

    containers.forEach(container => {
        setInterval(() => {
            container.scrollBy({
                left: 280,
                behavior: 'smooth'
            });
        }, 4000);
    });
});
