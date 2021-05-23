function recursiveSort(arr) {
    console.log('arr passed is', arr);

    if(arr.length == 1){
        return arr;
    }
    var max = arr[0];
    var maxidx = 0;

    // encuentra el valor máximo y maxidx
    for(var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            max = arr[i];
            maxidx = i;
        }
    }

    arr[maxidx] = arr[arr.length-1];
    arr.pop();
    console.log('Maximum found', max);

    x = recursiveSort(arr);
    console.log('x is', x);
    x.push(max);
    return x;
}
output = recursiveSort([5,3,7]);
console.log('Final Output', output);