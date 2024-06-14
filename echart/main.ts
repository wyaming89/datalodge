const fs = require('fs');
const echarts = require('echarts');
// const sqlite = require('sqlite');
import * as sqlite from 'sqlite';



async function get_data(){
    const db = new sqlite.Database('./data/data.db');
    let date:string[] = []
    let cnt:number[] = []
    let data = await db.all(`SELECT create_time 
	  ,sum(house_num) AS cnt
FROM gzdata g 
WHERE TYPE = '签约'
GROUP BY create_time `)

console.log(data)

    return [date,cnt]
}


function main(){
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

fs.writeFile('echart2.svg', svg, function (err:Error) {
    if (err){
        console.log(err);
    }else {
    console.log('Saved!');
    process.exit(0);
    }
});
}

// main()
(async () => { 
    let data = await get_data()
console.log(data)
})()