function countgreater(x,y) {
    var greater=0;
    for(var i=0;i<x.length;i++){
        if(x[i]>y){
            greater++;
            console.log(x[i]);
        }
    }
    console.log(greater);
    return greater;
}
b=countgreater([1,2,3,4,5],3);


function maxMinAvg(arr) {
    var sum=0;
    var max=arr[0];
    var min=arr[0];
    for(var i=0;i<arr.length;i++){
        sum=sum+arr[i]
        if(arr[i]>max){
            max=arr[i];
        }
        else if (arr[i]<min){
            min=arr[i];
        }
    }
    var avg=sum/arr.length;
    arrnew=[max,min,avg];
    return arrnew; 
}
var b=[15,2,3,4,5,56];
console.log(maxMinAvg(b));


function replace_neg(x){
    var arr=[];
    for(var i=0;i<x.length;i++){
        if(x[i]<0){
            arr.push('dojo')
        }
        else{
            arr.push(x[i]);
        }
    }
    return arr;
}
b=replace_neg([1,2,-3,-5,5]);
console.log(b);


function remove_i(x,y,z){
    var arr=[];
    for(i=0;i<x.length;i++){
        if(i<y){
            arr.push(x[i]);
        }
        else if(i>z){
            arr.push(x[i]);
        }
    }
    return arr;
}
b=remove_i([20,30,40,50,60,70],2,4);
console.log(b);