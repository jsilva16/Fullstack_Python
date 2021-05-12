/* obtener 1 al 255 */
function a (x){
    var arr=[];
    for (var i=1;i<=x;i++){
        arr.push(i);
    }
    return arr;
}
console.log(a(255));

/*Consigue pares hasta 1000*/
function sum_1000 (){
    var i=2;
    var sum = 0;
    while(i<=1000){
        sum += i;
        i +=2;
    }
    console.log(sum);
    return sum;
}
sum_1000();

/*Suma impares hasta 5000*/
function sum_5000 (){
    var i=1;
    var sum = 0;
    while(i<=5000){
        sum += i;
        i +=2;
    }
    console.log(sum);
    return sum;
}
sum_5000();

/*Itera un array*/
function a (arr){
    var sum=0;
    for(var i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    console.log(sum);
    return sum
}
a([1,2,5]);
a([-5,2,5,12]);

/*Encuentra el mayor (max)*/
function max (arr){
    var max= arr[0];
    for(var i=0;i<arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    console.log(max);
    return max;
}
max([-3,3,5,7]);

/*Encuentra el promedio (avg)*/
function avg(arr){
    var avg=0;
    var sum=0
    for(var i=0;i<arr.length;i++){
        sum+=arr[i];
    }
    avg=sum/arr.length;
    console.log(avg);
    return avg;
}
avg([1,3,5,7,20]);

/*Array de impares*/
function odd_numbs(){
    var arr=[];
    for(var i=1;i<=50;i+=2){
        arr.push(i);
    }
    console.log(arr);
    return arr;
}
odd_numbs();

/*Mayor que Y*/
function greater(y,arr){
    var great_numbs=0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>y){
            great_numbs++;
        }
    }
    console.log(great_numbs);
    return great_numbs;
}
greater(3,[1,3,5,7,15,20,1,54]);

/*Cuadrados*/
function squared(arr){
    var squared_arr=[];
    for(var i=0;i<arr.length;i++){
        squared_arr.push(arr[i]*arr[i]);
    }
    console.log(squared_arr);
    return squared_arr;
}
squared([1,5,10,-2]);

/*Negativos*/
function negs(arr){
    var arr_new=[]
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr_new.push(0);
        }
        else{
            arr_new.push(arr[i]);
        }
    }
    console.log(arr_new);
    return arr_new;
}
negs([1,5,10,-2]);

/*Max/Min/Avg*/
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
var b=[1,5,10,-2];
console.log(maxMinAvg(b));

/*Intercambia Valores*/
function swap(arr){
    var arr_new=[];
    var temp=arr[arr.length-1];
    for(var i=0;i<arr.length;i++){
        arr_new.push(arr[i]);
    }
    arr_new[arr_new.length-1]=arr_new[0];
    arr_new[0]=temp;
    console.log(arr_new);
    return arr_new;
}
swap([1,5,5,5,6,5,4,2,1,54,5,10,-2]);

/*De Número a String*/
function swap_negs(arr){
    var arr_new=[];
    for(var i=0;i<arr.length;i++){
        if(arr[i]<0){
            arr_new.push('Dojo');
        }
        else{
            arr_new.push(arr[i]);
        }
    }
    console.log(arr_new);
    return arr_new;
}
swap_negs([-1,-3,2]);