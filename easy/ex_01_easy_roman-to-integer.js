// https://leetcode.com/problems/roman-to-integer/description/

/**
 * @param {string} string
 * @return {number}
 */
var romanToInt = function(string) {
    var numbersMap = new Map(
        [
            ["I", 1],
            ["V", 5],
            ["X", 10],
            ["L", 50],
            ["C", 100],
            ["D", 500],
            ["M", 1000],
        ]
    )

    i = string.length - 1
    result = 0

    for (i; i >= 0; i--) {
        if (i == 0) {
            result += numbersMap.get(string[i])
        }
        else if (numbersMap.get(string[i]) > numbersMap.get(string[i - 1])) {
            result += numbersMap.get(string[i]) - numbersMap.get(string[i - 1])
            i--
        } else {
            result += numbersMap.get(string[i])
        }
    }
    
    return result
};

// change string to test other scenarios

console.log(romanToInt('XVII'))
console.log(romanToInt('IX'))
console.log(romanToInt('V'))
console.log(romanToInt('DCIVXX'))