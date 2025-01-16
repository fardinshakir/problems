var isPalindrome = function(x) {
    if ( x < 0) {
        return false
    } else if (x.toString().length == 1) {
        return true
    }
    let my_array = Array.from(String(x), Number)
    let inverse = [...my_array].reverse()
    for (let [i, n] of my_array.entries()) {
        if (my_array[i] === inverse[i]) {
        } else {
            return false
        }
    }
    return true
};

console.log(isPalindrome(15))