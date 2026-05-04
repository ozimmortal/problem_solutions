/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    
    function compactArr(arr){
        let res = [ ]
        for (let e of arr){
            if (Array.isArray(e)){
                res.push(compactArr(e))
            } else if (typeof e === "object" && e !== null) {
                res.push(compactobj(e))
            } else {
                if (e) res.push(e)
            }
        }
        return res
    }

    function compactobj(obj){
        let res = {};

        for (let key in obj){
            let val = obj[key] 
            if(typeof val === "object"  && val !== null && !Array.isArray(val)){
                res[key] = compactobj(val)
            }else if (Array.isArray(val)){
                res[key] = compactArr(val)
            }else{
                if (val) res[key] = val
            }
            
        }
        return res
    }

    if(Array.isArray(obj)){
        return compactArr(obj)
    }else{
        return compactobj(obj)
    }

};