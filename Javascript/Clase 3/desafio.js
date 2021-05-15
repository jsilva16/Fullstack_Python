function hound(arr,x){
    var check=true;
    for(var i=0;i<arr.length;i++){
        if(arr[i]==x){
            console.log('El número está en la posición:',i+1);
            check=false;
            return i;
        }
    }
    if(check==true){
        console.log('El número no se encuentra en el arreglo')
    }
    return null;
}
b=hound([1,2,3,4,5,6,7,8,9],4);

function order(arr){
    var arr_temp=arr;
    var order=[];
    var min=arr[0];
    var max=0;
    for(var j=0;j<arr.length;j++){
        if(arr[j]>max){
            max=arr[j];
        }
    }
    while(order.length<arr.length){
        for(var i=0;i<arr_temp.length;i++){
            if(arr_temp[i]<min){
                min=arr_temp[i];
            }
        }
        order.push(min);
        console.log(order)
        min=arr_temp[0];
    }
    console.log(order)
    return order;
}
b=order([4,5,9,3,21,6,8]);
console.log(b);