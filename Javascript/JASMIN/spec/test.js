//funcion suma max y min//

function sum_min_max(arr){
    var min=arr[0];
    var max=arr[0];
    var sum=0;
    for (var i=0;i<arr.length;i++){
        if(arr[i]>max){
            max=arr[i];
        }
        else if(arr[i]<min){
            min=arr[i];
        }
        sum=max+min;
    }
    console.log(max);
    console.log(min);
    console.log(sum);
    return sum;
}
sum_min_max([6,25,6,3,8,30]);
describe("Prueba de la función",function(){
    it("Debe entregar 33", function(){
        expect(sum_min_max([6,25,6,3,8,30])).toEqual(33);
    });
    it("Debe entregar 236", function(){
        expect(sum_min_max([1,4,6,6,5,45,235,25,6,3,8,30])).toEqual(236);
    });
    it("Debe entregar 24", function(){
        expect(sum_min_max([6,25,-6,3,8,30])).toEqual(24);
    });
    it("Debe entregar 24", function(){
        expect(sum_min_max([6,2.5,-6,3,8,30])).toEqual(24);
    });
    it("Debe entregar 24", function(){
        expect(sum_min_max([6,25,-6,3,'casa',8,30])).toEqual(24);
    });
});

//imprime el penultimo y devuelve el primer impar
function return_odd(arr){
    console.log(arr[arr.length-2]);
    for(var i=0;i<arr.length;i++){
        if(arr[i]%2!=0){
            return arr[i];
        }
    }
}

describe("Prueba de la función",function(){
    it("Debe entregar 25", function(){
        expect(return_odd([6,25,6,3,8,30])).toEqual(25);
    });
    it("Debe entregar 1", function(){
        expect(return_odd([1,4,6,6,5,45,235,25,6,3,8,30])).toEqual(1);
    });
    it("Debe entregar 23", function(){
        expect(return_odd([6,4,23,4,6,225,-6,3,8,30])).toEqual(23);
    });
    it("Debe entregar 7", function(){
        expect(return_odd([6,7,-6,3,8,30])).toEqual(7);
    });
    it("Debe entregar 25", function(){
        expect(return_odd([6,25,-6,3,'casa',8,30])).toEqual(25);
    });
});

/*Contar Positivos */
function count_pos(arr){
    var positives=0;
    for(var i=0;i<arr.length;i++){
        if(arr[i]>0){
            positives++;
        }
    }
    return positives;
}
b=count_pos([6,-25,6,3,-8,30]);
console.log(b);

describe("Prueba de la función",function(){
    it("Debe entregar 4", function(){
        expect(count_pos([6,-25,6,3,-8,30])).toEqual(4);
    });
    it("Debe entregar 7", function(){
        expect(count_pos([1,-4,6,-6,5,-45,235,-25,6,3,-8,30])).toEqual(7);
    });
    it("Debe entregar 9", function(){
        expect(count_pos([6,4,23,4,6,22.5,-6,3,8,30])).toEqual(9);
    });
    it("Debe entregar 9", function(){
        expect(count_pos([6,7,-6,3,8,-30,5,2,3,0,22])).toEqual(8);
    });
    it("Debe entregar 4", function(){
        expect(count_pos([-6,25,-6,3,'casa',8,30])).toEqual(4);
    });
});
