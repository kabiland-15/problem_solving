import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
class HelloWorld {
    public static void main(String[] args) {
        int[] arr = {1,2,3,4,5};
        int n = arr.length;
        ArrayList<Integer> ans = new ArrayList<>();
        int i = 0;
        while(i<n){
            if(arr[i]<arr[i+1])
                break;
            i++;
        }
        int j = i;
        while(j < n){
            ans.add(arr[j]);
            j++;
        }
        int mini = Integer.MAX_VALUE;
        int flag = i;
        while(i<n){
            if(arr[flag]<arr[i])
                mini = Math.min(arr[i],mini);
            i++;
        }
        Collections.sort(ans);
        ans.remove(mini);
        arr[flag] = mini;
        for(int k=flag+1;k<n;k++){
            arr[k] = ans.get(k-flag-1);
        }
        System.out.print("[ ");
        for(int f:arr){
            System.out.print(f + " ");
        }
        System.out.print("]");
    }
}
