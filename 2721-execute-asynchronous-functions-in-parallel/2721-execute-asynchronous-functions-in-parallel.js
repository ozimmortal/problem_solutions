/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    
    return new Promise((resolve , reject)=>{
        let results = [];
        let completed = 0 , n = functions.length;

        functions.forEach((func, idx) =>{
            func().then((num)=>{
                results[idx] = num;
                completed++;

                if (completed === n){
                    resolve(results);
                }

            }).catch((msg) =>{
                reject(msg);
            })
        })
        
        
    })
    
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */