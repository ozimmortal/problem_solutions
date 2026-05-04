/**
 * @param {string} str1
 * @param {string} str2
 * @return {string}
 */
var gcdOfStrings = function(str1, str2) {
    let m = str1.length, n= str2.length;
    
    function isDivisor(l){
        if(!m %l || !n%l) return false
        let a = Math.floor(m / l) , b = Math.floor(n / l);

        return  str1.slice(0 , l).repeat(a) == str1 && str1.slice(0 , l).repeat(b) == str2;
    }
    
    for (let l= Math.min(m ,n); l>0; l--){
        
        if (isDivisor(l)) return str1.slice(0 , l)
    }
    return ""

    

};