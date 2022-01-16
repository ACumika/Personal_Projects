public class neighborhood
{
   private String name;
   private final String DEFAULT_NAME="Block 13";
   private firestation station;
   private house[] houses;
   private int nbrHouses;
   private final int MAX = 6;
 
   //Purpose: Need to construct a neighborhood object
   //assumptions: Inputs are of the proper data type
   //inputs: name - the name of the neighborhood
   //post conditions: A neighborhood object has been created   
   public neighborhood(String name)
   {
      this.name=strValid(name, DEFAULT_NAME);
      this.station=null;
      this.houses = new house[MAX];
      this.nbrHouses=0;
   }

   //Purpose: Need to construct a default neighborhood object
   //assumptions: None
   //inputs: None 
   //post conditions: A default neighborhood object has been created 
   public neighborhood()
   {
      this.name=DEFAULT_NAME;
      this.houses = new house[MAX];
      this.nbrHouses=0;
   }
   
   //Purpose: validate is the given string is not an empty string
   //assumptions: inputs are type String
   //inputs: parameter - a string that has to be validated
   //        defVal - default value of a given parameter
   //post conditions: returns the inuput string if its valid; if not valid returns default string
   private String strValid(String parameter, String defVal)
   {
      if (parameter.length()<=0)
         return defVal;
      else
         return parameter;
   }
   
   //Purpose: display the information about the neighborhood
   //assumptions: none 
   //input: none
   //post condition: the information about the neighborhood is displayed
   public void display()
   {  
      if (station==null)
         System.out.println(name+" neighborhood has no firestarion");
      else
         System.out.println(name+" neighborhood has firestarion with "+ station.getNumberBays()+" bays on street "+ station.getStreetName() + ", street number " + station.getStreetNumber() + ", year built "+station.getYearBuilt());
      if (nbrHouses==0)
         System.out.println(name+" neighborhood has no house");
      else
      {
         System.out.println(nbrHouses+" houses in "+name+" neighborhood:");
         diplayHouseArray(houses); 
      }      
   }
   
   //Purpose: update the station variable (attribute). Set the firestation in the neigborhood.
   //assumptions: parameter is a firestation data type
   //input: firest - the firestation object variable
   //post condition: the station variable is updated. Firestation is now in the neighborhood. 
   public void setFireStation (firestation firest)
   {
      this.station=firest;
   } 
      
   public boolean addHouse (house aHouse)
   {
      if (nbrHouses < MAX)
      {
         houses[nbrHouses]=aHouse;
         nbrHouses++;
         return true;
      }
      else
      {
         return false;
      }     
   }   
   
   private void diplayHouseArray(house[] houses)
   {
      for (int i=0; i<nbrHouses; i++)          
            System.out.println("House "+(i+1)+" has "+houses[i].getNumberBedrooms()+" bedrooms, "+houses[i].getNumberBathrooms()+" bathroooms. Adress: "+houses[i].getStreetNumber()+
            " "+houses[i].getStreetName()+" and it was build in "+houses[i].getYearBuilt()+" year."); 
   } 
}

//black/white for testing arrays - black - jsut to see if it works with houses. White see if it works without the houses, with one house, with 6 houses and with 7 houses??
