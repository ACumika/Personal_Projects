
void setup() {
  // initialize serial communication at 9600 bits per second:
Serial.begin(9600);
}

void loop(){
  analogReference (INTERNAL);
  int sum = 0;
  for (int i=0; i<30; i++) {
  sum=sum+analogRead(A2); //for loop to sum 30 measurments
  }
  float average=sum/30; //get average of the 30 measurments (better precision)
  float voltage = average * (1.1/ 1024) * 1000; //voltage mili reading 
  // Convert the analog reading (which goes from 0 - 1023) to a voltage (0 - 5V):

  unsigned long Time=millis()/1000; //how much time has elapsed 
  
  // print out the value you read:
  Serial.print("Voltage reading: ");
  Serial.print(voltage,4); //print voltage mesurement with 4 decimals
  Serial.println(" mV");

  delay (1000);//repeat the loop every second (take data every second)
 
}
