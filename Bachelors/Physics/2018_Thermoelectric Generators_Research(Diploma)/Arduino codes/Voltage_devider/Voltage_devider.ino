
void setup() {
  // initialize serial communication at 9600 bits per second:
Serial.begin(9600);
Serial.println("CLEARSHEET");//setup so PLX-DAQ recieves data.
Serial.println("CLEARDATA");
Serial.println("LABEL, Time, Voltage,");//Name labels for columns in Excel
Serial.println("RESETTIMER");
}

void loop(){
  Serial.print("DATA,"); //setup so PLX-DAQ recieves data.
  
  int sum = 0;
  for (int i=0; i<30; i++) {
  sum=sum+analogRead(A2); //for loop to sum 30 measurments
  }
  float average=sum/30; //get average of the 30 measurments (better precision)
  float voltageR2 = average * (5.015 / 1024); //voltage reading across R2
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):
  float Vs =( voltageR2 * 10.2)+voltageR2; //Total voltage calculations
  //R1 and R2 ratio is 10.2, therefore V across R1 is V for R2*Ratio
  //Total voltage is the sum of voltages across both resistors
  unsigned long Time=millis()/1000; //how much time has elapsed 
  // print out the value you read:
  Serial.print(Time); //print time elapsed
  Serial.print(",");
  Serial.println(Vs,5); //print total voltage with 5 decimals
  //separate data print outs with by comma, so PLX-DAQ recognizes it as separate data
  delay (1000);//repeat the loop every second (take data every second)
 
}
