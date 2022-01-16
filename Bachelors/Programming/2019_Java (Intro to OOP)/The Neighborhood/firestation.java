public class firestation extends building
{
   private int numberBays;
   private final int DEFAULT_BAYS=2;
   
   //Purpose: Need to construct a firestation object
   //assumptions: Inputs are of the proper data type
   //inputs: numberBays - number of bays in the firestation
   //        streetName - a name of the street that firestation stands on
   //        streetNumber - a street number of the firestation
   //        yearBuilt - a year in which the firestation was built
   //post conditions: A firestation object has been created   
   public firestation(int numberBays, String streetName, String streetNumber, int yearBuilt)
   {
      super(streetName, streetNumber, yearBuilt);
      this.numberBays=isPositive(numberBays, DEFAULT_BAYS);
   }
   
   //Purpose: Need to construct a default firestation object
   //assumptions: None
   //inputs: None 
   //post conditions: A default firestation object has been created 
   public firestation()
   {
      super();
      this.numberBays=DEFAULT_BAYS;
   }
   
   //Purpose: Need to Return the number of bays at the firestation
   //assumptions: None
   //inputs: None 
   //post conditions: returns the number of bays 
   public int getNumberBays()
   {
      return numberBays;
   }


   //Purpose: validate the value to be greater than 0
   //assumptions: inputs are of the proper Data type
   //inputs: parameter - parameter that has to be vaidated
   //        defVal - default value of that parameter
   //post conditions: if number not valid returns default number of bathrooms   
   private int isPositive(int parameter, int defVal)
   {
      if (parameter <= 0)
			return defVal;
		else
			return parameter;
   }
   
}

