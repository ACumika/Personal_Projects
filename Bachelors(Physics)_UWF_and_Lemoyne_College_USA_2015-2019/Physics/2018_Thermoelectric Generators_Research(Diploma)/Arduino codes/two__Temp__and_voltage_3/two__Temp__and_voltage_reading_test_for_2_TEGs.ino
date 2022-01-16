//assigning variables to analog pins
int temppinhot1=0; 
int temppincold1=1;
int temppinhot2=3;
int temppincold2=4;

void setup() {
Serial.begin(9600);
Serial.println("CLEARSHEET");  //setup so PLX-DAQ recieves data. 
Serial.println("CLEARDATA");   //aka talking to PLX-DAQ
Serial.println("LABEL, TimeElappsed, TempHot1, TempCold1, TempHot2, TempCold2, DeltaT1, DeltaT2, AvDeltaT, VoltageR, Seebeck, Current");
Serial.println("RESETTIMER");
}

void loop() { 
 Serial.print("DATA,"); //PLX-DAQ knows that it will recieve data
unsigned long ElapsedTime=millis(); //Reads how much time has elapsed since the beggining of he experiment
ElapsedTime=ElapsedTime*0.001; //convert milliseconds to second

int temphot1=analogRead(temppinhot1); //Readiag data from the sensor on the hot bar for TEG1. Stored as a 10bit number
float voltagehot1 = temphot1 * 5.0/1024;  
float tempChot1=(voltagehot1 - 0.5) * 100;//Converting 10bit number to the temperature.
int tempcold1=analogRead(temppincold1); //Readiag data from the sensor on the cold bar for TEG1. Stored as a 10bit number
float voltagecold1 = tempcold1 * 5.0/1024;  
float tempCcold1=(voltagecold1 - 0.5) * 100;//Converting 10bit number to the temperature.
int temphot2=analogRead(temppinhot2); //Readiag data from the sensor on the hot bar for TEG2. Stored as a 10bit number
float voltagehot2 = temphot2 * 5.0/1024; 
float tempChot2=(voltagehot2 - 0.5) * 100;//Converting 10bit number to the temperature. 
int tempcold2=analogRead(temppincold2); //Readiag data from the sensor from the cold bar for TEG2. Stored as a 10bit number
float voltagecold2 = tempcold2 * 5.0/1024; 
float tempCcold2=(voltagecold2 - 0.5) * 100;//Converting 10bit number to the temperature. 

int sum = 0;
for (int i=0; i<30; i++) {
sum=sum+analogRead(A2); //for loop to sum 30 measurments
 }
float average=sum/30; //get average of the 30 measurments (better precision)
float voltageR = average * (5.015 / 1024);// Measured voltage (for whatever I am measuring)
//Computations from the measured data
float DeltaT1=tempChot1-tempCcold1; //temperature differece on the TEG1
float DeltaT2=tempChot2-tempCcold2; //temperature differece on the TEG2
float AvDeltaT=(DeltaT1+DeltaT2)/2; //Average temperature difference
float Seebeck=voltageR/AvDeltaT; //calculated Seebeck coefficient
// print out the value you read:
Serial.print(  ElapsedTime);
Serial.print(",");
Serial.print(  tempChot1 ); 
Serial.print(",");
Serial.print(  tempCcold1 ); 
Serial.print(",");
Serial.print(  tempChot2 );
Serial.print(",");
Serial.print(  tempCcold2 ); 
Serial.print(",");
Serial.print( DeltaT1 );
Serial.print(",");
Serial.print(  DeltaT2 ); 
Serial.print(",");
Serial.print(  AvDeltaT, 2 ); 
Serial.print(",");
Serial.print( voltageR, 4);
Serial.print(",");
Serial.println(  Seebeck, 4 );  
//separate data print outs with by comma, so PLX-DAQ recognizes it as separate data
delay(5000); //repeat the loop every second (take data every second)
}
