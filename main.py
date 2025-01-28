import pyautogui
import time
import random
import threading
import keyboard

# Função que monitora a tecla de cancelamento
def monitorar_cancelamento():
    global cancelado
    while True:
        if keyboard.is_pressed('esc'):  # Se a tecla ESC for pressionada
            cancelado = True
            print("Execução cancelada.")
            break
        time.sleep(0.1)

# Lista de palavras para pesquisar
palavras = [
    "futuro digital", "astronomia", "motores elétricos", "saúde pública", "modelos de negócios",
    "inteligência artificial", "novas tecnologias", "biotecnologia", "criatividade digital", 
    "comunicação virtual", "soluções sustentáveis", "inteligência emocional", "manutenção de carros", 
    "engenharia genética", "cidades do futuro", "mundo pós-pandemia", "educação 4.0", "transformação digital", 
    "autossuficiência energética", "redes neurais", "fotografia de paisagens", "astrobiologia", 
    "segurança digital", "aplicativos para produtividade", "impacto ambiental", "futuro do trabalho", 
    "matemática aplicada", "futuro do ensino", "tecnologias emergentes", "ciência de dados", "mudanças climáticas", 
    "agricultura sustentável", "cidades inteligentes", "futuro dos transportes", "engenharia ambiental", 
    "soluções ecológicas", "viver no espaço", "tecnologias móveis", "exoplanetas", "fotografia urbana", 
    "humanização da tecnologia", "design de produto", "computação em nuvem", "bioinformática", 
    "internet das coisas", "mercado de criptomoedas", "alimentos orgânicos", "redes sociais", "robôs assistivos", 
    "cultura digital", "política ambiental", "educação inclusiva", "saúde mental", "blockchain", 
    "investimentos sustentáveis", "economia verde", "energia solar", "reciclagem de plásticos", "engenharia de software", 
    "aplicativos móveis", "inovação educacional", "automação industrial", "sistemas inteligentes", "realidade aumentada", 
    "sistemas operacionais", "web 3.0", "mineração de dados", "sistemas de recomendação", "agilidade empresarial", 
    "indústria 4.0", "código aberto", "desenvolvimento de jogos", "gestão de resíduos", "transporte sustentável", 
    "inovação social", "desafios tecnológicos", "conscientização ambiental", "smart cities", "engenharia elétrica", 
    "energias renováveis", "aceleração de startups", "tendências de mercado", "cultura do desperdício", "inclusão digital", 
    "tecnologia blockchain", "saúde de precisão", "uso de drones", "novas fronteiras científicas", "economia colaborativa", 
    "drones de entrega", "transporte autônomo", "gerenciamento de projetos", "smartphones dobráveis", "dispositivos vestíveis", 
    "comércio eletrônico", "gestão de equipes", "empreendedorismo social", "futuro das energias", "circuitos integrados"
]


# Número de pesquisas
num_pesquisas = 30

# Variável para verificar se a execução foi cancelada
cancelado = False

# Iniciar o monitoramento da tecla ESC em um thread separado
monitoramento_thread = threading.Thread(target=monitorar_cancelamento)
monitoramento_thread.daemon = True  # Torna o thread da monitorização em segundo plano
monitoramento_thread.start()

# Esperar antes de começar
print("Iniciando em 5 segundos... Abra o navegador e esteja no campo de busca.")
time.sleep(5)

for i in range(num_pesquisas):
    if cancelado:  # Se a execução foi cancelada
        break
    
    # Escolher uma palavra aleatória da lista
    palavra = random.choice(palavras)
    
    # Digitar a palavra
    pyautogui.typewrite(palavra, interval=random.uniform(0.05, 0.15))
    
    # Pressionar Enter
    pyautogui.press("enter")
    
    # Esperar um tempo aleatório entre 5 e 10 segundos
    time.sleep(random.uniform(5, 10))
    
    # Pressionar Ctrl + E (para selecionar o campo de busca novamente)
    pyautogui.hotkey("ctrl", "e")
    
    # Esperar um tempo aleatório antes da próxima busca
    time.sleep(random.uniform(3, 6))

if not cancelado:
    print("Pesquisas concluídas!")
