jQuery(document).ready(function ($) {

    // Smooth scroll for the menu and links with .scrollto classes
    $('.smothscroll').on('click', function (e) {
        e.preventDefault();
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            if (target.length) {

                $('html, body').animate({
                    scrollTop: target.offset().top - 62
                }, 1500, 'easeInOutExpo');
            }
        }
    });

    $('.carousel').carousel({
        interval: 3500
    });

    // PCBDesign Chart
    var doughnutData = [{
        value: 80,
        color: "#1abc9c"
    },
    {
        value: 20,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("pcbdesign").getContext("2d")).Doughnut(doughnutData);

    // Circuit Chart
    var doughnutData = [{
        value: 90,
        color: "#1abc9c"
    },
    {
        value: 10,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("circuit").getContext("2d")).Doughnut(doughnutData);

    // C++ Chart
    var doughnutData = [{
        value: 95,
        color: "#1abc9c"
    },
    {
        value: 5,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("embc").getContext("2d")).Doughnut(doughnutData);

    // Python/Django
    var doughnutData = [{
        value: 80,
        color: "#1abc9c"
    },
    {
        value: 20,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("python").getContext("2d")).Doughnut(doughnutData);

    // Photoshop Chart
    var doughnutData = [{
        value: 95,
        color: "#1abc9c"
    },
    {
        value: 5,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("photoshop").getContext("2d")).Doughnut(doughnutData);

    // Illustrator Chart
    var doughnutData = [{
        value: 95,
        color: "#1abc9c"
    },
    {
        value: 5,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("illustrator").getContext("2d")).Doughnut(doughnutData);
    
    // Sold Works Chart
    var doughnutData = [{
        value: 70,
        color: "#1abc9c"
    },
    {
        value: 30,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("solid").getContext("2d")).Doughnut(doughnutData);
    
    // Microsoft Office Chart
    var doughnutData = [{
        value: 75,
        color: "#1abc9c"
    },
    {
        value: 25,
        color: "#ecf0f1"
    }
    ];
    var myDoughnut = new Chart(document.getElementById("msoffice").getContext("2d")).Doughnut(doughnutData);
});
