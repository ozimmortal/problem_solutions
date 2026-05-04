/**
 * @param {string} s
 * @return {string}
 */
var reverseVowels = function(s) {

    let l = 0 , r = s.length -1 , vowels = ['a','e','i','o','u'];
    s = s.split("");

    while(l <= r){
        let w1 = s[l].toLowerCase(), w2 = s[r].toLowerCase()
        if (vowels.includes(w1) && vowels.includes(w2)){
            [s[l] , s[r]] = [s[r] , s[l]]
            l++;
            r--;
        }else if(vowels.includes(w1) && !vowels.includes(w2)){
            r--;
        }else if(!vowels.includes(w1) && vowels.includes(w2)){
            l++;
        }else{
            l++;
            r--;
        }
    }
    return s.join("")



    
};