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
   public void run()
   {
      textInput tx = new textInput("LinesOfTokens.txt");
      tokenStore ts = new tokenStore();      
      TextOutput to = new TextOutput("Token New List.txt");
      String str = tx.buildStr();
      ts.buildToken2DArray(str);
      ts.createLineSumArray();
      ts.createLineMultArray();     
      ts.writeText(to);
      to.closeOutFile();
      tx.closeFile();    
   }
}
  