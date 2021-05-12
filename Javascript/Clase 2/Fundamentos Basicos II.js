/*Tamaño Grande*/
function swap_bigs(arr){
    var arr_new=[];
    for(var i=0;i<arr.length;i++){
        if(arr[i]>0){
            arr_new.push('big');
        }
        else{
            arr_new.push(arr[i]);
        }
    }
    console.log(arr_new);
    return arr_new;
}
swap_bigs([-1,3,5,-5]);

/*Imprime (print) el menor, devuelve (return) el mayor*/
function min_max(arr){
    var min=arr[0];
    var max=arr[0];
    for(var i=0;i<arr.length;i++){
        if(min>arr[i]){
            min=arr[i];
        }
        else if (max<arr[i]){
            max=arr[i];
        }
    }
    console.log(min);
    return max;
}
b=min_max([1,5,5,5,6,5,4,2,1,54,5,10,-2]);
console.log(b);

/*Imprime (print) uno, devuelve (return) otro*/
function return_odd(arr){
    console.log(arr[arr.length-2]);
    for(var i=0;i<arr.length;i++){
        if(arr[i]%2!=0){
            return arr[i];
        }
    }
}
b=return_odd([2,4,4,5,6,5,4,2,1,54,5,10,-2]);
console.log(b);

/*Doble Visión*/
function double(arr){
    var double_arr=[];
    for(var i=0;i<arr.length;i++){
        double_arr.push(arr[i]*2);
    }
    console.log(double_arr);
    return double_arr;
}
double([1,5,10,-2]);

/*Contar Positivos */
function count_pos(arr){
    var positives=0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>0){
            positives++;
        }
    }
    arr[arr.length-1]=positives;
    return arr;
}
b=count_pos([2,4,4,5,6,5,4,2,1,54,5,10,-2]);
console.log(b);

/*Pares e Impares*/
function odd_and_even(arr){
    for(var i=0;i<arr.length-2;i++){
        if(arr[i]%2!=0&&arr[i+1]%2!=0&&arr[i+2]%2!=0){
            console.log("¡Qué imparcial!");
        }
        else if(arr[i]%2==0&&arr[i+1]%2==0&&arr[i+2]%2==0){
            console.log("¡Es para bien!");
        }
    }
}
b=odd_and_even([2,4,4,5,6,5,5,5,4,2,54,5,10,-2]);

/*Incrementa los Segundos*/
function rise_2nds(arr){
    for(var i=0;i<arr.length;i++){
        if (i%2==1){
            arr[i]++;
        }
        console.log(arr[i])
    }
    console.log(arr);
}
b=rise_2nds([2,4,4,5,6,5,5,5,4,2,54,5,10,-2]);

/*Longitudes previas*/
function prev_lengths(arr){
    for(var i=arr.length-1;i>0;i--){
        arr[i]=arr[i-1].length;
    }
    console.log(arr);
}
b=prev_lengths(['programar','dojo','genial','paralelepipedo','escandinavia']);

/*Agrega Siete*/
function add_7(arr){
    var arr_new=[];
    for(var i=0;i<arr.length;i++){
        arr_new.push(arr[i]+7);
    }
    console.log(arr_new);
    return arr_new;
}
b=add_7([1,2,3]);

/*Array Inverso*/
function inverse(arr){
    var temp=0;
    var j=0
    for(var i=arr.length-1;i>=arr.length/2;i--){
    temp=arr[j]; /*temp=3*/
    arr[j]=arr[i]; /*arr[j]=2*/
    arr[i]=temp; /*arr[i]=3*/
    j++
}
console.log(arr);
return arr;
}
b=inverse([3,1,6,4,2]);
c=inverse([3,1,6,8,6,5]);

/*Perspectiva: Negativa*/
function neg_persp(arr){
    var arr_new=[];
    var i=0;
    while(i<arr.length){
        if(arr[i]>0){
            arr_new.push(arr[i]*-1);
        }
        else{
            arr_new.push(arr[i]);
        }
        i++;
    }
    console.log(arr_new);
    return arr_new;
}
b=neg_persp([1,-3,-4,1,6,8,-9,5]);

/*Siempre hambriento*/
function hungry(arr){
    var arr_new=[];
    var i=0;
    while(i<arr.length){
        if(arr[i]=='comida'){
            arr_new.push(1);
            console.log('yummy');
        }
        i++;
    }
    if(arr_new.length==0){
        console.log('tengo hambre')
        }
}
b=hungry([1,'comida',-4,1,'comida',8,-9,5]);

/*Cambiar hacia el centro*/
function mid_swap(arr){
    var temp=arr[0];
    arr[0]=arr[arr.length-1];
    arr[arr.length-1]=temp;
    temp=arr[2];
    arr[2]=arr[arr.length-3];
    arr[arr.length-3]=temp;
    console.log(arr);
}
b=mid_swap([1,'comida',-4,1,'comida',8,-9,5]);
b=mid_swap([1,2,3,4,5,6,7,8,9]);

/*Escala el Array*/
function scale(arr,x){
    var i=0;
    while(i<arr.length){
        arr[i]=arr[i]*x;
        i++;
    }
    console.log(arr);
    return arr;
}
b=scale([1,2,3,4,5,6,7,8,9],4);
b=scale([1,2,3],3)