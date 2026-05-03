/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    let items = 0;
    for(let _ in obj){
        items++;
    }
    return items === 0
};