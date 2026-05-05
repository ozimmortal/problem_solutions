/**
 * @param {character[]} chars
 * @return {number}
 */
var compress = function(chars) {

    let c = 0 , l = 0;

    for(let r=0; r <chars.length; r++){
        if(chars[r] != chars[r + 1] || r + 1 == chars.length){
            let d = r - l + 1;
            chars[c] = chars[r]
            c++;

            if( d > 1){
                for(let ch of String(d)){
                    chars[c] = ch
                    c++;
                }              
            }
            l = r + 1
        }
    }
    let n = chars.length
    for(let i=c; i<n; i++){
        chars.pop()
    }
    return chars.length


    
};