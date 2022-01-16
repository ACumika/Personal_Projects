import java.util.Scanner;

public class Assignment3_methods
{
   Scanner scan;
   
   //Purpose: Need to construct a Assignment3_method_Obj object.
   //assumprions: None.
   //imputs: None.
   //Post conditions: A Assignment_methods_Obj has been created
   public Assignment3_methods()
   {
      scan = new Scanner(System.in);
   }
   
   //Purpose: Execute the Assignment3 program
   //Assumptions: User is ready to enter lenght of the square and diameter of the circle
   //Inputs: None
   //Post Condition: Displays the area of the square and the circle, as well as the percentage that the smaller computed area is of the larger computed area
   public void go()
   {
      double length = getValidInput("Enter the lenght of the square in meters: ", 0);   
      double diameter = getValidInput("Enter the diameter of the circle in meters: ", 0);
      
      Square sqr = new Square(length); 
      Circle crc = new Circle(diameter);
      Percentage perc = new Percentage(sqr.CalcAreaSquare(), crc.CalcAreaCircle());
      System.out.println("The area of the square is " + sqr.CalcAreaSquare() + " m^2");
      System.out.println("The area of the circle is " + crc.CalcAreaCircle() + " m^2");
      System.out.println("The percentage that the smaller computed area is of the larger computed area is " + perc.CalcPercentageArea());
   }
   
   //Purpose: Obtain a valid input from user
   //Assumptions: input is entered. Input has to be validated to be greater than min
   //Input: prompt - text that user sees if input is not valid
   //       min - min value for the input
   //Post Conditions: return validated input
   private double getValidInput (String prompt, double min)
   {
      double numInp = getNumber(prompt);
      while (! isInputValid(numInp, min))
      {
         System.out.println("Number must be greater than " + min);
         numInp = getNumber(prompt);
      }
      return numInp;
   }   
      
   //Purpose: Obtain a number from a user
   //Assumptions: User ready to enter a number
   //Inputs: prompt - text displayed to a user before he/she enters the number
   //Post conditions: Returns the number entered by user
   private double getNumber(String prompt)
   {
      double num=-1;
      try
      {
         System.out.print(prompt);
         num=scan.nextDouble();
      }
      catch (Exception ex)
      {
         scan.nextLine(); //skip past the data entered by user
      }
      return num;
   }
   
   //Purpose: Validate a number entered by user
   //Assumptions: input has to be validated to be inside the range of (min, max)
   //inputs: userInput - number entered by user
   //        min - userInput must be > min
   //post condition: Returns true when userInput is within the range of (min,max]. Otherwise, returns false. 
   private boolean isInputValid(double userInput, double min)
   {
      if (userInput > min)
         return true;
      else
         return false;
   }
}


//I wrote this test before you said that we do not need it. So I will just keep it... 
//Test
//Lengh input = 5, Diameter input = 3           Expect: The area of the square is 25.0 m^2
//                                                    The area of the circle is 28.274333882308138 m^2
//                                                    The percentage that the smaller computed area is of the larger computed area is 0.8841941282883075
//Lengh input = 1.2, Diameter input = 3.5       Expect: The area of the square is 1.44 m^2
//                                                    The area of the circle is 38.48451000647496 m^2
//                                                    The percentage that the smaller computed area is of the larger computed area is 0.037417651926910905
//Lengh input = -2                            Expect: Lengh of the square must be greater then 0
//                                                    Re-enter the lengh in meters
//Lengh input = 3, Diameter input = -2          Expect: Diameter of the circle must be greater then 0
//                                                    Re-enter the diameter in meters
//Lengh input = 0                             Expect: Lengh of the square must be greater then 0
//                                                    Re-enter the lengh in meters
//Lengh input = 4, Diameter input = 0           Expect: Diameter of the circle must be greater then 0
//                                                    Re-enter the Diameter in meters