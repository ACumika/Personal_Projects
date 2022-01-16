public class counter
{
   private int[] counterStore;
   private String[] strStore;
   private int cases=3;

   //Purpose: Need to construct a default counter object
   //assumptions: None
   //inputs: None 
   //post conditions: A default counter object has been created    
   public counter()
   {
      this.strStore = new String[cases];
   }
   
   //Purpose: Convert the string so that all characters are lowercase 
   //assumptions: input is a string type  
   //inputs: str - a string that has to be converted
   //post conditions: returns a string with all characters lowercase   
   private String lowerCaseConvert(String str)
   { 
      String lowerCaseStr=str.toLowerCase(); 
      return lowerCaseStr;
   }

   //Purpose: counts how many times a specific character appears in the imput string
   //assumptions: indexComp imput is an int type and other inputs are string type
   //inputs: inputStr - a string that we study to count the frequency of the character
   //        compStr - a reference string from which we take the character we want to count in the imput string
   //        indexComp - an index of the character in comp Str that we want to count in input sting
   //post conditions: returns the frequncy of how many times the character appeard in the input string.  
   private int compare(int indexComp, String inputStr, String compStr)
   {
      int count=0; 
      for(int idx=0;idx<inputStr.length();idx++)
      {
         if (compStr.charAt(indexComp)==inputStr.charAt(idx))
            count=count+1;
      }
      return count;
   }
   
   //Purpose: build an array of the frequancies of characters in input string
   //assumptions: inputs are of a string type   
   //inputs: input - a string that we study to count frequencies of the characters
   //        comp - a reference string that stores characters that we are counting in input string 
   //post conditions: an array with character frequencies has been created   
    private void buildCounterArray(String input, String comp)
    {
       String inputStr=lowerCaseConvert(input);
       for (int i=0;i<comp.length();i++)
          counterStore[i]=compare(i, inputStr, comp);
    }    
  
   //Purpose: Need to create an array of reference strings cases
   //assumptions: None
   //inputs: None 
   //post conditions: case array has been created
   public void buildCaseArray()
   {
      strStore[0] = "abcdefghijklmnopqrstuvwxyz";
      strStore[1] = " !@#$%^&*()_+-=[];'./,<>?:{}`~";
      strStore[2] = "\n"; 
   }

   //Purpose: display the frequencies of characters stored in the counterArray for specific input string and case string
   //assumptions: inputs are string type  
   //inputs: input - a string that we study to count frequencies of the characters
   //        comp - a reference string that stores characters that we are counting in input string 
   //post conditions: characters and its frequanceis in the input string are displayed
   private void displayCounterStore(String input, String comp)
   {
      this.counterStore = new int[comp.length()];
      buildCounterArray(input, comp);
      if (comp.length()==1)
         System.out.println(counterStore[0]);
      else
      {
         for (int i=0;i<comp.length();i++)
            if (counterStore[i]>0)
               System.out.println(comp.charAt(i)+"      "+counterStore[i]);
      }
   }  
  
   //Purpose: display the information about the frequancies of characters in the input sting for all the cases
   //assumptions: input is string type 
   //inputs: input - a string that we study to count frequencies of the characters
   //post conditions: the information about the character frequency in the input string is displayed   
   public void displayInfo(String input)
   {
      System.out.print("Number of lines in A Dream Within a Dream.txt is ");
      displayCounterStore(input, strStore[2]);
      System.out.println("Letter frequencies are as follows:");
      System.out.println("Char   Freq");
      displayCounterStore(input, strStore[0]);
      System.out.println("");
      System.out.println("Punctuation & space frequencies are as follows:");
      System.out.println("Char   Freq");
      displayCounterStore(input, strStore[1]);
   }   
 }
       
    
      
            
         
      