public class building
{
   private String streetName;
   private String streetNumber;
   private int yearBuilt;
   private final String DEFAULT_STREETNAME="Salt Springs Rd";
   private final String DEFAULT_STREETNUMBER="1419";
   private final int DEFAULT_YEARBUILT=1980;
   
   //Purpose: Need to construct a building object
   //assumptions: Inputs are of the proper data type
   //inputs: streetName - a name of the street that building stands on
   //        streetNumber - a street number of the building
   //        yearBuilt - a year in which the buiding was built
   //post conditions: A building object has been created 
   public building(String streetName, String streetNumber, int yearBuilt)
   {
      this.streetName=strValid(streetName, DEFAULT_STREETNAME);
      this.streetNumber=strValid(streetNumber, DEFAULT_STREETNUMBER);
      this.yearBuilt=rangeValid(2019, 1975, yearBuilt, DEFAULT_YEARBUILT);
   }
   
   //Purpose: Need to construct a default building object
   //assumptions: None
   //inputs: None 
   //post conditions: A default building object has been created   
   public building()
   {
      this.streetName=DEFAULT_STREETNAME;
      this.streetNumber=DEFAULT_STREETNUMBER;
      this.yearBuilt=DEFAULT_YEARBUILT;
   }
   
   //Purpose: Need to Return the name of the street
   //assumptions: None
   //inputs: None 
   //post conditions: returns the name of the street 
   public String getStreetName()
   {
      return streetName;
   }
   
   //Purpose: Need to Return the number of the street 
   //assumptions: None
   //inputs: None 
   //post conditions: returns the number of the street
   public String getStreetNumber()
   {
      return streetNumber;
   }
   
   //Purpose: Need to Return the year the building was built
   //assumptions: None
   //inputs: None 
   //post conditions: returns the year of build
   public int getYearBuilt()
   {
      return yearBuilt;
   }
   
   //Purpose: validate is the given string is not an empty string
   //assumptions: inputs are type String
   //inputs: parameter - a string that has to be validated
   //        defVal - default value of a given parameter
   //post conditions: returns the number of bathrooms
   private String strValid(String parameter, String defVal)
   {
      if (parameter.length()<=0)
         return defVal;
      else
         return parameter;
   }
   
   //Purpose: validate if the value is within the range specified
   //assumptions: inputs are integers
   //inputs: max - maximum value allowed 
   //        min - minimum value allowed
   //        parameter - parameter that has to be validated
   //        defVal - default value of a given parameter
   //post conditions: returns the number of bathrooms
   private int rangeValid(int max, int min, int parameter, int defVal)
   {
      if (parameter<min || parameter>max)
         return defVal;
      else
         return parameter;
   }
}