/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var maxVowels = function(s, k) {

    let vowels = ['a', 'e', 'i', 'o', 'u'];
    let count = 0, l = 0;
    let ans=0;

    for(let r=0; r<s.length; r++){
        count += vowels.includes(s[r]) ? 1 : 0

        if(r - l + 1 === k){
            ans = Math.max(ans, count);
            count -= vowels.includes(s[l]) ? 1 : 0;
            l++;
        }
    }
    return ans
    
};