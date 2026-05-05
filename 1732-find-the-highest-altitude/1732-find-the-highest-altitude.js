/**
 * @param {number[]} gain
 * @return {number}
 */
var largestAltitude = function(gain) {
    let prefix = [0];
    for(let i=1; i<=gain.length; i++){
        prefix[i] = prefix[i-1] + gain[i-1];
    }
    return Math.max(...prefix)
};