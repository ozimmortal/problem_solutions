/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    
    let p1 = 0, p2 = 0;
    let ans = "";
    while(p1 < word1.length && p2 < word2.length){
        ans += word1[p1] + word2[p2];
        p1++;
        p2++;
    }

    if (p1 < word1.length){
        ans+=word1.slice(p1 , word1.length)
    }else{
        ans+=word2.slice(p2 , word2.length)
    }

    return ans
};