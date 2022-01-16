public class BMI_5_bmi
{
	double bmi;

	//purpose: Need to construct a BMI_5_bmi object.
	//assumptions: None.
	//inputs: None.
	//post-conditions: A BMI_5_bmi object has been created.
	public BMI_5_bmi(double weight, double height)
	{
		this.bmi = weight / Math.pow(height,2.0) * 703;
	}

	//purpose: Return BMI category given a weight and height.
	//assumptions: weight and height are valid values.
	//inputs: weight - weight of person in pounds.
	//			height - height of person in inches.
	//post-conditions: Returns category that the BMI value corresponds to.
	public String getBMICategory()
	{
		String result = null;
		if (this.bmi <= 18.5)
			result = "underweight";
		else if (this.bmi <= 25)
			result = "normal";
		else if (this.bmi <= 30)
			result = "overweight";
		else
			result = "obese";
		return result;
	}
}
