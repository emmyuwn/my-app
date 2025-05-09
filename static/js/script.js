    // Example JavaScript Functionality
    function showAlert() {
        alert("Thank you for ordering with FoodStore!");
    }

    document.addEventListener('DOMContentLoaded', () => {
        console.log('FoodStore platform loaded successfully!');
        // Dynamic behavior for food items can be added here
    });

    document.addEventListener("DOMContentLoaded", function () {
        const products = document.querySelectorAll(".product");
    
        products.forEach(product => {
            product.addEventListener("click", function () {
                this.classList.toggle("expanded"); // Toggle class on click
            });
        });
    });

    
    //contact   
    document.addEventListener("DOMContentLoaded", function () {
        const contactForm = document.getElementById("contactForm");
        const formMessage = document.getElementById("formMessage");
    
        contactForm.addEventListener("submit", function (event) {
            event.preventDefault(); // Prevent default form submission
    
            // Simple validation
            let name = document.getElementById("name").value.trim();
            let email = document.getElementById("email").value.trim();
            let message = document.getElementById("message").value.trim();
    
            if (name === "" || email === "" || message === "") {
                formMessage.textContent = "Please fill in all fields.";
                formMessage.classList.add("error");
                formMessage.classList.remove("hidden");
                return;
            }
    
            // Simulate success
            formMessage.textContent = "Thank you! We'll get back to you soon.";
            formMessage.classList.add("success");
            formMessage.classList.remove("hidden");
    
            // Reset form fields after submission
            contactForm.reset();
        });
    });
    