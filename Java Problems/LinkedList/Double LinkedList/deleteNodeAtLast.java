 public static Node deleteLastNode(Node head) {
        if(head == null || head.next == null)
            return null;
        Node temp = head;
        while(temp.next.next != null)
            temp = temp.next;
        temp.next.prev = null;
        temp.next = null;
        return head;
    }