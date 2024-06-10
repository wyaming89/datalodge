const fs = require('fs');
const echarts = require('echarts');

let chart = echarts.init(null,null, {
    renderer: 'svg',
    ssr: true,
    width: 400,
    height: 300
});

chart.setOption({
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line'
    }]
});

const svg = chart.renderToSVGString();

fs.writeFile('echart.svg', svg);