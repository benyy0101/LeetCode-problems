import java.util.Arrays;

class Solution {
    public String reversePrefix(String word, char ch) {
        char[] target = word.toCharArray();
        int idx = 0;
        StringBuilder sb = new StringBuilder();
        for(char i: target){
            if(i == ch){
                for(int j = idx ; j >= 0 ;j--){
                    sb.append(target[j]);
                }
                for(int j = idx+1, end = target.length; j < end;j++){
                    sb.append(target[j]);
                }
                break;
            }
            idx++;
        }
        if(idx == target.length){
            return word;
        }
        else{
            return sb.toString();
        }
        
    }
}