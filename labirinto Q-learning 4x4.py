# Importação de bibliotecas necessárias
import numpy as np  # Biblioteca para operações com arrays e matrizes
import random  # Biblioteca para geração de números aleatórios
import tkinter as tk  # Biblioteca para criação de interfaces gráficas
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  # Backend do Matplotlib para integração com Tkinter



# Definição da classe Labirinto
class Labirinto:
    def __init__(self):
        # Definindo diferentes configurações de labirintos usando arrays numpy
        labirinto1 = np.array([
            [0, 1, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [0, 1, 0, 0]
        ])
        
        labirinto2 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ])
        
        labirinto3 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [1, 0, 1, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0]
        ])
        
        labirinto4 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ])
        
        labirinto5 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 0, 0]
        ])
        
        labirinto6 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 1, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 0]
        ])
        
        labirinto7 = np.array([
            [0, 1, 0, 0], # 0 = labirinto; 1 = parede
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [1, 0, 0, 0]
        ])
        
        labirinto8 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0]
        ])
        
        labirinto9 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 0, 1, 1],
            [1, 0, 1, 1],
            [0, 0, 0, 0]
        ])
        
        labirinto10 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ])
        labirinto11 = np.array([
            [0, 1, 0, 1], # 0 = labirinto; 1 = parede
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0]
        ])
        
        labirinto12 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [1, 1, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0]
        ])
        
        labirinto13 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [1, 0, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 0, 1]
        ])
        
        labirinto14 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 1]
        ])
        
        labirinto15 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 0, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 0, 0]
        ])
        
        labirinto16 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [1, 1, 1, 0],
            [1, 1, 0, 0],
            [1, 0, 0, 0]
        ])
        
        labirinto17 = np.array([
            [0, 1, 1, 0], # 0 = labirinto; 1 = parede
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 0]
        ])
        
        labirinto18 = np.array([
            [0, 0, 1, 1], # 0 = labirinto; 1 = parede
            [1, 0, 0, 1],
            [1, 0, 0, 0],
            [1, 0, 1, 0]
        ])
        
        labirinto19 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 0, 1, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ])
        
        labirinto20 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 0, 1]
        ])

        labirinto21 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 0, 1, 0],
            [0, 0, 0, 0],
            [1, 0, 0, 1]
        ])

        labirinto22 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 1]
        ])

        labirinto23 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 1],
            [0, 1, 0, 1],
            [0, 1, 0, 1]
        ])

        labirinto24 = np.array([
            [0, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0]
        ])

        labirinto25 = np.array([
            [0, 1, 0, 1], # 0 = labirinto; 1 = parede
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 1, 0, 1]
        ])

        labirinto26 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0]
        ])

        labirinto27 = np.array([
            [1, 0, 0, 0], # 0 = labirinto; 1 = parede
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1]
        ])

        labirinto28 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 0, 0, 0],
            [0, 1, 0, 0]
        ])

        labirinto29 = np.array([
            [0, 1, 0, 0], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 1, 1]
        ])

        labirinto30 = np.array([
            [0, 0, 0, 1], # 0 = labirinto; 1 = parede
            [0, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 0, 0, 1]
        ])
        
        # Armazenando todos os labirintos em uma lista
        arrays = [labirinto1, labirinto2, labirinto3, labirinto4, labirinto5, labirinto6, labirinto7, labirinto8, labirinto9, labirinto10, labirinto11, labirinto12, labirinto13, labirinto14, labirinto15, labirinto16, labirinto17, labirinto18, labirinto19, labirinto20, labirinto21, labirinto22, labirinto23, labirinto24, labirinto25, labirinto26, labirinto27, labirinto28, labirinto29, labirinto30]

        # Escolhendo um labirinto aleatoriamente
        array_escolhido = random.choice(arrays)
        self.grade = array_escolhido # Definindo o labirinto escolhido como atributo da classe
        
        # Gerando coordenadas iniciais e finais aleatórias dentro do labirinto
        iniX = random.randint(0, 3) # Coordenada X inicial
        iniY = random.randint(0, 3) # Coordenada Y inicial
        chegaX = random.randint(0, 3) # Coordenada X final
        chegaY = random.randint(0, 3) # Coordenada Y final
        
        # Ajustando coordenadas para garantir que início e fim estejam em posições válidas
        if iniX > chegaX:
            maiorX = iniX
            menorX = chegaX
        else:
            maiorX = chegaX
            menorX = iniX
        if iniY > chegaY:
            maiorY = iniY
            menorY = chegaY
        else:
            maiorY = chegaY
            menorY = iniY
        
        # Garantindo que as coordenadas de início e fim sejam válidas e não estejam muito próximas
        if self.grade[iniX, iniY] == 1 or self.grade[chegaX, chegaY] or (iniX == chegaX and iniY == chegaY) or (maiorX - menorX < 2 or maiorY - menorY < 2):
            while self.grade[iniX, iniY] == 1 or self.grade[chegaX, chegaY] or (iniX == chegaX and iniY == chegaY) or (maiorX - menorX < 2 or maiorY - menorY < 2):
                iniX = random.randint(0, 3) # Coordenada X inicial
                iniY = random.randint(0, 3) # Coordenada Y inicial
                chegaX = random.randint(0, 3) # Coordenada X final
                chegaY = random.randint(0, 3) # Coordenada Y final

                if iniX > chegaX:
                    maiorX = iniX
                    menorX = chegaX
                else:
                    maiorX = chegaX
                    menorX = iniX
                if iniY > chegaY:
                    maiorY = iniY
                    menorY = chegaY
                else:
                    maiorY = chegaY
                    menorY = iniY
        
        # Definindo posições de início e fim como atributos da classe
        self.inicio = (iniX, iniY)  # Posição inicial
        self.fim = (chegaX, chegaY)  # Posição final
        
        # Definindo as ações possíveis no labirinto
        self.acoes = ['cima', 'baixo', 'esquerda', 'direita']
    def movimento_valido(self, posicao): 
        # Verifica se a posição está dentro dos limites do labirinto e não é uma parede (1)
        x, y = posicao
        if x < 0 or x >= 4 or y < 0 or y >= 4 or self.grade[x, y] == 1:
            return False
        return True
    
    def mover(self, posicao, acao):
        # Move para uma nova posição com base na ação, se o movimento for válido
        x, y = posicao
        if acao == 'cima':
            nova_posicao = (x - 1, y) #esquerda
        elif acao == 'baixo':
            nova_posicao = (x + 1, y) #direita
        elif acao == 'esquerda':
            nova_posicao = (x, y - 1) #cima
        elif acao == 'direita':
            nova_posicao = (x, y + 1) #baixo
        else:
            raise ValueError("Ação inválida")
        
        if self.movimento_valido(nova_posicao):
            return nova_posicao
        return posicao

# Função para treinar o agente usando Q-Learning
def treinar_q_learning(labirinto, canvas_best, canvas_current, melhor_passos_label, episodio_label, passos_label, start_button, pontuacao_melhor_episodio_label, pontuacao_atual_episodio_label, pontuacao_ultimo_episodio_label, passos_ultimo_episodio_label, fig, ax, canvas_graph, alpha=0.1, gamma=0.9, epsilon=1.0, epsilon_decaimento=0.98, num_episodios=999, max_passos=100):

    start_button.config(bg="lightgray", state=tk.DISABLED)

    tabela_q = np.zeros((4, 4, len(labirinto.acoes)))

    melhor_caminho = None
    melhor_recompensa = float('-inf')
    melhor_passos = float('inf')
    pontuacao_melhor_episodio = 0
    pontuacao_ultimo_episodio = 0
    passos_ultimo_episodio = 0
    
    passos_por_episodio = []

    for episodio in range(1, num_episodios + 1):
        estado = labirinto.inicio  
        recompensa_total = 0  
        passos = 0  
        caminho = [estado]  
        
        for passo in range(max_passos):
            if random.uniform(0, 1) < epsilon:
                indice_acao = random.choice(range(len(labirinto.acoes)))  
            else:
                indice_acao = np.argmax(tabela_q[estado[0], estado[1], :])  

            acao = labirinto.acoes[indice_acao]  
            proximo_estado = labirinto.mover(estado, acao)  
            caminho.append(proximo_estado)  

            recompensa = -1 if proximo_estado == estado else (1 if proximo_estado == labirinto.fim else -0.1)
            valor_q = tabela_q[estado[0], estado[1], indice_acao]  
            maior_valor_q = np.max(tabela_q[proximo_estado[0], proximo_estado[1], :])  
            novo_valor_q = valor_q + alpha * (recompensa + gamma * maior_valor_q - valor_q)  
            
            tabela_q[estado[0], estado[1], indice_acao] = novo_valor_q  
            estado = proximo_estado  

            recompensa_total += recompensa  
            passos += 1  

            imprimir_labirinto(labirinto, caminho, canvas_current, "Tentativa Atual", espessura_linha=2)
            canvas_current.update()  
            canvas_current.after(10)  

            passos_label.config(text=f"Passos no episódio atual: {passos}/100")
            pontuacao_atual_episodio_label.config(text=f"Pontuação no episódio atual: {recompensa_total:.2f}")

            if estado == labirinto.fim:  
                break  

        if recompensa_total > melhor_recompensa or (recompensa_total == melhor_recompensa and passos < melhor_passos):
            melhor_recompensa = recompensa_total
            melhor_caminho = caminho.copy()
            melhor_passos = passos
            pontuacao_melhor_episodio = recompensa_total
            
            imprimir_labirinto(labirinto, melhor_caminho, canvas_best, "Melhor Caso", espessura_linha=2)
            canvas_best.update()

        pontuacao_ultimo_episodio = recompensa_total  
        passos_ultimo_episodio = passos  

        epsilon = max(epsilon * epsilon_decaimento, 0.01)  

        episodio_label.config(text=f"Episódio atual: {episodio+1}/1000")
        melhor_passos_label.config(text=f"Melhor quantidade de passos: {melhor_passos}")
        pontuacao_melhor_episodio_label.config(text=f"Pontuação no melhor episódio: {pontuacao_melhor_episodio:.2f}")
        passos_ultimo_episodio_label.config(text=f"Passos no último episódio: {passos_ultimo_episodio}")
        pontuacao_ultimo_episodio_label.config(text=f"Pontuação no último episódio: {pontuacao_ultimo_episodio:.2f}")

        passos_por_episodio.append(passos)

        ax.clear()
        ax.plot(range(1, episodio + 1), passos_por_episodio, color="#3E869C")
        ax.set_xlabel('Episódio')
        ax.set_ylabel('Passos')
        ax.set_title('Passos por Episódio')
        canvas_graph.draw()

    start_button.config(state=tk.NORMAL, bg="#C2FAC0") 

    return tabela_q

# Função para imprimir o labirinto na interface gráfica
def imprimir_labirinto(labirinto, caminho, canvas, titulo, espessura_linha=2):
    canvas.delete("all")  # Limpa o canvas
    grade_visual = labirinto.grade.copy()  # Copia o labirinto para visualização

    # Atualiza o caminho no labirinto visual
    for (x, y) in caminho:
        if (x, y) != labirinto.inicio and (x, y) != labirinto.fim:
            grade_visual[x, y] = 2

    grade_visual[labirinto.inicio] = 3  # Marca o ponto de início
    grade_visual[labirinto.fim] = 4  # Marca o ponto final

    cell_size = 55
    for i, linha in enumerate(grade_visual):
        for j, celula in enumerate(linha):
            if celula == 0:
                cor = "#989898"  # Cor do caminho
            elif celula == 1:
                cor = "#151515"  # Cor da parede
            elif celula == 2:
                cor = "#3E869C"  # Cor do caminho percorrido
            elif celula == 3:
                cor = "#C7161A"  # Cor do início
            elif celula == 4:
                cor = "#1A9823"  # Cor do fim

            canvas.create_rectangle(j * cell_size + 8, i * cell_size + 40, j * cell_size + cell_size + 8, i * cell_size + cell_size + 40, fill=cor, outline="black", width=espessura_linha)

            if (i, j) == caminho[-1]:
                canvas.create_rectangle((j*cell_size+8)+15, (i*cell_size+40)+15, (j*cell_size+cell_size+8)-15, (i*cell_size+cell_size+40)-15, outline="#FFFF00", width=7)  # quadrado que indica posição do agente
                
    canvas.create_text((2 * cell_size, 20), text=titulo, font=("Helvetica", 14), fill="black")

# Função para testar o agente treinado usando a tabela Q
def testar_q_learning(labirinto, tabela_q, canvas_current, max_passos=100):
    estado = labirinto.inicio  # Define o estado inicial como a posição de início do labirinto
    caminho = [estado]  # Inicializa a lista de caminho com o estado inicial
    for passo in range(max_passos):  # Loop para executar até o máximo de passos permitidos
        indice_acao = np.argmax(tabela_q[estado[0], estado[1], :])  # Seleciona a ação com maior valor Q para o estado atual
        acao = labirinto.acoes[indice_acao]  # Converte o índice da ação para a ação correspondente
        proximo_estado = labirinto.mover(estado, acao)  # Calcula o próximo estado após a ação
        caminho.append(proximo_estado)  # Adiciona o próximo estado ao caminho
        estado = proximo_estado  # Atualiza o estado atual para o próximo estado
        imprimir_labirinto(labirinto, caminho, canvas_current, "Tentativa Atual", espessura_linha=2)  # Atualiza a visualização do labirinto com o caminho atual
        canvas_current.update()  # Atualiza o canvas para refletir as mudanças
        canvas_current.after(0)  # Aguarda antes de continuar
        if estado == labirinto.fim:  # Se o agente chegou ao final do labirinto
            break  # Encerra o loop

# Função para iniciar o treinamento do agente
def iniciar_treinamento(canvas_best, canvas_current, melhor_passos_label, episodio_label, passos_label, start_button, pontuacao_melhor_episodio_label, pontuacao_atual_episodio_label, pontuacao_ultimo_episodio_label, passos_ultimo_episodio_label, fig, ax, canvas_graph):
    start_button.config(bg="lightgray", state=tk.DISABLED)  # Desabilita o botão de início durante o treinamento
    labirinto = Labirinto()  # Cria uma nova instância do labirinto
    # Inicia o treinamento do agente usando Q-Learning
    treinar_q_learning(
        labirinto, canvas_best, canvas_current, melhor_passos_label, episodio_label, passos_label, start_button, pontuacao_melhor_episodio_label, pontuacao_atual_episodio_label, pontuacao_ultimo_episodio_label, 
        passos_ultimo_episodio_label, fig, ax, canvas_graph
    )

# Função para criar a interface gráfica do aplicativo
def criar_interface():
    
     

    cori = "#D4D4D4"  # Define uma cor de fundo padrão para a interface
    root = tk.Tk()  # Cria a janela principal do aplicativo
    root.title("Labirinto Q-Learning")  # Define o título da janela
    root.configure(bg=cori)  # Configura a cor de fundo da janela
    
    # Função para fechar a janela corretamente
    def on_closing():
        root.quit()  # Encerra o loop principal do Tkinter
        root.destroy()  # Destroi a janela principal

    root.protocol("WM_DELETE_WINDOW", on_closing)  # Define o comportamento ao fechar a janela

    

    title_frame = tk.Frame(root)  # Cria um frame para o título
    title_frame.pack(pady=10)  # Adiciona o frame à janela principal com padding
    title_frame.configure(bg=cori)  # Configura a cor de fundo do frame
    
    # Cria um label para o título do aplicativo
    label = tk.Label(title_frame, text="Treinamento de Q-Learning para Labirinto 4x4", font=("Helvetica", 20))
    label.pack(pady=10)  # Adiciona o label ao frame com padding
    label.configure(bg=cori)  # Configura a cor de fundo do label
    
    # Cria um botão para iniciar o treinamento
    start_button = tk.Button(title_frame, text="INICIAR TREINAMENTO", font=("Helvetica", 14), bd=10)
    start_button.pack(side=tk.TOP, pady=(10, 0))  # Adiciona o botão ao frame com padding

    left_frame = tk.Frame(root)  # Cria um frame à esquerda da janela principal
    left_frame.pack(side=tk.LEFT, padx=10, pady=(10,0))  # Adiciona o frame à janela principal com padding
    left_frame.configure(bg=cori)  # Configura a cor de fundo do frame

    # Cria um sub-frame para organizar os labels e as legendas lado a lado
    info_legenda_frame = tk.Frame(left_frame, bg=cori)
    info_legenda_frame.pack(pady=(80, 40), padx=(40, 40), fill=tk.BOTH, expand=True)

    # Cria um frame para os labels das informações
    info_frame = tk.Frame(info_legenda_frame, bg=cori)
    info_frame.pack(side=tk.LEFT, anchor='n', padx=(0, 10))

    # Cria vários labels para exibir informações durante o treinamento
    melhor_passos_label = tk.Label(info_frame, text="Melhor quantidade de passos: ", font=("Arial", 12))
    melhor_passos_label.pack(pady=(5, 0), padx=(40,0))  # Adiciona o label ao frame com padding
    pontuacao_melhor_episodio_label = tk.Label(info_frame, text="Pontuação no melhor episódio: ", font=("Arial", 12))
    pontuacao_melhor_episodio_label.pack(pady=(0, 0), padx=(40,0))  # Adiciona o label ao frame
    melhor_passos_label.configure(bg=cori)  # Configura a cor de fundo do label
    episodio_label = tk.Label(info_frame, text="Episódio atual: 1/1000", font=("Arial", 12))
    episodio_label.pack(pady=(0, 0), padx=(40,0))  # Adiciona o label ao frame
    episodio_label.configure(bg=cori)  # Configura a cor de fundo do label
    passos_label = tk.Label(info_frame, text="Passos no episódio atual: ", font=("Arial", 12))
    passos_label.pack(pady=(0, 0), padx=(40,0))  # Adiciona o label ao frame
    passos_label.configure(bg=cori)  # Configura a cor de fundo do label
    pontuacao_melhor_episodio_label.configure(bg=cori)  # Configura a cor de fundo do label
    pontuacao_atual_episodio_label = tk.Label(info_frame, text="Pontuação no episódio atual: ", font=("Arial", 12))
    pontuacao_atual_episodio_label.pack(pady=(0, 0), padx=(40,0))  # Adiciona o label ao frame
    pontuacao_atual_episodio_label.configure(bg=cori)  # Configura a cor de fundo do label
    passos_ultimo_episodio_label = tk.Label(info_frame, text="Passos no último episódio: ", font=("Arial", 12))
    passos_ultimo_episodio_label.pack(pady=(0, 0), padx=(40,0))  # Adiciona o label ao frame
    passos_ultimo_episodio_label.configure(bg=cori)  # Configura a cor de fundo do label
    pontuacao_ultimo_episodio_label = tk.Label(info_frame, text="Pontuação no último episódio: ", font=("Arial", 12))
    pontuacao_ultimo_episodio_label.pack(pady=(0, 10), padx=(40,0))  # Adiciona o label ao frame com padding
    pontuacao_ultimo_episodio_label.configure(bg=cori)  # Configura a cor de fundo do label

    # Cria um frame para as legendas das cores
    legenda_frame = tk.Frame(info_legenda_frame, bg=cori)
    legenda_frame.pack(side=tk.RIGHT, anchor='n', pady=(5,0))

    cores_legenda = [
        ("#C7161A", "Posição inicial"),
        ("#151515", "Paredes"),
        ("#989898", "Caminho do labirinto"),
        ("#3E869C", "Caminho já visitado"),
        ("#1A9823", "Posição objetivo"),
        ("#FFFF00", "Agente inteligente")
    ]
    for cor, texto in cores_legenda:
        legenda_item = tk.Frame(legenda_frame, bg=cori)
        legenda_item.pack(anchor="w", pady=2)
        tk.Canvas(legenda_item, width=20, height=20, bg=cor, highlightthickness=2, highlightbackground="black").pack(side="left", padx=5)
        tk.Label(legenda_item, text=texto, font=("Arial", 12), bg=cori).pack(side="left")

    # Cria um frame para o gráfico
    graph_frame = tk.Frame(left_frame)
    graph_frame.pack(pady=(0, 0))  # Adiciona o frame ao frame esquerdo
    graph_frame.configure(bg=cori)  # Configura a cor de fundo do frame

    # Cria um gráfico usando matplotlib
    fig, ax = plt.subplots(figsize=(6, 3.1))
    ax.set_xlabel('Episódio', fontsize=10)
    ax.set_ylabel('Passos', fontsize=10)
    ax.set_title('Passos por Episódio', fontsize=10)
    plt.tight_layout()
    fig.patch.set_facecolor(cori)  # Configura a cor de fundo do gráfico
    
    # Integra o gráfico ao Tkinter
    canvas_graph = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas_graph.draw()
    canvas_graph.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    right_frame = tk.Frame(root)  # Cria um frame à direita da janela principal
    right_frame.pack(side=tk.RIGHT)  # Adiciona o frame à janela principal
    right_frame.configure(bg=cori, padx=40)  # Configura a cor de fundo do frame e adiciona padding

    # Cria canvas para exibir o labirinto atual e o melhor caminho encontrado
    canvas_current = tk.Canvas(right_frame, width=238, height=268, bg="lightgray", highlightthickness=0, highlightbackground="black")
    canvas_current.pack(pady=(25, 5))  # Adiciona o canvas ao frame direito com padding

    canvas_best = tk.Canvas(right_frame, width=238, height=268, bg="lightgray", highlightthickness=0, highlightbackground="black")
    canvas_best.pack(pady=(5, 40))  # Adiciona o canvas ao frame direito com padding

    # Configura o botão de início para chamar a função de iniciar treinamento
    start_button.config(bg="#C2FAC0", command=lambda: iniciar_treinamento(canvas_best, canvas_current, melhor_passos_label, episodio_label, passos_label, start_button, pontuacao_melhor_episodio_label, pontuacao_atual_episodio_label, pontuacao_ultimo_episodio_label, passos_ultimo_episodio_label, fig, ax, canvas_graph))
    
    
    # Inicia o loop principal do Tkinter
    root.mainloop()

# Chama a função para criar a interface
criar_interface()