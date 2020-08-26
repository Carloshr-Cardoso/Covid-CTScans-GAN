# Carlos Cardoso's Master's Thesis
## GANs como Estratégia de Balanceamento de Dados: Aplicado em Tomografias Computadorizadas de Covid-19 

#### Base de Dados Tratada
  - Imagens de Resolução 512x512 em formato .jpg 
  - Classes: Covid Positivos | Covid Negativos
  - Disponivel Para Download em: <Link Google Drive>
  
  
#### Base de Dados Original
  - Imagens de Resolução 512x512 em formato .TIF 16bit em escala de cinza. (Não possível abrir em monitores convencionais, precisando ser convertida para 32bit)
  - <Visualize.py> Arquivo para conversão das imagens .TIF para jpg 32bit em escala de cinza.
  - Disponível em https://drive.google.com/drive/folders/1xdk-mCkxCDNwsMAk2SGv203rY1mrbnPB?usp=sharing
  
#### Classes:
  
|                |Covid Positivos                |Covid Negativos              |
|----------------|-------------------------------|-----------------------------|
|Train Set       |15.589 Imagens                 |48.260 Imagens               |
|Test Set        |2.282 Imagens                  |9.776 Imagens                |
|Total           |17.871 Imagens                 |58.036 Imagens               |

#### Train Set:

|                |Pacientes Covid Positivos      |Pacientes Covid Negativos    |
|----------------|-------------------------------|-----------------------------|
|Train Set       |95 Pacientes                   |282 Pacientes                |

> **Sobre:** COVID-CTset is our introduced dataset. This dataset contains the full original CT scans of 377 persons. There are 15589 and 48260 CT scan images belonging to 95 Covid-19 and 282 normal persons, respectively. It was gathered from Negin medical center that is located at Sari in Iran. This medical center uses a SOMATOM Scope model and syngo CT VC30-easyIQ software version for capturing and visualizing the lung HRCT radiology images from the patients. The format of the exported radiology images was 16-bit grayscale DICOM format with 512*512 pixels resolution. As the patient's information was accessible via the DICOM files, we converted them to TIFF format, which holds the same 16-bit grayscale data but does not conclude the patients' private information.
