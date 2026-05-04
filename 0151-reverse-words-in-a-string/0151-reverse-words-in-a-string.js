/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    return s.trim().split(" ").reverse().filter((e)=>{ if(e) return e}).join(" ")
};