var main = echarts.init(document.getElementById('main'));

function fn(res) {
	// console.log(res.data)
	var six = []
	var five = []
	var four = []
	var three = []
	var agent = []
	// 将所有干员信息放在同一个数组里
	for (var i = 0, l = res.data.length; i < l; i++) {
		for (var n = 0, ln = res.data[i].chars.length; n < ln; n++) {
			agent.push(res.data[i].chars[n]);
		}
	}

	// 讲干员按星级分到不同数组
	var cnt = 0;
	for (var i = 0, l = agent.length; i < l; i++) {
		cnt += 1;

		if (agent[i].rarity == 5) {
			agent[i]['times'] = cnt;
			six.push(agent[i]);
		} else if (agent[i].rarity == 4) {
			agent[i]['times'] = cnt;
			five.push(agent[i]);
		} else if (agent[i].rarity == 3) {
			agent[i]['times'] = cnt;
			four.push(agent[i]);
		} else {
			agent[i]['times'] = cnt;
			three.push(agent[i]);
		}
	}

	// 整合成echart饼图所需要的数据
	var ChartData = [];
	var sixData = {};
	var fiveData = {};
	var fourData = {};
	var threeData = {};
	sixData['value'] = six.length;
	sixData['name'] = '六星干员';
	ChartData[0] = sixData;
	fiveData['value'] = five.length;
	fiveData['name'] = '五星干员';
	ChartData[1] = fiveData;
	fourData['value'] = four.length;
	fourData['name'] = '四星干员';
	ChartData[2] = fourData;
	threeData['value'] = three.length;
	threeData['name'] = '三星干员';
	ChartData[3] = threeData;
	option = {
		title: {
			text: '近百次寻访记录',
			left: 'center'
		},
		tooltip: {
			trigger: 'item'
		},
		legend: {
			orient: 'vertical',
			left: 'left'
		},
		series: [{
			name: '寻访',
			type: 'pie',
			radius: '50%',
			data: ChartData,
			emphasis: {
				itemStyle: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}]
	};
	main.setOption(option);
}
