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
