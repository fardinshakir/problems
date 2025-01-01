var fizzBuzz = function(n) {
    let my_array = []
    for (i = 1; i <= n; i++) {
        let output = ""
        if (i % 3 === 0) {
            output += 'Fizz'
        }
        if (i % 5 === 0) {
            output += 'Buzz'
        } 
        if (output === "") {
            output = String(i)
        }
        my_array.push(output)
        
    }
    return my_array
};

console.log(fizzBuzz(5))