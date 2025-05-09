document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".order-btn").forEach(button => {
        button.addEventListener("click", function () {
            alert("Your order has been placed!");
        });
    });

    // Highlight top products when hovered
    document.querySelectorAll(".product-card").forEach(card => {
        card.addEventListener("mouseenter", function () {
            this.style.transform = "scale(1.05)";
        });
        card.addEventListener("mouseleave", function () {
            this.style.transform = "scale(1)";
        });
    });
});
