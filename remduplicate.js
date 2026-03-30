/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums === 0) return 0;
    let k = 1
    for (let i = 1;
        i < length(nums);
        i++
        ){
            if (nums[i] !== nums[i-1]){
                nums[k] === nums[i];
                k++;
            }

    }
    return 0
    
};