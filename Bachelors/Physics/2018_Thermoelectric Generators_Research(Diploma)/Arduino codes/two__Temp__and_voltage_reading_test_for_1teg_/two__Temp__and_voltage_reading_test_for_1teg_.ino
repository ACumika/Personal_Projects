//assigning variables
int temppinhot=0; 
int temppincold=1;

void setup() {
Serial.begin(9600);
Serial.println("CLEARSHEET");  //setup so PLX-DAQ recieves data. 
Serial.println("CLEARDATA");   //aka talking to PLX-DAQ
Serial.println("LABEL, TimeElappsed, TempHot, TempCold, Voltagetotal, DeltaT, , Seebeck");
Serial.println("RESETTIMER");
}

void loop() { 
  
Serial.print("DATA,"); //setup so PLX-DAQ receives data
unsigned long ElapsedTime=millis(); //Reads how much time has elapsed since the beggining of he experiment
ElapsedTime=ElapsedTime*0.001; //convert milliseconds to seconds

int temphot=analogRead(temppinhot); //Readiag data from the sensor on the hot bar. Stored as a 10bit number
float voltagehot = temphot * 5.0/1024; //Converting 10bit number to voltage ant then to the temperature. 
float tempChot=(voltagehot - 0.5) * 100; 
int tempcold=analogRead(temppincold); //Readiag data from the sensor on the cold bar. Stored as a 10bit number
float voltagecold = tempcold * 5.0/1024; //Converting 10bit number to voltage and then to the temperature. 
float tempCcold=(voltagecold - 0.5) * 100;

int sum = 0;
for (int i=0; i<30; i++) {
sum=sum+analogRead(A2); //for loop to sum 30 measurments
}
float average=sum/30; //get average of the 30 measurments (better precision)
float voltagetotal = average * (5.015 / 1024); //voltage measured fromt the TEG
float DeltaT=tempChot-tempCcold; //Computed delta temperature
 float Seebeck=voltagetotal/DeltaT; //Computed seebeck coefficient
// print out the value you read:
Serial.print(  ElapsedTime);
Serial.print(",");
Serial.print(  tempChot ); 
Serial.print(",");
Serial.print(  tempCcold); 
Serial.print(",");
Serial.print(voltagetotal, 4);
Serial.print(",");
Serial.print(  DeltaT ); 
Serial.print(",");
Serial.println(  Seebeck, 4);
//separate data print outs with by comma, so PLX-DAQ recognizes it as separate data 

delay(5000); //repeat the loop every second (take data every second)
}

