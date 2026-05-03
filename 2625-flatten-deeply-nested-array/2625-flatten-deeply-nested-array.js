/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    let res = []
    if (n == 0 ){
        res = res.concat(arr)
        return res
    }
    
    for (let v of arr){
        if (Array.isArray(v)){
            res.push(...flat(v , n - 1 ))
        }else{
            res.push(v)
        }
    }

    return res

    
    
};