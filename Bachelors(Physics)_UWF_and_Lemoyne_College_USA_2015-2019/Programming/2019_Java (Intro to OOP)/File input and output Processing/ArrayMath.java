public class ArrayMath
{
   private int [] eachLineSum;
   private final int MAX = 20;  
   private Object [][] arrayCalc; 
   
   public ArrayMath()
   {
      tokenStore ts = new tokenStore();
      this.eachLineSum = eachLineSum[MAX];
      this.arrayCalc = ts.store;
   }
   
   public void createLineSumArray()
   {
      int sum;
      for(int row=0;row<arrayCalc.length; row++)
      {
         sum=0;
         for(int col=0; col < store[row].length;col++)
         {
            sum=sum+arrayCalc[row][col].length();
         }
         eachLineSum[row]=sum;
      }
   }
   
   public void display1D()
   {
      for(int i=0;i<MAX;i++)
      {
          System.out.println("token: "+eachLineSum[i]);
      }
   }
}
            
      
      
   
   