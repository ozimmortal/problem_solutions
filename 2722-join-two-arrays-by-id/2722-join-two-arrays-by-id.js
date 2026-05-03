/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    let seen = new Map();
    
    for(let i=0; i<arr1.length; i++){
        seen.set(arr1[i].id , i)
    }

    for(let i=0; i<arr2.length; i++){
        if (seen.has(arr2[i].id)){
            let idx = seen.get(arr2[i].id);
            for (let k in arr2[i]){
                arr1[idx][k] = arr2[i][k]
            }
        }else{
            arr1.push(arr2[i])
        }
    }
    return arr1.sort((a , b) => a.id - b.id)

    
};