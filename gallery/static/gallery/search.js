document.addEventListener("DOMContentLoaded", () => {
    const galleriesFilter = document.querySelector("#galleries-filter");
    const artworksFilter = document.querySelector("#artworks-filter");
    const usersFilter = document.querySelector("#users-filter");

    const galleriesSection = document.querySelector("#galleries-section");
    const artworksSection = document.querySelector("#artworks-section");
    const usersSection = document.querySelector("#users-section");

    artworksFilter.addEventListener("click", () => {
        artworksSection.style.display = "block";
        galleriesSection.style.display = "none";
        usersSection.style.display = "none";
    })

    galleriesFilter.addEventListener("click", () => {
        galleriesSection.style.display = "block";
        artworksSection.style.display = "none";
        usersSection.style.display = "none";
    })

    usersFilter.addEventListener("click", () => {
        usersSection.style.display = "block";
        artworksSection.style.display = "none"
        galleriesSection.style.display = "none";
    })
})