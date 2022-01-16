public class Assignment5_main
{

   //Purpose: need to create a assignment5_main object and run the test method
   //assumptions: None
   //inputs: None 
   //post conditions: assignment5_main object, test runs
public static void main(String[] args)
   {
      Assignment5_main com = new Assignment5_main();
      com.testBlack();
      com.testWhite();
   }
   
   //Purpose: perform black box testing
   //assumptions: None
   //inputs: None 
   //post conditions: Prints out test cases  
   public void testBlack()
   {
      house com = new house();
      print(com, "Default", "2, 4, Salt Springs Rd, 1419, 1980");
      com = new house(4,8,"Maskavas", "271", 1999);
      print(com, "4, 8, Maskavas, 271, 1999", "4, 8, Maskavas, 271, 1999");
   }
   
   //Purpose: perform white box testing
   //assumptions: None
   //inputs: None 
   //post conditions: Prints out test cases 
   public void testWhite()
   {
      house com = new house(-1,-1,"","",1974);
      print(com, "-1, -1, , ,1974","2, 4, Salt Springs Rd, 1419, 1980");
      com = new house(0,0,"G","1",1975);
      print(com, "0, 0, G, 1, 1975","2, 0, G, 1, 1975");
      com = new house(1,1,"G","1",2019);
      print(com, "1, 1, G, 1, 2019","1, 1, G, 1, 2019");
      com = new house(2.5, 1,"G","1",2020);
      print(com, "2.5, 1, G, 1, 2020","2.5, 1, G, 1, 1980");
      com = new house(2.4,1,"G","1",2000);
      print(com, "2.4, 1, G, 1, 2000","2, 1, G, 1, 2000");
      com = new house(2.6,1,"G","1",2000);
      print(com, "2.6, 1, G, 1, 2000","2, 1, G, 1, 2000");
      com = new house(0.5,1,"G","1",2000);
      print(com, "0.5, 1, G, 1, 2000","0.5, 1, G, 1, 2000");   
      com = new house(0.99,1,"G","1",2000);
      print(com, "0.99, 1, G, 1, 2000","2, 1, G, 1, 2000");  
   }
   
   //Purpose: need to reate a assignment5_main object and run the test method
   //assumptions: None
   //inputs: None 
   //post conditions: assignment5_main object, test runs
   private void print(house object, String input, String expected)
   {
      System.out.println("Input: " + input + " Expected: "+ expected + " Recieved: " + object.getNumberBathrooms()+", "+ object.getNumberBedrooms()+", "+object.getStreetName()+", "+object.getStreetNumber()+", "+object.getYearBuilt());
   }
   
}
