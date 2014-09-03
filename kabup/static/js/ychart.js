var rousoku=function(svg,dataSet,xScale,yScale){
	//ろうそく足（高値、安値）
	svg.selectAll("line")
	.data(dataSet)
	.enter()
	.append("line")
	.attr("x1",function(d){
		return xScale(d[0]);
	})
	.attr("y1",function(d){
		return yScale(d[2]);
	})
	.attr("x2",function(d){
		return xScale(d[0]);
	})
	.attr("y2",function(d){
		return yScale(d[3]);
	})
	.attr("stroke","black");
	//ろうそく足（始値、終値）
	svg.selectAll("rect")
	.data(dataSet)
	.enter()
	.append("rect")
	.attr("width",function(d){
		return 4;
	})
	.attr("height",function(d){
		var tmp = Math.abs(yScale(d[1])-yScale(d[4]));
		if(tmp==0){return 1;}
		else{
			return tmp;
		}
	})
	.attr("x",function(d){
		return xScale(d[0])-2;
	})
	.attr("y",function(d){
		if(d[1]<d[4]){
			return yScale(d[4]);
		}else{
			return yScale(d[1]);
		}
	})
	.attr("fill",function(d){
		if(d[1]<d[4]){
			return "blue";
		}else{
			return "red";		
		}
	});
}
var drawLine=function(svg,dataSet,line,color){
	svg.append("path")
		.datum(dataSet)
		.attr("class","line")
		.attr("d",line)
		.attr("stroke",color);
}

