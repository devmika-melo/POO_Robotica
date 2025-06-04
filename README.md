<h1 align="center">🤖 POO_Robótica 🤖</h1>
<h3 align="center">🚀 Treinando aplicação de Programação Orientada a Objetos (POO) na Robótica 🚀</h3>

---

### 🧠 Linguagens utilizadas:
- 🐍 Python
- 💻 C
- 💻 C++
- ☕ Java

---

## 🛠️ Projetos:

## 🧠 Desafio 1 — Gerenciamento de Energia do Robô
Crie uma classe chamada `Robo` com os atributos: `nome` e `bateria` (inicialmente em 100%).
Implemente os métodos:
- `exibir_status()`: mostra o nome e a bateria atual do robô.
- `diminuir_bateria(valor)`: reduz a bateria no valor informado, sem permitir que fique abaixo de 0.
  Caso a bateria chegue a 0%, exibir "Descarregado (0%)".

Bônus: Implemente o método `recarregar()` que restaura a bateria para 100%.

## 🤖 Desafio 2 — Robô Inteligente: Movimento, Parada e Bateria
Crie uma classe `Robo` com os atributos: `nome`, `bateria` (100%) e `velocidade` (50 km/h).
Implemente os métodos:
- `mover()`: o robô se move, reduz 10% da bateria e aumenta a velocidade em 10 km/h (até 100 km/h).
  Se estiver parado (velocidade 0), começa a 10 km/h.
  Não se move se estiver sem bateria.
- `parar()`: zera a velocidade.
- `recarregar()`: recarrega a bateria para 100%.
- `exibir_status()`: mostra nome, bateria e velocidade atual.
- `verificar_velocidade(limite)`: limita a velocidade ao valor definido se ultrapassar.

Bônus: Crie o método `tem_bateria()` que retorna `True` se a bateria for maior que 0 e `False` se estiver descarregado.
