/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    let canBePlanted = 0;
    let j =0 , l = flowerbed.length
    while ( j < n){
        for(let i=0; i<l; i++){
            const left = i - 1,  right = i + 1; 
            
            if((flowerbed[i]==0) && (left < 0 || (left>=0 && flowerbed[left]==0)) && (right >= l || (right<l && flowerbed[right]==0))){
                canBePlanted++;
                flowerbed[i] = 1
                break;
            }
            
        }
        j++;
    }
    console.log(flowerbed)
    return canBePlanted === n
};