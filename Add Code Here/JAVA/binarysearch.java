public class binarysearch {
    public static void main(String[] args) {
        int[] nums = {1,2,3,45,65,78,552,1024,2048,4096};
        int bsearch = search(nums, 552);
        System.out.println(search(nums,bsearch));
    }

    //return the index
    public static int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length;
        while(start<end){
            int mid = start + (end-start) /2 ;
            if(target < nums[mid]){
                end = mid-1;
            }
            else if(target > nums[mid]){
                start = mid + 1;
            }
            else{
                return mid;
            }
        }
        return -1;
    }
}