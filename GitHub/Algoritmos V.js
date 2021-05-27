/**Ejercicio 1 **/
function reset(arr){
    for(var i=0;i<arr.length;i++){
        if (arr[i]<0){
            arr[i]=0;
        }
    }
    console.log(arr);
    return arr;
}
b=reset([1,2,-1,-3]);

/**Ejercicio 2**/
function move_left(arr){
    for(var i=0;i<arr.length;i++){
        if(i==arr.length-1){
            arr[i]=0;
        }
        else{
            arr[i]=arr[i+1];
        }
    }
    console.log(arr);
    return arr;
}
b=move_left([1,2,-1,-3]);

/**Ejercicio 3**/
function reverse(arr){
    var arr_new=[];
    for(var i= arr.length-1;i>=0;i--){
        arr_new.push(arr[i]);
    }
    console.log(arr_new);
    return arr_new;
}
b=reverse([1,2,-1,-3]);

/**Ejercicio 4**/
function repeat(arr){
    var arr_new=[];
    for(var i=0;i<arr.length;i++){
        arr_new.push(arr[i]);
        arr_new.push(arr[i]);
    }
    console.log(arr_new);
    return arr_new;
}
b=repeat([1,2,-1,-3]);