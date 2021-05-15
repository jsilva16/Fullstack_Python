/*1.Sigma*/
function sigma(x){
    var i=1;
    var sum=0;
    var suma='';
    while(i<=x){
        sum+=i;
        suma+=i;
        if(i<x){
            suma+='+';
        }
        i++;
    }
    console.log('Sigma'+'('+x+')','=',sum,'('+suma+')');
}
sigma(5);

/*2.Factorial*/
function factorial(x){
    var i=1;
    var mult=1;
    var fact='';
    while(i<=x){
        mult=mult*i;
        fact+=i;
        if(i<x){
            fact+='*';
        }
        i++;
    }
    console.log('Factorial'+'('+x+')','=', mult,'('+fact+')');
}
factorial(10);

/*Fibonacci*/
function fibo(x){
    var i=1;
    var sum=0;
    var fib=[0];
    while(i<=x){
        if(i-2<0){
            fib.push(1);
            i++;
            continue;
        }
        sum=fib[i-2]+fib[i-1];
        fib.push(sum);
        i++;
    }
    if (x<2){
        console.log('Fibonacci('+x+') =',fib[fib.length-1],'(Dado)');
    }
    else{
        console.log('Fibonacci('+x+') =',fib[fib.length-1],'(Fib('+(x-2)+') + Fib('+(x-1)+'))');
    }
    
    return fib;
}
b=fibo(0)
console.log(b);

/*Array: Penúltimo*/
function second_last(arr){
    if(arr.length<2){
        return null;
    }
    else{
        return arr[arr.length-2];
    }
}
b=second_last([42,true,4,'Liam',7]);
console.log(b);

/*n_ultimo*/
function n_last(arr,x){
    if(arr.length<2){
        return null;
    }
    else{
        return arr[arr.length-(x+1)];
    }
}
b=n_last([5,2,3,6,4,9,7],3);
console.log(b)

/*Array: Segundo más grande*/
function second_max(arr){
    var max=arr[0];
    var min=arr[0];
    var indice=0;
    if(arr.length<2){
        return null;
    }
    for(var i=0;i<arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
            indice=i;
        }
        if(arr[i]<min){
            min=arr[i];
        }
    }
    arr[indice]=min;
    max=arr[0];
    for(var i=0;i<arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
    }
    return max;
}
b=second_max([42,1,4,3.14,7,20]);
console.log(b);

/*  */ 






/*fib recursion*/
function fib(x){
    if (x<2){
        return x;
    }
    else{
        return fib(x-2)+fib(x-1);
    }
}
b=fib(10);
console.log(b);