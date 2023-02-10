### >>> Carregar, visualizar, colar e salvar arquivos de áudio <<<

````{r}
library(tuneR)
library(seewave)

# Carregar arquivo de áudio
    tico <- readWave("./tico.wav")

# Vizualizar arquivo de áudio em um oscilograma.
# "f": indica a frequência da taxa de amostragem do áudio em Hz, que não é obrigatório desde que o arquivo wave já tenha esta informação incorporada a ele.
    oscillo(tico,f=22050)

# Colar o arquivo de áudio. 
# "f": indica a frequência da taxa de amostragem do áudio em Hz, que não é obrigatório desde que o arquivo wave já tenha esta informação incorporada a ele.
# "output": indica a classe de objeto que deve ser retornada, pode ser "matrix", "Wave", "Sample", "audioSample" ou "ts".
# "plot": se TRUE, retorna um gráfico com oscilogramas de cada um dos áudios de entrada e do resultado.
    a10 <- pastew(tico,tico,f=22050, output = "Wave", plot=TRUE)
````

### >>> Função para juntar vários arquivos de áudios de um único arquivo <<<

Esta função une/junta/cola vários arquivos de áudios provenientes do Audiomoth (firmware 1.8.1) em um único arquivo. Faz uso dos pacotes 'tuneR' e 'seewave'.

````{r}
juntar_audios <- function (lista_audios, diretorio) {
  library(tuneR)
  library(seewave)
  for (a in lista_audios) {
    if (exists ("a1") == FALSE) { #carrega o primeiro áudio da lista, caso ainda não tenha sido carregado
      a1 <- readWave(a) 
      a1_hora <- substr(basename(a),10,13) # armazena a hora do primeiro áudio para nomear o arquivo final
      print (a)}
    else {
      print(a)
      a2 <- readWave(a)
      a2_hora <- substr(basename(a),10,13) # armazena a hora do último áudio para nomear o arquivo final
      ax <- bind(a1,a2) # une/junta/cola os áudios
      a1 <- ax}
  }
  dia <- substr(basename(a),1,9) # armazena o dia de gravação dos áudios
  writeWave(a1, filename = paste0(diretorio,dia, a1_hora,"-", a2_hora,"_G.WAV")) # salva o arquivo de áudio resultante, "AAAAMMDD_HoraPrimeiro-HoraÚltimo_G.WAV"
  print("SALVO")
  gc() # Libera a memória RAM utilizada pelo R, já que os arquivos trabalhados podem ser bem grandes.
}
````
### >>> Função para juntar um determinado número de arquivos de áudios de um único arquivo <<<

Esta função une/junta/cola um determinado número de arquivos de áudios provenientes do Audiomoth (firmware 1.8.1) em um único arquivo. Faz uso dos pacotes 'tuneR' e 'seewave', além da função **juntar_audios**.

````{r}
juntar_audios_grupos <- function(audios, diretorio,n){
library(tuneR)
library(seewave)
for (i in audios) {
  if (length(audios) > 0){
    lista_n_audios <- audios [1:n] # cria uma lista com os nomes dos arquivos de áudio na quantidade determinda
    lista_n_audios <- lista_n_audios[!is.na(lista_n_audios)] # caso não tenha a quantidade suficiente de arquivos, elimina-se o item NA criados. Elimina NA de uma lista.
    print (paste0("AGRUPANDO: ", lista_n_audios[1], " -----ATÉ------ ", lista_n_audios[length(lista_n_audios)])) # Escreve no console para acompanhamento do laço.
    juntar_audios(lista_audios = lista_n_audios, diretorio = diretorio ) # junta os arquivos em um único aqruivo.
    audios <- audios[-c(1:n)]} # Elimina os arquivos que já foram unidos da lista de áudios que está sendo utilizada pelo laço.
    }
  print("FIM")
}
````
### >>> Juntar vários arquivos de áudios de um único arquivo COM reamostragem <<<

Esta função une/junta/cola vários arquivos de áudios provenientes do Audiomoth (firmware 1.8.1) em um único arquivo. Faz uso dos pacotes 'tuneR' e 'seewave'.
````{r}
#### Aumentando a memória RAM disponível para uso no R, se necessário ####
library(unix)
rlimit_all()
rlimit_as(1e15)  #aumenta para ~15GB

#### Carregando bibliotecas & configurando WD  ####
library(seewave)
library(tuneR)
setwd("~/CPLE")
files <- list.files("./audios",pattern = "*.WAV", full.names = TRUE)

#### Juntar Áudios com reamostragem ####
juntar_audios <- function (lista_audios, diretorio) {
  library(tuneR)
  library(seewave)
  for (a in lista_audios) {
    if (exists ("a1") == FALSE) { #carrega o primeiro áudio da lista, caso ainda não tenha sido carregado
      a1 <- readWave(a)
      a1 <- downsample(a1, samp.rate = 44000) # reamostragrem para frequência inferior
      a1_hora <- substr(basename(a),10,13) # armazena a hora do primeiro áudio para nomear o arquivo final
      print (a)
      gc() # Libera a memória RAM utilizada pelo R, já que os arquivos trabalhados podem ser bem grandes.
      }
    else {
      print(a)
      a2 <- readWave(a)
      a2 <- downsample(a2, samp.rate = 44000) # reamostragrem para frequência inferior
      a2_hora <- substr(basename(a),10,13) # armazena a hora do último áudio para nomear o arquivo final
      ax <- bind(a1,a2) # une/junta/cola os áudios
      a1 <- ax
      dia <- substr(basename(a),1,9) # armazena o dia de gravação dos áudios
      writeWave(a1, filename = paste0(diretorio,dia, a1_hora,"-", a2_hora,"_G.WAV")) # salva o arquivo de áudio resultante, "AAAAMMDD_HoraPrimeiro-HoraÚltimo_G.WAV"
      gc() # Libera a memória RAM utilizada pelo R, já que os arquivos trabalhados podem ser bem grandes.
      }
  }
  dia <- substr(basename(a),1,9) # armazena o dia de gravação dos áudios
  gc() # Libera a memória RAM utilizada pelo R, já que os arquivos trabalhados podem ser bem grandes.
  #writeWave(a1, filename = paste0(diretorio,dia, a1_hora,"-", a2_hora,"_G.WAV")) # salva o arquivo de áudio resultante, "AAAAMMDD_HoraPrimeiro-HoraÚltimo_G.WAV"
  print("SALVO")
  gc() # Libera a memória RAM utilizada pelo R, já que os arquivos trabalhados podem ser bem grandes.
}

#### Executa a função ####
juntar_audios(files,"./audios_teste/")
````
