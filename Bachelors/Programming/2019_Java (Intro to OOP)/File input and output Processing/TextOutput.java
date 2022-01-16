import java.io.PrintWriter;
import java.io.File;

public class TextOutput
{
   private String fileName;
   private PrintWriter outFile;
   
   //Purpose: Need to construct a TextOuput object
   //assumptions: input is type string 
   //inputs: fileName - name of the file that we want to create and open. 
   //post conditions: A TextOutput object has been created  
   public TextOutput(String fileName)
   {
      this.fileName = fileName;
      this.outFile = tryWriteFile();  
   }

   //Purpose: have to validate if we can create and write in the file
   //assumptions: None
   //inputs: None 
   //post conditions: returns PrintWriter type variable outFile that stores information about the file
   public PrintWriter tryWriteFile()
   {
      try
      {
         outFile = new PrintWriter(fileName);
      }
      catch (Exception Ex)
      {
         System.out.println("Can't write in file");
      }
      return outFile;
   }

   //Purpose: write the passed string into the file
   //assumptions: input is type string 
   //inputs: str - a text that has to be written in the file
   //post conditions: str text is written in file    
   public void writeToFile(String str)
   {
      outFile.print(str);
   }
  
   //Purpose: Need to close a file
   //assumptions: file is open
   //inputs: None 
   //post conditions: an out file is closed  
   public void closeOutFile()
   {
      outFile.close();
   }
}