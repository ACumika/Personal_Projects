public class house extends building
{
   private double numberBathrooms;
   private int numberBedrooms; 
   private final double DEFAULT_BATHROOMS=2;
   private final int DEFAULT_BEDROOMS=4;
   
   //Purpose: Need to construct a house object
   //assumptions: Inputs are of the proper data type
   //inputs: numberBathrooms - number of bathrooms in the house
   //        numberBedrooms - number of bedroom in the house
   //        streetName - a name of the street that house stands on
   //        streetNumber - a street number of the house
   //        yearBuilt - a year in which the house was built
   //post conditions: A house object has been created   
   public house(double numberBathrooms, int numberBedrooms, String streetName, String streetNumber, int yearBuilt)
   {
      super(streetName, streetNumber, yearBuilt);
      this.numberBathrooms=isPositiveAndIncr(numberBathrooms, DEFAULT_BATHROOMS, 0.5);
      this.numberBedrooms=isInputNotNeg(numberBedrooms, DEFAULT_BEDROOMS);
   }
   
   //Purpose: Need to construct a default house object
   //assumptions: None
   //inputs: None 
   //post conditions: A default house object has been created 
   public house()
   {
      super();
      this.numberBathrooms=DEFAULT_BATHROOMS;
      this.numberBedrooms=DEFAULT_BEDROOMS;
   }
   
   //Purpose: Need to Return the number of bathrooms in the house
   //assumptions: None
   //inputs: None 
   //post conditions: returns the number of bathrooms  
   public double getNumberBathrooms()
   {
      return numberBathrooms;
   }

   //Purpose: Need to Return the number of bedrooms in the house
   //assumptions: None
   //inputs: None 
   //post conditions: returns the number of bedrooms  
   public int getNumberBedrooms()
   {
      return numberBedrooms;
   }

   //Purpose: validate the value to be greater than 0 and fractional value of given number
   //assumptions: inputs are of the proper Data type
   //inputs: parameter - parameter that has to be vaidated
   //        defVal - default value of that parameter
   //        fracVal - fractional value of the parameter to check
   //post conditions: if number not valid returns default number of bathrooms   
   private double isPositiveAndIncr(double parameter, double defVal, double fracVal)
   {
      if ( parameter % fracVal !=0 || parameter <= 0)
			return defVal;
		else
			return parameter;
   }
   
   //Purpose: validate if the given parameter is greater or equal to 0
   //assumptions: inputs are integers
   //inputs: paramter - parameter that has to be validated
   //        defVal - default value of that parameter
   //post conditions: returns the number of bathrooms 
   private int isInputNotNeg(int parameter, int defVal)
   {
      if (parameter<0)
         return defVal;
      else
         return parameter;
   }
   
}

