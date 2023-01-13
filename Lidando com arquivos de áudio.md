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

### >>> <<<
