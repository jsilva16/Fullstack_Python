function printUpTo(x) {
  if(x<0){
    console.log(false);
    return false;
  }
  for (i=0;i<=x;i++){
    console.log(i);
  }
}
printUpTo(1000); // debería imprimir todos los enteros de 1 to 1000
y = printUpTo(-10); // debería imprimir false
console.log(y); // debería imprimir false

function printSum(x) {
  var sum = 0;
  for(i=0;i<=x;i++){
    sum+=i;
    console.log(i);
    console.log(sum);
  }
  return sum
}
y = printSum(255) // debería imprimir todos los enteros de 0 a 255 y que cada entero imprima la suma parcial.
console.log(y) // // debería imprimir 32640


function printSumArray(x) {
  var sum = 0;
  for(var i=0; i<x.length; i++) {
    sum= sum+x[i];//your code here
  }
  return sum;
}
console.log( printSumArray([1,2,3]) ); // debería imprimir 6

function max(x) {
  var max=x[0];
  for (i=0;i<x.length;i++){
    if(x[i]>max){
      max = x[i];
    }
  }
  return max;
}
console.log(max([1,30,5,7]));