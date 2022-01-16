public class Assignment7_main
{

   //Purpose: need to create a assignment6_main object and run the test method
   //assumptions: None
   //inputs: None 
   //post conditions: assignment6_main object, test runs
public static void main(String[] args)
   {
      Assignment7_main com = new Assignment7_main();
      com.testBlack();
      com.testWhite();
   }
   
   //Purpose: perform black box testing
   //assumptions: None
   //inputs: None 
   //post conditions: Prints out test cases  
   public void testBlack()
   {
      System.out.println("Black Testing: ");
      neighborhood hood = new neighborhood();
      firestation stat = new firestation();
      house house1 = new house();
      print("DEFAULT", "Block 13, no firestation, no house");
      hood.display();
      hood.setFireStation(stat);
      wasHouseAdded(hood,house1);
      print("DEFAULT", "2 bays, Salt Springs rd, 1419, 1980, 1 house in array - default one");
      hood.display();
      
      hood = new neighborhood("Riga");
      stat = new firestation(4,"Maskavas", "271", 2002);
      house1 = new house();
      print("Riga, 4 bays, Maskavas 271, 2002","Riga, no firestation, no house");
      hood.display(); 
      hood.setFireStation(stat);
      wasHouseAdded(hood,house1);
      print("Riga, has firestation, 1 house added", "Riga, 4 bays, Maskavas 271, 2002. 1 house in array - default.");
      hood.display();       
      house house2 = new house(5, 9, "Pavasara", "6", 2000);
      wasHouseAdded(hood,house2);
      print("Riga, has firestation, 2 houses added", "Riga, 4 bays, Maskavas 271, 2002. 2 house in array - default and 9,5 Pavasara 6, 2000");
      hood.display();
   }
   
   //Purpose: perform white box testing
   //assumptions: None
   //inputs: None 
   //post conditions: Prints out test cases 
   public void testWhite()
   {
      System.out.println("White Testing: ");
      neighborhood hood = new neighborhood("Syracuse");
      firestation stat = new firestation(1,"Rd","1",2000);
      house house1 = new house();
      house house2 = new house(1,2,"Str","2",1999);
      house house3 = new house(4,5,"Str","3",1999);
      house house4 = new house(5,3,"Str","4",1999);
      house house5 = new house(1,2,"Str","5",1999);
      house house6 = new house(1,2,"Str","6",1999);
      house house7 = new house(1,2,"Str","7",1999);
      hood.setFireStation(stat);
      print("Syracuse, has firestation, no house", "Syracuse, 1 bay, 1 Rd 2000 firestation, no house");
      hood.display();
      wasHouseAdded(hood, house1);
      print("Syracuse, Riga, has firestation, 1 house added", "Syracuse, 1 bay, 1 Rd 2000 firestation, 1 default house");
      hood.display();
      wasHouseAdded(hood, house2);
      wasHouseAdded(hood, house3);
      wasHouseAdded(hood, house4);
      wasHouseAdded(hood, house5);
      wasHouseAdded(hood, house6);
      print("Syracuse, has firestation, 6 houses added", "Syracuse, 1 bay, 1 Rd 2000 firestation, 6 houses");
      hood.display();
      wasHouseAdded(hood, house7);
      print("Syracuse, has firestation, 7 house added", "Syracuse, 1 bay, 1 Rd 2000 firestation, No houses added - has total 6 houses");
      hood.display();     
      
      hood = new neighborhood("");
      hood.display();
      hood = new neighborhood("G");
      hood.display();
   }
   
   //Purpose: print out the input and expected values
   //assumptions: input parameters are string data type
   //inputs: input - a string that shows the input for the test case
   //        expected - a string that shows what is an expected output for the test case
   //post conditions: input and expected values are printed
   private void print(String input, String expected)
   {
      System.out.println("");
      System.out.println("Input: " + input + " Expected: "+ expected);
   }   
   
   private void wasHouseAdded(neighborhood hood,house aHouse)
   {
      if (hood.addHouse(aHouse)==false)
         System.out.print("No house added. Max reached");
   }      
}

// for (int i=0; i<nbrHouses; i++)
           // System.out.println("House "+i+" has "+aHouse.getNumberBedrooms()+" bedrooms, "+ahouse.getNumberBathrooms()+" bathroooms"); 