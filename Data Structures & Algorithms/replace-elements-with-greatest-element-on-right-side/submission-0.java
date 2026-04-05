class Solution {
    public int[] replaceElements(int[] arr) {
        int maxNum = -1;
        for (int i = arr.length-1; i>=0; i--){
            int temp = maxNum;
            maxNum = Math.max(maxNum, arr[i]);
            arr[i] = temp;
        }
        return arr;
    }
}