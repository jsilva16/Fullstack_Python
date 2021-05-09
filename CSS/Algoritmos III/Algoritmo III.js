function printAverage(x){
    sum = 0;
    avg = 0;
    for (i=0;i<x.length;i++){
        sum=sum+x[i]
    }
    avg=sum/x.length;
    return avg
}
y = printAverage([1,2,3]);
 console.log(y); // should log 2

y = printAverage([2,5,8]);
 console.log(y); // should log 5


function returnOddArray(){
    arr=[];
    for(i=0;i<256;i++){
        if(i%2!==0){
            arr.push(i);
        }
    }
    return arr;
}
y = returnOddArray();
console.log(y); 

function squareValue(x){
    for(i=0;i<x.length;i++){
        x[i]= x[i]*x[i];
    }
    return x;
}
y = squareValue([1,2,3]);
console.log(y); // should log [1,4,9]

y = squareValue([2,5,8]);
 console.log(y); // should log [4,25,64]


