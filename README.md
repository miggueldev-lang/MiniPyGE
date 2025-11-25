# MiniPyGE
Uma mini game engine em Python criada para desenvolvimento rápido, modular e organizado de jogos 2D.

MiniPyGE é uma engine minimalista construída sobre **Pygame**, focada em simplicidade, organização e extensibilidade.  
Ideal para quem quer estudar arquitetura de game engines, criar protótipos rápidos ou desenvolver jogos completos.

---

## 📦 Recursos Principais

### 🔹 Sistema de Entidades (ECS simples)
- `Entity` com posição, tamanho, física, rendering, hitbox e eventos.
- `EntityManager` para organizar, atualizar e desenhar por layers.
- Tags para filtragem rápida de entidades.

### 🔹 Sistema de Cenas
- Estrutura com `enter()`, `update()`, `draw()`, `exit()`.
- Gerenciador para trocar cenas com segurança.

### 🔹 Motor de Física
- `PhysicsBody` com gravidade, aceleração, velocidade e colisão.
- Aplicação de força horizontal e saltos.
- Atualização centralizada e independente da cena.

### 🔹 Sistema de Câmera
- Segue entidades dinamicamente.
- Suavização (lerp).
- Aplicação automática ao desenhar entidades.

### 🔹 Gerenciador de Inputs
- Mapeamento de ações → teclas (`move_left`, `jump`, etc).
- `is_key_pressed`, `is_key_held`, `is_key_released`.
- Acesso a teclas cruas.

### 🔹 Gerenciamento de Assets
Carregamento fácil com caching automático:
- Imagens  
- Sons  
- Música  
- Fontes  

---