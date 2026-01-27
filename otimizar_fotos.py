import os
from PIL import Image

def converter_para_webp(diretorio_origem):
    # Extensões que vamos procurar
    extensoes = ('.jpg', '.jpeg', '.png')
    
    # Percorre a pasta e subpastas
    for raiz, diretorios, arquivos in os.walk(diretorio_origem):
        for arquivo in arquivos:
            if arquivo.lower().endswith(extensoes):
                caminho_completo = os.path.join(raiz, arquivo)
                
                # Define o novo nome com extensão .webp
                nome_sem_ext = os.path.splitext(caminho_completo)[0]
                novo_caminho = nome_sem_ext + ".webp"
                
                try:
                    with Image.open(caminho_completo) as img:
                        # Converte e salva com 80% de qualidade (ótimo equilíbrio)
                        img.save(novo_caminho, "webp", quality=80, optimize=True)
                        print(f"✅ Convertido: {arquivo} -> {os.path.basename(novo_caminho)}")
                    
                    # Opcional: Remove o arquivo original após converter
                    # os.remove(caminho_completo) 
                    
                except Exception as e:
                    print(f"❌ Erro ao converter {arquivo}: {e}")

# Ajuste o caminho para a sua pasta de imagens do Flask
diretorio_das_imagens = 'static/imagens'
converter_para_webp(diretorio_das_imagens)
print("\n✨ Processo concluído! Não esqueça de atualizar os nomes no seu HTML.")