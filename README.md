# MagicLens

O aplicativo tem como objetivo simplificar a transformação e otimização de imagens para o front-end, proporcionando uma experiência mais eficiente e rápida para desenvolvedores e designers.

## Instalação
```bash
poetry install
```

## Uso
Para usar o MagicLens, siga os passos abaixo:

1. **Escolha as configurações**: Ajuste as opções de transformação e otimização conforme necessário utilizando o path da URL.

2. **Enviar Imagem**: Utilize a seguinte URL para enviar a imagem que deseja salvar:
   ```
   POST /api/upload
   ```
   - **Corpo da Requisição**: Envie a imagem no formato multipart/form-data.

3. **Puxar Imagem**: Para obter a imagem otimizada, utilize a URL abaixo, incluindo as informações de modificações desejadas:
   ```
   GET /api/image?size=larguraxaltura&flip=true&crop=top
   ```
   - **Parâmetros**:
     - `size`: Especifique o tamanho desejado da imagem (ex: 800x600).
     - `flip`: Indica se a imagem deve ser invertida (true/false).
     - `crop`: Define a área a ser cortada (ex: top, bottom, left, right).



## Funcionalidades
- **Otimização de Imagens**: Reduz o tamanho das imagens sem perda significativa de qualidade.