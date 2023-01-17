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

Esta função une/junta/cola vários arquivos de áudios provenientes do Audiomoth (firmware 1.8.1) eu um único arquivo. Faz uso dos pacotes 'tuneR' e 'seewave'.

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
