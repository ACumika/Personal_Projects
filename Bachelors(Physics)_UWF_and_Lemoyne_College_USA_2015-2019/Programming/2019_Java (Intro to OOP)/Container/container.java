import java.math.BigDecimal;

public class container
{ 
   private BigDecimal[] numbers;
   private final int MAX = 7;
   private int nbrDecimals;

   //Purpose: Need to construct a default container object
   //assumptions: None
   //inputs: None 
   //post conditions: A default container object has been created    
   public container()
   {
      this.nbrDecimals = 0;
      this.numbers = new BigDecimal[MAX];
   }  
   
   //Purpose: add the object to the array
   //assumptions: passed parameter is of a proper data type
   //inputs: deci - an object(number) that has to be added
   //post conditions: returns true if object was added; returns false if max reached and object was not added
   public boolean addObject(BigDecimal deci)
   {
      if (nbrDecimals < MAX)
      {
         numbers[nbrDecimals]=deci;
         nbrDecimals++;
         return true;
      }     
      else
         return false;
   } 
   
   //Purpose: display an array of BigDecimals
   //assumptions: none
   //inputs: None 
   //post conditions: if no numbers in array- displays that, otherwise displays array objects on one line  
   public void displayBigDecimal()
   {
      if (nbrDecimals==0)
            System.out.print("No numbers in array");
      else
      {
         for (int i=0; i<nbrDecimals; i++)
            System.out.print(numbers[i]+" ");
      }
      System.out.println("");
   }
   
   //Purpose: return the smallest number in array
   //assumptions: None
   //inputs: None 
   //post conditions: a smallest number in array returned
   public BigDecimal returnSmallest()
   {
      BigDecimal deci=null;
      if (nbrDecimals==0)
         deci = null;
      else if (nbrDecimals==1)
         deci = numbers[0];
      else
         deci = returnSmallestHelper(numbers[0], 0);
      return deci;
   }   

   //Purpose: need a recursive logic for return smallest
   //assumptions: an array has at least one number. inputs of a proper type. first passed n is a first number of array
   //inputs: n - object of an array
   //        idx - index of a object in array that n is compared to 
   //post conditions: a smallest number in array returned   
   private BigDecimal returnSmallestHelper(BigDecimal n, int idx)
      {
         if (idx==nbrDecimals)
            return n;
         else if (n.compareTo(numbers[idx])==-1) 
         { 
            return returnSmallestHelper(n, idx+1);
         }
         else
            n=numbers[idx];
            return returnSmallestHelper(numbers[idx],idx+1);
      }
}



                        

         