document.addEventListener("DOMContentLoaded", () => {

    const editGalleryBtn = document.querySelector("#editGalleryBtn");

    if (editGalleryBtn) {
        editGalleryBtn.addEventListener("click", function() {
            this.style.display = "none";
            const galleryDescriptionParagraph = document.querySelector(".gallery-description");
            const galleryDescription = galleryDescriptionParagraph.innerHTML;
            
            const galleryNameHeader = document.querySelector(".gallery-name");
            const galleryName = galleryNameHeader.innerHTML;

            const editGalleryDiv = document.querySelector("#editGalleryDiv");

            const newGalleryNameInput = document.createElement("input")
            newGalleryNameInput.setAttribute("type", "text");
            newGalleryNameInput.classList.add("form-control");
            newGalleryNameInput.value = galleryName;
            
            const newDescriptionTextarea = document.createElement("textarea");
            newDescriptionTextarea.classList.add("form-control");
            newDescriptionTextarea.value = galleryDescription;
            newDescriptionTextarea.rows = 5;

            galleryNameHeader.innerHTML = "";
            galleryNameHeader.append(newGalleryNameInput);
            
            galleryDescriptionParagraph.innerHTML = "";
            galleryDescriptionParagraph.append(newDescriptionTextarea);
            
            const submitEditBtn = document.createElement("button");
            submitEditBtn.classList.add("btn", "outline-btn", "btn-sm", "mb-3");
            submitEditBtn.innerHTML = "Save";

            editGalleryDiv.append(submitEditBtn);
            
            // const closeEditBtn = document.createElement("button");
            // submitEditBtn.classList.add("btn", "outline-btn", "btn-sm", "ms-3");
            // submitEditBtn.innerHTML = "Close";

            // editGalleryDiv.append(closeEditBtn);

            submitEditBtn.addEventListener("click", function() {
                const csrfToken = document.querySelector("[name='csrfmiddlewaretoken']").value;
                fetch(`/api/edit-galleries/${slug}`, {
                    method: "PUT",
                    headers: {
                        "X-CSRFToken": csrfToken,
                        "Content-Type": "application/json"
                    },
                    credentials: "same-origin",
                    body: JSON.stringify({
                        newGalleryName: newGalleryNameInput.value,
                        newGalleryDescription: newDescriptionTextarea.value,
                        gallerySlug: slug,
                        galleryOwner: galleryOwner,
                        path: path
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message)
                    if (data.message === "Ok") {
                        let stateObj = { additionalInformation: 'Slug Change' };
                        window.history.replaceState(stateObj, "", data.newUrl);
                        galleryNameHeader.innerHTML = newGalleryNameInput.value;
                        galleryDescriptionParagraph.innerHTML = newDescriptionTextarea.value;
                        slug = data.newSlug;
                        this.remove();
                        editGalleryBtn.style.display = "block";
                    }
                })

            })
        })
    }
})