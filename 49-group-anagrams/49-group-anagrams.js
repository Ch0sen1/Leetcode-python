/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    let dic = {}
    for (let word of strs) {
        let groupKey = word.split("").sort().join("")
        dic[groupKey] ? dic[groupKey].push(word) : dic[groupKey] = [word]
    }
    
    return Object.values(dic)
};