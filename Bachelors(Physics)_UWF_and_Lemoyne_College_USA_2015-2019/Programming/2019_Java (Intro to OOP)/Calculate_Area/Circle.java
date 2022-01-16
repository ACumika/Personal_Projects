public class Circle
{
   private double diameter;
   
   //Purpose: Need to construct a Circle object
   //assumptions: None
   //inputs: None 
   //post conditions: A Circle object has been created 
   public Circle(double diameter)
   {
      this.diameter = diameter;
   }
   
   //Purpose: Return Area of the circle for the given diameter of the circle
   //assumptions: the diameter value is a valid value
   //inputs: diameter - diameter of the of the circle
   //post conditions: returns the area fo the circle
   public double CalcAreaCircle()
   {
      double AreaCircle = Math.PI*Math.pow(this.diameter/2, 2.0);
      return AreaCircle;
   }

}