Highcharts.chart('prod-chart', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Productos por tipo'
    },
    xAxis: {
        categories: []
    },
    series: [
        {
            name: 'Tipos',
            data: []
        }

    ]
});

Highcharts.chart('ped-chart', {
    chart: {
        type: 'column'
    },
    title: {
        text: 'Pedidos por comuna'
    },
    xAxis: {
        categories: []
    },
    series: [
        {
            name: 'Comunas',
            data: []
        }

    ]
});

fetch("http://127.0.0.1:5000/get-estadisticas")
    .then((response) => response.json())
    .then((data) => {
        let tipos = []
        let parsedDataProd = data[0].map((item) => {
            tipos.push(item.tipo)
            return [
                item.tipo,
                item.count,
            ]
        })
        let comunas = []
        let parsedDataPed = data[1].map((item) => {
            comunas.push(item.comuna)
            return [
                item.comuna,
                item.count,
            ]
        })

        const chartProd = Highcharts.charts.find(
            (chartProd) => chartProd && chartProd.renderTo.id === "prod-chart"
        );

        const chartPed = Highcharts.charts.find(
            (chartPed) => chartPed && chartPed.renderTo.id === "ped-chart"
        );

        chartProd.update({
            xAxis : {
                categories: tipos
            },
            series: [
                {
                    data: parsedDataProd,
                },
            ],
        });

        chartPed.update({
            xAxis : {
                categories: comunas
            },
            series: [
                {
                    data: parsedDataPed,
                },
            ],
        });
    })
    .catch((error) => console.error("Error:", error))