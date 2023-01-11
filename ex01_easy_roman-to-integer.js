/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
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

    i = s.length - 1
    result = 0

    for (i; i >= 0; i--) {
        if (i == 0) {
            result += numbersMap.get(s[i])
        }
        else if (numbersMap.get(s[i]) > numbersMap.get(s[i - 1])) {
            result += numbersMap.get(s[i]) - numbersMap.get(s[i - 1])
            i--
        } else {
            result += numbersMap.get(s[i])
        }
    }
    
    return result
};
