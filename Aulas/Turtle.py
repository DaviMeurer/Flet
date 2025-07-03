import turtle

tela = turtle.Screen() #inicia a janela do executável
tela.bgcolor("black") #cor do plano de fundo
tela.title("Programa da tartaruga") #título do programa

#criando e editando um modelo
tartaruga1 = turtle.Turtle()
tartaruga1.shape("turtle") #modelo da variável
tartaruga1.color("blue", "white") #cor do modelo
tartaruga1.pensize(5) #tamanho da linha
tartaruga1.speed(1000) #velocidade
tartaruga1.begin_fill() #início para preencher

#desenhar o quadrado usando a lógica de programação
def desenharQuadrado(tartaruga):
    for i in range(4):
        tartaruga.forward(90) #andar reto  
        tartaruga.right(90) #girar eixo à direita

desenharQuadrado(tartaruga1)

tartaruga1.end_fill() #termina de preencher

robo = turtle.Turtle()
robo.shape("turtle")
robo.color("blue", "white")
robo.pensize(5)
robo.begin_fill()
robo.penup() #sobe a caneta
robo.goto(-200,300) #vá para coordenada x
robo.pendown() #desce a caneta
robo.circle(-100) #desenha um circulo

robo.end_fill()

tela.clearscreen() #limpa a tela

tartaruga1.penup()
tartaruga1.goto(0,0)
tartaruga1.pendown()
angulo = 0
while True:
    angulo -= 3.14
    tartaruga1.circle(angulo)