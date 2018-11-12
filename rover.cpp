int motor1Pin1 = 5; 
int motor1Pin2 = 6; 
int motor2Pin1 = 8;
int motor2Pin2 = 7; 
char dataIn = 'S';
char determinant;
char det;
int vel = 0; 
int whitelight = 13;
int redlight = 10;
void setup() {
Serial.begin(9600); 
pinMode(motor1Pin1, OUTPUT);
pinMode(motor1Pin2, OUTPUT);
pinMode(motor2Pin1, OUTPUT);
pinMode(motor2Pin2, OUTPUT);
pinMode(whitelight, OUTPUT);
pinMode(redlight, OUTPUT);
digitalWrite(whitelight, LOW);
digitalWrite(redlight, LOW);
}
void loop() {
det = check(); 
switch (det){
case 'F': // F, move forward
digitalWrite(motor1Pin1, HIGH);
digitalWrite(motor1Pin2, LOW);
digitalWrite(motor2Pin1, LOW);
digitalWrite(motor2Pin2, HIGH);
det = check();
break;
case 'B': // B, move back
digitalWrite(motor1Pin1, LOW);
digitalWrite(motor1Pin2, HIGH);
digitalWrite(motor2Pin1, HIGH);
digitalWrite(motor2Pin2, LOW);
det = check();
break;
case 'L':// L, move wheels left
digitalWrite(motor1Pin1, HIGH);
digitalWrite(motor1Pin2, LOW);
digitalWrite(motor2Pin1, LOW);
digitalWrite(motor2Pin2, LOW);
det = check();
break;
case 'R': // R, move wheels right
digitalWrite(motor1Pin1, LOW);
digitalWrite(motor1Pin2, LOW);
digitalWrite(motor2Pin1, LOW);
digitalWrite(motor2Pin2, HIGH);
det = check();
break;
case 'S': // S, stop
digitalWrite(motor1Pin1, LOW);
digitalWrite(motor1Pin2, LOW);
digitalWrite(motor2Pin1, LOW);
digitalWrite(motor2Pin2, LOW);
det = check();
break;
case 'U': // V, Red light on
//Serial.println("Red LIght On");
digitalWrite(redlight, HIGH);
break;
case 'u': //v, Red light off
//Serial.println("Red Light Off");
digitalWrite(redlight, LOW);
break;
case 'W': //W, Front Lights On
//Serial.println("White LIght On");
digitalWrite(whitelight, HIGH);
break;
case 'w': //w, Front Lights Off
//Serial.println("White Light Off");
digitalWrite(whitelight, LOW);
break;
}
}
int check(){
if (Serial.available() > 0){
dataIn = Serial.read();
if (dataIn == 'F'){//Forward
determinant = 'F';
}
else if (dataIn == 'B'){//Backward
determinant = 'B';
}
else if (dataIn == 'L'){//Left
determinant = 'L';
}
else if (dataIn == 'R'){//Right
determinant = 'R';
}
else if (dataIn == 'S'){//Stop
determinant = 'S';
}
else if (dataIn == 'U'){//Red Lights On
determinant = 'U';
}
else if (dataIn == 'u'){//Red Lights Off
determinant = 'u';
}
else if (dataIn == 'W'){//White Lights On
determinant = 'W';
}
else if (dataIn == 'w'){//White Lights Off
determinant = 'w';
}
return determinant;
}
}