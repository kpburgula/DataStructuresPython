public class temp{

  public static int temp(int value){
    if (value <= 0){
      return 0;
    }
    else{
      System.out.println(value);
      temp(value - 1);
    }
    return 0;
  }

  public static void main(String[] args){

    temp(10);
  }
}