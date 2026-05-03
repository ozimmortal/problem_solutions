var TimeLimitedCache = function() {
    // the store includes key , value , start_time , duration
    // key => [value ,start_time , duration]
    this.store = new Map();
    
};








/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    let curTime = Date.now()
    let state = false
    if (this.store.has(key)){
        let res = this.store.get(key)
        if(curTime - res[1] <= res[2]){
            state = true
        }
    }
    this.store.set(key , [value , Date.now() , duration]);
    return state
    
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    if (this.store.has(key)){
        let res = this.store.get(key)
        let curTime = Date.now()
        if(curTime - res[1] <= res[2]){
            return res[0]
        }
    }
    return  -1
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    let count = 0;
    for(let key of this.store.keys()){
        let curTime = Date.now()
        let [val , st , duration] = this.store.get(key);
        if(curTime - st <= duration){
            count++
        }

    }
    return count;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */