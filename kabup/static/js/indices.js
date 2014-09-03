var movingAv=function(dataSet,span){
	var mv = [];
	for(var i=0;i<dataSet.length-span;i++){
		var element=[];
		element.push(dataSet[i+span][0]);
		for(var j=1;j<dataSet[i].length;j++){
			sum=0;
			for(var k=i;k<i+span;k++){
				sum+=dataSet[k][j];
			}
			element.push(Math.round(sum/span));
		}
		mv.push(element);
	}
	return mv;
}
var baseLine=function(dataSet,span){
	var bl = [];
	for(var i=0;i<dataSet.length-span;i++){
		var element=[];
		element.push(dataSet[i+span][0]);
		var min_v=Number.MAX_VALUE;
		var max_v=0;
		for(var k=i;k<i+span;k++){
			if(max_v<dataSet[k][1]){
				max_v=dataSet[k][1];
			}
			if(min_v>dataSet[k][2]){
				min_v=dataSet[k][2];
			}
		}
		element.push(Math.round((max_v+min_v)/2));
		bl.push(element);
	}
	return bl;
}
var timeShift=function(dataSet,span){
	var ts = [];
	for(var i=0;i<dataSet.length;i++){
		if(i+span>=dataSet.length){
			break;
		}
		if(i+span>=0){
			var element=[];
			element.push(dataSet[i+span][0]);
			tmp = dataSet[i];
			for(var j=1;j<tmp.length;j++){
				element.push(dataSet[i][j]);
			}
			ts.push(element);
		}
	}
	return ts;
}
var dataAv=function(data1,data2){
	var da = [];
	var dataLength = 0;
	if(data1.length<data2.length){
		dataLength = data1.length;
	}else{
		dataLength = data2.length;
	}
	for(var i=0;i<dataLength;i++){
		var element = [];
		element.push(data1[i][0]);
		for(var j=1;j<data1[i].length;j++){
			element.push(Math.round((data1[i][j]+data2[i][j])/2));
		}
		da.push(element);
	}
	return da;
}
