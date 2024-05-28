class Demo  {
    public static void main(String a[]){
        Student s1 = new Student("Aakash", 1, 9.98);
        Student s2 = new Student("Arun", 2, 9.99);
        s1.show();
        Student.show1(s2);
    }
}





class Student{
    String name;
    int rollNo;
    double gpa;
    static String designation;

    static{        // static block static variables will be initialized irrespective of objects created
        designation = "Student";
    }

    public Student(String name, int rollNO, double d){    // parameterized constructor
            this.name = name;
            this.rollNo = rollNO;
            this.gpa = d;
    }

    public void show(){
        System.out.println(name + " : " + rollNo + " : " + gpa + " : " + designation);
    }

    public static void show1(Student objStudent){    // difference between the static method and normal method is shown
        System.out.println(objStudent.name + " : " + objStudent.rollNo + " : " + objStudent.gpa + " : " + designation);
    }

}
