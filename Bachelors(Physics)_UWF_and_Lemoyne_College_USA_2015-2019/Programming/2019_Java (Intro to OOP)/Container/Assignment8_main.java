import java.util.Scanner;
import java.math.BigDecimal;

public class Assignment8_main
{
   private Scanner scan;

   //Purpose: need to create a assignmen8_main object and run the test methods
   //assumptions: None
   //inputs: None 
   //post conditions: assignment8_main object, test runs
   public static void main(String[] args)
   {
      Assignment8_main com = new Assignment8_main();
      com.testNoInput();
      com.test1Input();
      com.test2Input();
      com.test7Input();
      com.test8Input();
      
   }
   
   //Purpose: Need to construct a construct Assignment8_main object to create scanner object
   //assumptions: scan variable declared
   //inputs: no input
   //post conditions: A scanner object has been created   
   private Assignment8_main()
   {
      this.scan = new Scanner(System.in);
   }

   //Purpose: perform No input testing
   //assumptions: None
   //inputs: None 
   //post conditions: displays that there is no numbers in array 
   private void testNoInput()
   {
      System.out.println("No Input Testing");
      container cont = new container();
      cont.displayBigDecimal();
      displaySmallest(cont);
   }
   
   //Purpose: perform 1 input testing
   //assumptions: None
   //inputs: None 
   //post conditions: displays numbers in array and the smallest number
   private void test1Input()
   {    
      System.out.println("1 Input Testing");
      container cont = new container();
      wasObjectAdded(cont);
      cont.displayBigDecimal();
      displaySmallest(cont);
   }

   //Purpose: perform 2 input testing
   //assumptions: None
   //inputs: None 
   //post conditions: displays numbers in array and the smallest number   
   private void test2Input()
   {   
      System.out.println("2 Input Testing");
      container cont = new container();
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      cont.displayBigDecimal();
      displaySmallest(cont);
   }
   
   //Purpose: perform 7 input testing
   //assumptions: None
   //inputs: None 
   //post conditions: displays numbers in array and the smallest number   
   private void test7Input()
   {   
     System.out.println("7 Input Testing");
      container cont = new container();
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      cont.displayBigDecimal();
      displaySmallest(cont);
   }

   //Purpose: perform 8 input testing
   //assumptions: None
   //inputs: None 
   //post conditions: prints that max reached. displays 7 numbers in array and the smallest number  
   private void test8Input()
   {
      System.out.println("8 Input Testing");
      container cont = new container();
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      wasObjectAdded(cont); 
      wasObjectAdded(cont);
      wasObjectAdded(cont);
      cont.displayBigDecimal();
      displaySmallest(cont);     
   }   

   //Purpose: display the smallest number in array
   //assumptions: passed parameter is container data type
   //inputs: cont - a container object
   //post conditions: displays smallest number . If no numbers displays:there is no numbers in the array. Therefore there is no smallest number
   private void displaySmallest(container cont)
   {
      if (cont.returnSmallest()==null)
         System.out.println("there is no numbers in the array. Therefore there is no smallest number");
      else 
         System.out.println("smallest number is: " +cont.returnSmallest());
   }

   //Purpose: add the object and print weather the object was added or not
   //assumptions: passed parameter is container data type
   //inputs: cont - a container object
   //post conditions: adds the object and displays if the object was added or not (in case of owerflow)  
      private void wasObjectAdded(container cont)
   {
      if (cont.addObject(getBigDecimal())==false)
         System.out.println("No object added. Max reached");
      else
         System.out.println("number added to array");
   }  

   //Purpose: get data from user
   //assumptions: passed parameter is string data type
   //inputs: prompt - text that is displayed to a user
   //post conditions: returns data entered by user
   private String getUserData(String prompt)
	{
		String data;
		System.out.print(prompt);
		data = scan.nextLine();
		return data;
	} 

   //Purpose: transled the user entered data to BidDecimal type
   //assumptions: passed parameter is string data type
   //inputs: userData - data that has to be translated
   //post conditions: returns the BigDecimal type data
   private BigDecimal translateUserData(String userData)
	{
		BigDecimal deci;
		try
		{
         deci = new BigDecimal(userData);
		}
		catch (Exception ex)
		{
			deci = null;
		}
		return deci;
	}

   //Purpose: Make sure user enters a real number
   //assumptions: no assumptions
   //inputs: no inputs
   //post conditions: if user does not enters real number, keeps asking to enter a real number. One number entered - returns that number(translated to BigDecimal)
   private BigDecimal getBigDecimal()
	{
		BigDecimal n=null;
		boolean invalid = true;
		//final int INVALID = Integer.MIN_VALUE; - what is that for? 
		do
		{
			String userData = getUserData("Enter a real number: ");
			BigDecimal nbr = translateUserData(userData);
			if (nbr == null)
				System.out.println("Did not enter a real number.");
			else
			{
				invalid = false;
				n = nbr;
			}
			
		} while (invalid);
		return n;
	} 
}

/*
Test Comeents:
Input testing: 
Input 1                    Expect: number added to array
Input 1.1                  Expect: number added to array
Input 1.3213546873214387   Expect: number added to array
Input 13544684354684354357 Expect: number added to array
Input -53434394343654534   Expect: number added to array
Input -0.1                 Expect: number added to array
Input 0                    Expect: number added to array
Input -0.00001             Expect: number added to array
Input g                    Expect: Did not enter a real number
Input two                  Expect: Did not enter a real number
Input 34.6.5               Expect: Did not enter a real number
Input 2*4                  Expect: Did not enter a real number
Input 2^3                  Expect: Did not enter a real number

Array testing:
Before input               Expect: for displayBigDecimal - No numbers in array. 
                              for returnSmallest - No numbers in array, therefore there is no smallest number
Input 1                    Expect: for displayBigDecimal - 1 
                              for returnSmallest - Smallest number is 1
Input 0                    Expect: for displayBigDecimal - 0 
                              for returnSmallest - Smallest number is 0
Input -0.01                Expect: for displayBigDecimal - -0.01
                              for returnSmallest - Smallest number is -0.01
Input 1254685221458245655756973213646532133 1  Expect: for displayBigDecimal - 1254685221458245655756973213646532133 1
                                               for returnSmallest - Smallest number is 1
Input 1 0                  Expect: for displayBigDecimal - 1 0
                              for returnSmallest - Smallest number is 0   
Input 1 0 -0.1             Expect: for displayBigDecimal - 1 0 -0.1
                              for returnSmallest - Smallest number is -0.1
Input 1 9 -66 5 1254 -5.6 1 Expect: for displayBigDecimal - 1 9 -66 5 1254 -5.6 1
                              for returnSmallest - Smallest number is -66
Input -1 9 5 5 1254 7 45    Expect: for displayBigDecimal - -1 9 5 5 1254 7 45
                              for returnSmallest - Smallest number is -1
Input 1 2 5 1 6 1 5         Expect: for displayBigDecimal - 1 2 5 1 6 1 5
                              for returnSmallest - Smallest number is 1
Input 1 2 5 5.5 6.234 0 3 1  Expect: No object added. Max Reched.
                              for displayBigDecimal - 1 2 5 5.5 6.234 0 3 
                              for returnSmallest - Smallest number is 0
                              
   
*/                                                                                                                                                                            