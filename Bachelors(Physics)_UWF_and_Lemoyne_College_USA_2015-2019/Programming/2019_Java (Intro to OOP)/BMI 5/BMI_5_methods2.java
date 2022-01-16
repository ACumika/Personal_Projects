import java.util.Scanner;
import java.util.InputMismatchException;
import java.util.NoSuchElementException;

public class BMI_5_methods2
{
	private Scanner scan;

	//purpose: Need to construct a BMI_5_methods2 object.
	//assumptions: None.
	//inputs: None.
	//post-conditions: A BMI_5_methods2 object has been created.
	public BMI_5_methods2()
	{
		scan = new Scanner(System.in);
	}

	//purpose: Execute this BMI program.
	//assumptions: User ready to enter weight and height.
	//inputs: None.
	//post-conditions: Displays the BMI category corresponding to inputs.
	public void go()
	{
      double weight = getValidWeight();
      double height = getValidHeight();

		BMI_5_bmi bmi = new BMI_5_bmi(weight, height);
		System.out.println(" Your BMI category is " + bmi.getBMICategory());
	}

   private double getValidWeight()
   {
		double weight = getNumber("Enter your weight in pounds: ");
		while (! isInputValid(weight, 0, 1000))
		{
			System.out.println("Weight must be a number in range (0,1000]");
			weight = getNumber("Re-enter your weight in pounds: ");
		}
      return weight;
   }

   private double getValidHeight()
   {
		double height = getNumber("Enter your height in inches: ");
		while (! isInputValid(height, 0, 100))
		{
			System.out.println("Height must be a number in range (0, 100]");
			height = getNumber("Re-enter your height in inches: ");
		}
      return height;
   }

	//purpose: Obtain a number from the user.
	//assumptions: User ready to enter a number.
	//inputs: prompt - text displayed to user before user enters a number.
	//post-conditions: Returns number entered by user.
	private double getNumber(String prompt)
	{
		double num = -1;
		try
		{
			System.out.print(prompt);
			num = scan.nextDouble();
		}
		catch (Exception ex)
		{
			scan.nextLine();	//skip past the data entered by user.
		}
		return num;
	}

	//purpose: Validate a number entered by user.
	//assumptions: user input needs to be validated to be inside range  (min, max].
	//inputs: userInput - number entered by user.
	//			min - userInput must be > min.
	//			max - userInput must be <= max.
	//post-conditions: Returns true when min < userInput <= max. Otherwise, returns false.
	private boolean isInputValid(double userInput, double min, double max)
	{
		if (userInput > min && userInput <= max)
			return true;
		else
			return false;
	}
}
