public class Square
{
   private double length;
   
   //Purpose: Need to construct a Square object
   //assumptions: None
   //inputs: None 
   //post conditions: A Square object has been created 
   public Square(double length)
   {
      this.length = length;
   }
   
   //Purpose: Return Area of the square for the given length of the square
   //assumptions: the lenght value is a valid value
   //inputs: lenght - lenght of the side of the square
   //post conditions: returns the area fo the square
   public double CalcAreaSquare()
   {
      double AreaSquare = Math.pow(this.length, 2.0); 
      return AreaSquare;
   }
}
