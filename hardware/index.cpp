void setup() {
  // Inicialize a porta serial com a mesma taxa de transmissão usada no Python
  Serial.begin(9600);
}

void loop() {
  // Verifique se há dados disponíveis para leitura na porta serial
  if (Serial.available() > 0) {
    // Leia os dados da porta serial
    String dadosRecebidos = Serial.readString();

    // Imprima os dados recebidos no monitor serial
    Serial.println("Dados recebidos do Python: " + dadosRecebidos);

    
    if(dadosRecebidos.find("subir") != string::npos){
      //SUBIR
      // pegar andar
    } else {
      //descer
      // pegar andar
    }
  }
}