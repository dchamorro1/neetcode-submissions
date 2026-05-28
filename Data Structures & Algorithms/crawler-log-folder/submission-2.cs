public class Solution {
    public int MinOperations(string[] logs) {
        var totalMovementsToBaseCount = 0;
        
        foreach(var action in logs){
            if (action == "../"){
                if (totalMovementsToBaseCount > 0) {
                    totalMovementsToBaseCount -= 1;
                }
            }else if(action == "./"){
                continue;
            }else{
                totalMovementsToBaseCount += 1;
            }
        }

        return totalMovementsToBaseCount;
    }
}