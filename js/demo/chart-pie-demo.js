// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['CA','TX','FL','NY','IL','PA','NJ','MI','GA','OH'],
    datasets: [{
      data: [8700000000,5800000000,4800000000,2500000000,2400000000,2400000000,2400000000,2400000000,2100000000,2100000000],
      backgroundColor: ['#2e59d9', '#17a673', '#FF0000','#ffcc00','#663300','#cccc00','#66ffff','#b3ccff','#7575a3','#6b6161'],
      hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf','#ffcc00','#663300','#cccc00','#66ffff','#b3ccff','#7575a3','#6b6161'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#FF0000',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
      
    },
    legend: {
      display: true
    },
    cutoutPercentage: 80,
  },
});
