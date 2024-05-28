 public static String read(int n, int []book, int target){
        Arrays.sort(book);
        int left = 0, right = n-1;
        while(left < right){
            int sum = book[left] + book[right];

            if(sum == target)
                return "YES";
            else if(sum > target)
                right--;
            else 
                left++;
        }
        return "NO";
    }