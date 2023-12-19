document.addEventListener("DOMContentLoaded", () => {

    const editArtworkBtn = document.querySelector("#editArtworkBtn");

    if (editArtworkBtn) {
        editArtworkBtn.addEventListener("click", function() {
            this.style.display = "none";
            const artworkDescriptionParagraph = document.querySelector(".artwork-description");
            const artworkDescription = artworkDescriptionParagraph.innerHTML;
            
            const artworkTitleHeader = document.querySelector(".artwork-title");
            const artworkTitle = artworkTitleHeader.innerHTML;

            const submitEditDiv = document.querySelector("#submitEditDiv");

            const newArtworkTitleInput = document.createElement("input")
            newArtworkTitleInput.setAttribute("type", "text");
            newArtworkTitleInput.classList.add("form-control");
            newArtworkTitleInput.value = artworkTitle;
            
            const newDescriptionTextarea = document.createElement("textarea");
            newDescriptionTextarea.classList.add("form-control");
            newDescriptionTextarea.value = artworkDescription;
            newDescriptionTextarea.rows = 5;

            artworkTitleHeader.innerHTML = "";
            artworkTitleHeader.append(newArtworkTitleInput);
            
            artworkDescriptionParagraph.innerHTML = "";
            artworkDescriptionParagraph.append(newDescriptionTextarea);
            
            const submitEditBtn = document.createElement("button");
            submitEditBtn.classList.add("btn", "outline-btn", "btn-sm", "mb-3");
            submitEditBtn.innerHTML = "Edit artwork";

            const closeEditBtn = document.createElement("button");
            closeEditBtn.classList.add("btn", "outline-btn", "btn-sm", "ms-3");
            closeEditBtn.innerHTML = "Close";

            const btnDiv = document.createElement("div");
            btnDiv.classList.add("d-flex", "justify-content-start", "align-items-start");

            btnDiv.append(submitEditBtn);
            btnDiv.append(closeEditBtn);

            submitEditDiv.append(btnDiv);

            closeEditBtn.addEventListener("click", function() {
                btnDiv.remove();
                artworkTitleHeader.innerHTML = artworkTitle;
                artworkDescriptionParagraph.innerHTML = artworkDescription;
                editArtworkBtn.style.display = "block";
            })

            submitEditBtn.addEventListener("click", function() {
                const csrfToken = document.querySelector("[name='csrfmiddlewaretoken']").value;
                fetch(`/api/edit-artworks/${slug}`, {
                    method: "PUT",
                    headers: {
                        "X-CSRFToken": csrfToken,
                        "Content-Type": "application/json"
                    },
                    credentials: "same-origin",
                    body: JSON.stringify({
                        newArtworkTitle: newArtworkTitleInput.value,
                        newArtworkDescription: newDescriptionTextarea.value,
                        artworkSlug: slug,
                        artworkOwner: artworkOwner,
                        path: path
                    })
                })
                .then(response => response.json())
                .then(data => {
                    console.log(data.message)
                    if (data.message === "Ok") {
                        let stateObj = { additionalInformation: 'Slug Change' };
                        window.history.replaceState(stateObj, "", data.newUrl);
                        artworkTitleHeader.innerHTML = newArtworkTitleInput.value;
                        artworkDescriptionParagraph.innerHTML = newDescriptionTextarea.value;
                        slug = data.newSlug;
                        this.remove();
                        editArtworkBtn.style.display = "block";
                    }
                })
            })
        })
    }
})