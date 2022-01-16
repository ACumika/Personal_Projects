public class main
{

   //Purpose: Need to create a main object and run the program
   //assumptions: None
   //inputs: None 
   //post conditions: main object created and program runs
	public static void main(String[] args)
	{
		main prg = new main();
		prg.run();
	}

   //Purpose: need to create counter and textInput objcts and display the information about the text document character frequencies
   //assumptions: None
   //inputs: None 
   //post conditions: an information about the charactersfrequencies in the text document is displayed  
   private void run()
   {
      textInput tx = new textInput();
      counter cr = new counter();
      String str = tx.buildStr();
      cr.buildCaseArray();
      cr.displayInfo(str);   
      tx.closeFile();  
   } 
  
}


