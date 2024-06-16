/**
 * @param {string} s
 * @return {number}
 */
var minimumChairs = function(s) {
    let count = 0
    let max_count = 0

    for(let i = 0; i <= s.length; i++){
        if(s[i] == "E"){
            count += 1;
            max_count = Math.max(max_count, count);
        }
        else if(s[i] == "L") {
            count -= 1;  
        }
        
    }
    return max_count
};