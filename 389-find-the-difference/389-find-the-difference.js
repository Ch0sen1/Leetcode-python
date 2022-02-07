/**
 * @param {string} s
 * @param {string} t
 * @return {character}
 */
var findTheDifference = function(s, t) {
    let code = 0
    for (let i=0; i < t.length; i++){
        code += t.charCodeAt(i)
        if (i < s.length){
            code -= s.charCodeAt(i)
        }
    }
    return String.fromCharCode(code)
    
};