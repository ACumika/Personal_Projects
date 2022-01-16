//assigning variables
int temppinhot=0; 
int temppincold=1;
//using analog pin 0


void setup() {
Serial.begin(9600);
Serial.println("CLEARSHEET");  //setup so PLX-DAQ recieves data. 
Serial.println("CLEARDATA");   //aka talking to PLX-DAQ
Serial.println("LABEL, TimeElappsed, TempHot, TempCold, Voltagetotal");
Serial.println("RESETTIMER");
}

void loop() { 
 Serial.print("DATA,"); //PLX-DAQ no knows that it will recieve data
unsigned long ElapsedTime=millis(); //Reads how much time has elapsed since the beggining of he experiment
ElapsedTime=ElapsedTime*0.001; //convert milliseconds to seconds
//analogReference (INTERNAL); //For the better precision, use internal reference (1.1V instead of 5V)
int temphot=analogRead(temppinhot); //Readiag data from the sensor. Stored as a 10bit number
float voltagehot = temphot * 5.0/1024; //Converting 10bit number to the temperature. 
float tempChot=(voltagehot - 0.5) * 100;
int tempcold=analogRead(temppincold); //Readiag data from the sensor. Stored as a 10bit number
float voltagecold = tempcold * 5.0/1024; //Converting 10bit number to the temperature. 
float tempCcold=(voltagecold - 0.5) * 100;
//1.1*temp/1024 - convert 10bit number to voltage
//Each degree rise results a 10 millivolt increase 
//so multiply by 1000 to convert to milivolts and devide by 10 to convet to degrees celsius. 
//float tempF=((tempC*9/5)+32); //Convert to Fahrenheit 
 int sum = 0;
 for (int i=0; i<30; i++) {
 sum=sum+analogRead(A2); //for loop to sum 30 measurments
  }
 float average=sum/30; //get average of the 30 measurments (better precision)
 float voltagetotal = average * (5.015 / 1024);
 //float voltageR2=analogRead(A3) * (5.015 / 1024);//voltage reading across R2
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
 //float Vs =( voltageR2 * 10.2)+voltageR2; //Total voltage calculations
  //R1 and R2 ratio is 10.2, therefore V across R1 is V for R2*Ratio
  //Total voltage is the sum of voltages across both resistors

Serial.print(  ElapsedTime);
Serial.print(",");
//Serial.print(  tempChot ); //print the temp in Celsius
//Serial.print(",");
//Serial.print(  tempCcold); //print temp in Fahrenheit
//Serial.print(",");
Serial.println(voltagetotal, 4);



 //print how much time elapsed since the begginign of the experiment
//separate data print outs with by comma, so PLX-DAQ recognizes it as separate data
delay(1000); //repeat the loop every second (take data every second)

}

