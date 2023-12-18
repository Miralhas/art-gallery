document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#start-btn").addEventListener("click", () => {
        const infoSection = document.querySelector(".information-section");
        const formSection = document.querySelector(".form-section");
        infoSection.classList.add("fade-out");
        infoSection.addEventListener('animationend', () => {
            infoSection.style.display = 'none';
            formSection.classList.remove("d-none");
            formSection.classList.add("fade-in");
        });
    })
})