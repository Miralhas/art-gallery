document.addEventListener("DOMContentLoaded", () => {
    const profileSection = document.querySelector("#profile-section");
    const informationSection = document.querySelector("#information-section");
    const commentSection = document.querySelector("#comment-section");
    const chartSection = document.querySelector("#chart-section");

    const analyticsBtn = document.querySelector("#analytics-btn");
    const closeChartBtn = document.getElementById("close-chart-btn");
    const refreshChartBtn = document.getElementById("refresh-chart-btn");

    refreshChartBtn.addEventListener("click", getArtworkChart);

    analyticsBtn.addEventListener("click", () => {
        getArtworkChart();
        chartSection.style.display = "block";
        profileSection.style.display = "none";
        commentSection.style.display = "none";
        informationSection.style.display = "none";
    })

    closeChartBtn.addEventListener("click", () => {
        chartSection.style.display = "none";
        profileSection.style.display = "block";
        commentSection.style.display = "block";
        informationSection.style.display = "block";
    })
})

function getArtworkChart() {
    fetch(artworkUrl)
    .then(response => response.json())
    .then(data => {
        let chartStatus = Chart.getChart("artworkChart");
        if (chartStatus != undefined) {
            chartStatus.destroy();
        }
        const ctx = document.querySelector("#artworkChart").getContext("2d");
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