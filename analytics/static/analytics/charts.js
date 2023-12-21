document.addEventListener("DOMContentLoaded", ()=> {
    window.onload = () => {
        getAnalyticsChart(galleriesUrl);
    }

    const galleriesChart = document.querySelector("#galleries-chart");
    galleriesChart.addEventListener("click", () => {
        getAnalyticsChart(galleriesUrl);
    });

    const artworksChart = document.querySelector("#artworks-chart");
    artworksChart.addEventListener("click", () => {
        getAnalyticsChart(artworksUrl);
    })

    const usersChart = document.querySelector("#users-chart");
    usersChart.addEventListener("click", () => {
        getAnalyticsChart(usersUrl);
    })
    
})

function getAnalyticsChart(apiUrl) {
    fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        let chartStatus = Chart.getChart("myCharts");
        if (chartStatus != undefined) {
            chartStatus.destroy();
        }

        const ctx = document.querySelector("#myCharts").getContext("2d");
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