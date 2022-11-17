#include <DHT11.h>
#define DHTPIN 2

#define DHTTYPE DHT11
// 아두이노 릴레이모듈 실험
// 1초마다 ON/OFF를 반복합니다. 1초마다 릴레이 접점이 붙었다 떨어지는 "딸깍"소리를 들을 수 있습니다.

int relay_pin = 6; //릴레이 신호핀(S)에 연결되는 아두이노 핀
int humi_pin = 5;
DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  pinMode(relay_pin, OUTPUT); //릴레이 신호용 아두이노 디지털 핀을 출력으로 설정
  pinMode(humi_pin, OUTPUT);
  Serial.println("temp, Humi");

  dht.begin();
}

void loop()
{
  // Wait a few seconds between measurements.
  delay(2000);

  
  int temp = (int)dht.readTemperature();
  int humi = (int)dht.readHumidity();

  Serial.print(temp); //온도값 시리얼 모니터에 출력
  Serial.print(',');
  Serial.println(humi); //습도: 출력

  if (temp >= 30){
    digitalWrite(relay_pin, LOW); //릴레이 접점 OFF
    delay(500); //1초 대기
  }else if (temp <= 20){
    digitalWrite(relay_pin, HIGH); //릴레이 접점 ON
    delay(500); //1초 대기
  }

  if (humi <= 60) {
    digitalWrite(humi_pin, HIGH);
    delay(500);
  }else if (humi >= 80) {
    digitalWrite(humi_pin, LOW);
    delay(500);
  }
  
  
}
