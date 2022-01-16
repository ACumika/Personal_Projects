//assigning pin for the temperature sesor
int temppin=0; 

void setup() {
Serial.begin(9600);
Serial.println("CLEARSHEET");  //setup so PLX-DAQ recieves data. 
Serial.println("CLEARDATA");   //aka talking to PLX-DAQ
Serial.println("LABEL, TimeElappsed, TempC, TempF");  //Label the columns in the Excel spreadsheet
Serial.println("RESETTIMER");
}

void loop() { 
 Serial.print("DATA,"); //PLX-DAQ no knows that it will recieve data
 
unsigned long ElapsedTime=millis(); //Reads how much time has elapsed since the beggining of he experiment
ElapsedTime=ElapsedTime*0.001; //convert milliseconds to seconds

int temp=analogRead(temppin); //Readiag data from the hot sensor. Stored as a 10bit number
float voltage = temp * 5.0/1024;  
float tempC=(voltage - 0.5) * 100; //Converting 10bit number to the temperature.

float tempF=((tempC*9/5)+32); //Convert to Fahrenheit  
//print data. Separate data print outs with by comma, so PLX-DAQ recognizes it as separate data
Serial.print(  ElapsedTime ); //print how much time elapsed since the begginign of the experiment
Serial.print(",");
Serial.print(  tempC ); //print the temp in Celsius
Serial.print(",");
Serial.println(  tempF ); //print temp in Fahrenheit

delay(1000); //repeat the loop every second (take data every second)

}

