$(function() {
    $("#chart").css("display","none");
    $("#float_chart div").mouseover(function(){
        var stock_num = $(this).children("a").text();
        $.getJSON('/kabuka_json/'+stock_num, function(data) {

            // split the data set into ohlc and volume
            var ohlc = [],
            volume = [],
            short_average = [],
            long_average = [],
            dataLength = data.length;

            for (i = 0; i < dataLength; i++) {
                ohlc.push([
                    data[i][0], // the date
                    data[i][1], // open
                    data[i][2], // high
                    data[i][3], // low
                    data[i][4] // close
                ]);

                volume.push([
                    data[i][0], // the date
                    data[i][5] // the volume
                ])

                short_average.push([
                    data[i][0], // the date
                    data[i][6] //short average
                ])

                long_average.push([
                    data[i][0], // the date
                    data[i][7]  // long average
                ])


            }

            // set the allowed units for data grouping
            var groupingUnits = [[
                'week',                         // unit name
                [1]                             // allowed multiples
            ], [
                'month',
                [1, 2, 3, 4, 6]
            ]];

            // create the chart
            $('#chart').highcharts('StockChart', {

                rangeSelector: {
                    inputEnabled: $('#chart').width() > 480,
                    selected: 1
                },

                title: {
                    text: '銘柄番号'+stock_num+'の株価'
                },

                yAxis: [{
                    labels: {
                        align: 'right',
                        x: -3
                    },
                    title: {
                        text: 'ロウソク足'
                    },
                    height: '60%',
                    lineWidth: 2
                }, {
                    labels: {
                        align: 'right',
                        x: -3
                    },
                    title: {
                        text: '売買高'
                    },
                    top: '65%',
                    height: '35%',
                    offset:0,
                    lineWidth: 2
                }],
                
                series: [{
                    type: 'candlestick',
                    name: stock_num,
                    data: ohlc,
                    dataGrouping: {
                        units: groupingUnits
                    }
                }, {
                    type: 'column',
                    name: '売買高',
                    data: volume,
                    yAxis: 1,
                    dataGrouping: {
                        units: groupingUnits
                    }
                }, {
                    name: '短期平均線',
                    data: short_average,
                    dataGrouping: {
                        units: groupingUnits
                    }
                }, {
                    name: '長期平均線',
                    data: long_average,
                    dataGrouping: {
                        units: groupingUnits
                    }
                }]
            }).show();
        });

    });
});
