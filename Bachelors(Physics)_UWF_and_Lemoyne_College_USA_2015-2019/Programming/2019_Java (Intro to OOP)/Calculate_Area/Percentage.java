public class Percentage
{
   private double percentage;
   
   //Purpose: Need to construct a Percentage object
   //assumptions: None
   //inputs: None                     
   //post conditions: A Percentage object has been created 
   public Percentage(double value1, double value2)
   {
      this.percentage = value1/value2;
   }
   
   //Purpose: Determine The percentage that the smaller computed area is of the larger computed area
   //assumptions: the Area values are valid values
   //inputs: AreaCircle - The area of the circle
   //        AreaSquare - the area of the square
   //post conditions: returns the percentage that the smaller computed area is of the larger computed area.   
   public double CalcPercentageArea()
   {
      double Perc=0;
      if (this.percentage < 1)
         Perc = this.percentage;
      else
         Perc = Math.pow(this.percentage, -1.0);
      return Perc;
   }
}