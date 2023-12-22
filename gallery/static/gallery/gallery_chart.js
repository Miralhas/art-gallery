document.addEventListener("DOMContentLoaded", () => {
    const profileSection = document.querySelector("#profile-section");
    const informationSection = document.querySelector("#information-section");
    const artworksSection = document.querySelector("#artworks-section");
    const chartSection = document.querySelector("#chart-section");

    const analyticsBtn = document.querySelector("#analytics-btn");
    const closeChartBtn = document.getElementById("close-chart-btn");

    analyticsBtn.addEventListener("click", () => {
        getGalleryChart();
        chartSection.style.display = "block";
        profileSection.style.display = "none";
        artworksSection.style.display = "none";
        informationSection.style.display = "none";
    })

    closeChartBtn.addEventListener("click", () => {
        chartSection.style.display = "none";
        profileSection.style.display = "block";
        artworksSection.style.display = "block";
        informationSection.style.display = "block";
    })

})

function getGalleryChart() {
    fetch(galleryUrl)
    .then(response => response.json())
    .then(data => {
        let chartStatus = Chart.getChart("galleryChart");
        if (chartStatus != undefined) {
            chartStatus.destroy();
        }
        const ctx = document.querySelector("#galleryChart").getContext("2d");
        new Chart(ctx, {
            type: 'bar',
            data: data,
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    });
}