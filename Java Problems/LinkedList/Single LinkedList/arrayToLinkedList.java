public static Node constructLL(int []arr) {
        Node head = new Node(arr[0]);
        Node move = head;
        for(int i=1;i<arr.length;i++){
            Node temp = new Node(arr[i]);
            move.next = temp;
            move = move.next;
        }
        return head;
    }