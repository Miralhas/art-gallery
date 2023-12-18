document.addEventListener("DOMContentLoaded", () => {
    const errorMessage = document.querySelector("#error-message");
    
    if (document.querySelector("#review-form")){
        document.querySelector("#review-form").addEventListener("submit", function(event){
            if (document.querySelector("#starValue").value === ""){
                event.preventDefault();
                errorMessage.style.display = "block";
            } else {
                errorMessage.style.display = "none";
            }
        })
    }

    const starWrapper = document.querySelector(".stars");
    const stars = document.querySelectorAll(".stars i");

    stars.forEach((star, clickedIdx) => {
        star.addEventListener('click', function () {
            starWrapper.classList.add("disabled")
            stars.forEach((otherStar, otherIdx) => {
                if (otherIdx <= clickedIdx) {
                    otherStar.classList.add("active");
                }
            })

            document.getElementById('starValue').value = clickedIdx + 1;
            
            if (errorMessage.style.display === 'block'){
                errorMessage.style.display = 'none'
            }

            console.log(`star of index ${clickedIdx} was clicked`)
        })
    })
})