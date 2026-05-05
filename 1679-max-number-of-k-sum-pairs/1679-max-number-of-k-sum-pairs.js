/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxOperations = function(nums, k) {
    let ans=0;
    let map = new Map();
    
    for(let num of nums){
        let d = k - num;

        if(map.has(d)){
            ans++;
            let v = map.get(d) - 1
            if(v == 0){
                map.delete(d)
            }else{
                map.set(d , v)
            }
        }else{
            map.set(num ,(map.get(num) || 0) + 1);
        }
        
    }
    return ans
};