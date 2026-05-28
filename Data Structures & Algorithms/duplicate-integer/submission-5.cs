public class Solution {
    public bool hasDuplicate(int[] nums) {
        var numsAsHashSet = new HashSet<int>(nums);

        return numsAsHashSet.Count < nums.Length;


    }
}