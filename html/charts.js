var laytpl = layui.laytpl;

function fn(res) {
	var main = echarts.init(document.getElementById('main'));
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

	//计算六星抽取次数
	times = 0;
	RecentTimesArr = [];
	for (var i = 0, l = six.length; i < l; i++) {
		RecentTimes = six[i].times - times
		times = six[i].times;
		RecentTimesArr[i] = RecentTimes;
		if (i == six.length - 1) {
			RecentTimesArr[i + 1] = agent.length - six[i].times;
		}
	}
	for (var i = 0, l = six.length; i < l; i++) {
		six[i]['retimes'] = RecentTimesArr[i + 1];
	}

	//模板渲染《最近六星》
	var getTpl = RecentSix.innerHTML,
		view = document.getElementById('RecentSixView');
	laytpl(getTpl).render(six, function(html) {
		view.innerHTML = html;
	});

	//模板渲染《寻访统计》
	var GachaSta = [{
		"avg": 0,
		"luck": "非酋",
		"NoSix": 0,
		"SixNum": 0,
		"FiveNum": 0,
		"FourNum": 0
	}];
	//计算寻访六星平均数
	var SixTotal = 0;
	for (var i = 0, l = six.length; i < l; i++) {
		SixTotal += six[i].retimes
	}
	var SixAvg = parseInt(SixTotal / six.length);
	GachaSta[0]['avg'] = SixAvg;
	//计算非酋程度
	if (SixAvg <= 30) {
		GachaSta[0]['luck'] = "欧皇";
	} else if (SixAvg > 30 && SixAvg <= 40) {
		GachaSta[0]['luck'] = "正常人";
	} else if (SixAvg > 40 && SixAvg <= 60) {
		GachaSta[0]['luck'] = "非酋";
	} else {
		GachaSta[0]['luck'] = "超级大非酋";
	}
	//计算多久未出六星
	GachaSta[0]['NoSix'] = six[0]['times'];
	//计算各星级干员数量
	GachaSta[0]['SixNum'] = six.length;
	GachaSta[0]['FourNum'] = four.length;
	GachaSta[0]['FiveNum'] = five.length;
	console.log(GachaSta);
	var sta = [{
		"avg": 50,
		"luck": "非酋",
		"NoSix": 27,
		"SixNum": 1,
		"FiveNum": 20,
		"FourNum": 20
	}];
	var getTpl2 = GachaStatistics.innerHTML,
		view2 = document.getElementById('GachaStatisticsView');
	laytpl(getTpl2).render(GachaSta, function(html) {
		view2.innerHTML = html;
	});
}
