import java.util.Scanner;
import java.io.File;

public class textInput
{

   private String fileName;
   private Scanner inFile;

   //Purpose: Need to construct a textInput object
   //assumptions: input is type string
   //inputs: fileName - a name of the file that we want to open
   //post conditions: A textInput object has been created  
   public textInput(String fileName)
   {
      this.fileName = fileName;
      this.inFile = tryScanFile();
   }

   //Purpose: have to validate if the file exists and we scan it
   //assumptions: None
   //inputs: None 
   //post conditions: returns the Scanner type vairable inFile that stores the information from the file scanned
   public Scanner tryScanFile()
   {
      try
      {
         inFile = new Scanner(new File(fileName));
      }
      catch (Exception Ex)
      {
         System.out.println("File not found");
      }
      return inFile;
   }

   //Purpose: Build the string from the text in the file
   //assumptions: file is txt format and contains text
   //inputs: None 
   //post conditions: returns a string of the text from the file 
   public String buildStr()
   {
      String str="";
      while (inFile.hasNext())
      {
         String line = inFile.nextLine();//repeatative?
         str = str.concat(line);
         str = str.concat("\n");//to have same text as in file, so each line ther is, so I can count lines
      }
      return str;
   }
   
   public String returnNextLine()
   {
      String line="";
      if (inFile.hasNext())
         line = inFile.nextLine();
      return line;
   } 
   //Purpose: Need to close the file we work with
   //assumptions: None
   //inputs: None 
   //post conditions: a file is closed  
   public void closeFile()
   {
      inFile.close();
   }
}

