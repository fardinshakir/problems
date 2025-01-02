var fib = function(n) {
    let prev = 0
    let cur = 1
    for (i = 0; i <n; i++) {
        let oldcur = cur
        cur = cur + prev
        prev = oldcur
    }
    return prev
};


console.log(fib(4))