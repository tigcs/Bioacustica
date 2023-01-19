### Cálculo de Índices Acústicos ###

Este script tem como objetivo calcular índices acústicos de vários arquivos de áudio utilizando o R para rodar o programa **AnalysisPrograms.exe (AP)** em laço (loop). Via R o comando é repassado ao terminal Linux.

````{r}
# Diretório de trabalho
setwd("~/CPLE")

# Diretório de entrada contendo os arquivos de áudio
diretorio <- "/home/tiago/CPLE/10minutos"
# Diretório de saída
output <- "/home/tiago/10minutos_output"

# Lista os arquivos de áudios no diretório de entrada
files <- list.files(diretorio, pattern = "*.WAV", full.names = TRUE)

# Loop
for(file in files) {
  message("Processing ", file) 
  
  # Nome do arquivo de áudio
  file_name <- basename(file)
  
  # Cria o diretório de saída
  output_diretorio <- normalizePath(file.path(output, file_name))
  dir.create(output_diretorio, recursive = TRUE)
  
  # Prepare o comando
  command <- sprintf('audio2csv "%s" "Towsey.Acoustic.yml" "%s" ', file, output_diretorio)
  
  # Roda o comando no terminal linux
  system2('AP', command)
}
````
