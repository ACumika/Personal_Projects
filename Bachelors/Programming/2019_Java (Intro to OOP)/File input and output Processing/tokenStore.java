public class tokenStore
{
   public String [][] store;
   public final int ROWMAX = 20;
   public final int COLMAX = 12;
   private int [] eachLineSum;
   private int [] eachLineMult;
   private int lineCount;
   
   //Purpose: Need to construct a default tokenStore object
   //assumptions: None
   //inputs: None 
   //post conditions: A default tokenStore object has been created  
   public tokenStore()
   {
      this.store = new String[ROWMAX][COLMAX];
      this.eachLineSum = new int[ROWMAX];
      this.eachLineMult = new int[ROWMAX];
   }
   //Purpose: Build a token 2D array with the tokens from the Input string 
   //assumptions: input is a string type
   //inputs: txt - a string from which we create an array
   //post conditions: a 2D array has been build.   
   public void buildToken2DArray(String txt)
   {
      String [] lineStore=txt.split("\n");
      lineCount=lineStore.length;
      for (int i=0; i < lineCount;i++)
      {
         String [] arr = breakLineInTokens(lineStore[i]);
         for (int k=0; k<arr.length; k++)
         {
            store[i][k]=arr[k];     
         }
      }
   }
  
   //Purpose: break the text line into an array of tokens
   //assumptions: input is a string type that has ony one line 
   //inputs: line - a line from which we build an array of tokens
   //post conditions: an array of tokens built  
   public String [] breakLineInTokens(String line)
   {
     String strComp;
     String [] arrayStr = line.split(" ");
     strComp="";
     for(int i=0;i<arrayStr.length;i++)
     { 
        if (arrayStr[i].equals(""))
           strComp = strComp.concat(arrayStr[i]);
        else 
        {
           strComp = strComp.concat(arrayStr[i]);
           strComp = strComp.concat(" ");
        }
     }
     arrayStr = strComp.split(" ");
     return arrayStr;
   }      
   
   //Purpose: build an array when each entry is a sum of length of tokens in each line
   //assumptions: None
   //inputs: None 
   //post conditions: an array with sums built 
   public void createLineSumArray()
   {
      int sum;
      for (int row=0; row < ROWMAX;row++)
      {
         sum=0;
         for(int col=0; col < COLMAX;col++)
         {
            if (store[row][col] != null)
               sum=sum+store[row][col].length();
            else
               sum=sum+0;
         }
         eachLineSum[row]=sum;
      }
   } 

   //Purpose: build an array where each entry is a multiplication of number of tokens by the sum of the length of the tokens for a line
   //assumptions: None
   //inputs: None 
   //post conditions: an array of products is built  
   public void createLineMultArray()
   {
      int mul;
      int count;
      for (int row=0; row < ROWMAX;row++)
      {
         mul=1;
         count=0;
         for(int col=0; col < COLMAX;col++)
         { 
           if (store[row][col] != null)
              count=count+1;
         }
         mul=eachLineSum[row]*count;
         eachLineMult[row]=mul;
      }
   }
   
   //Purpose: write the tokens from the 2d arary, their sum and product of token numbers and their sum to the file
   //assumptions: Input is type TextOuput
   //inputs: to - an object for a TextOuput class 
   //post conditions: text is written to the file 
   public void writeText(TextOutput to)
   {
      for (int row=0; row < lineCount;row++)
      {
         for(int col=0; col < COLMAX;col++)
         {
            if (store[row][col] != null)
            {
               to.writeToFile(store[row][col]);
               to.writeToFile(" ");
            }           
         }
            to.writeToFile(String.valueOf(eachLineSum[row]));
            to.writeToFile(" ");
            to.writeToFile(String.valueOf(eachLineMult[row]));
            to.writeToFile("\n");
      } 
   }
}
      