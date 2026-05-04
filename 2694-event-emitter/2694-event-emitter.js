class EventEmitter {
    
    /**
     * @param {string} eventName
     * @param {Function} callback
     * @return {Object}
     */
    constructor() {
        this.events = {};
        this.counter = 0
    }
    subscribe(eventName, callback) {
        if (!this.events[eventName]){
            this.events[eventName] = {}
        }
        const id = this.counter;
        this.events[eventName][id] = callback
        this.counter++;

        return {
            unsubscribe: () => {
                if (this.events[eventName]){
                    delete this.events[eventName][id];
                }
            }
        };
    }
    
    /**
     * @param {string} eventName
     * @param {Array} args
     * @return {Array}
     */
    emit(eventName, args = []) {
        
        let res = []
        const callbacks = this.events[eventName];
        for(let key in callbacks){
            res.push(callbacks[key](...args))
        }
        return res
    }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */