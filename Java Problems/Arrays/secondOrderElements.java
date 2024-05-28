public static int[] getSecondOrderElements(int n, int []arr) {
       int large2 = Integer.MIN_VALUE;
       int large1 = arr[0];
       int small2 = Integer.MAX_VALUE;
       int small1 = arr[0];
       int[] result = new int[2];

       for(int i=1;i<n;i++){
           if(large1 < arr[i]){
               large2 = large1;
               large1 = arr[i];
           }
           else if(large2 < arr[i])
               large2 = arr[i];
            
           if(small1 > arr[i]){
               small2 = small1;
               small1 = arr[i];
           }
           else if(small2 > arr[i])
               small2 = arr[i];
       }

       result[0] = large2;
       result[1] = small2;

       return result;
    }
