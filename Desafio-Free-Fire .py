# Desafio-Free-Fire: Gerenciamento de Vida e Cura

class Jogador:
    def __init__(self, nome, vida_maxima=200):
        self.nome = nome
        self.vida_maxima = vida_maxima
        self.vida_atual = vida_maxima
        self.kits_medicos = 3  # Inventário inicial de kits
        print(f"[{self.nome}] Airdrop: Vida Máxima {self.vida_maxima}, Kits Médicos {self.kits_medicos}.")

    def sofrer_dano(self, dano):
        """Calcula o dano sofrido e atualiza a vida."""
        
        # Simula o dano
        self.vida_atual -= dano
        print(f"\n🚨 {self.nome} sofreu {dano} de dano!")
        print(f"Vida atual: {self.vida_atual}")

        if self.vida_atual <= 0:
            self.vida_atual = 0
            print(f"💀 O jogador {self.nome} foi abatido!")
            return False # Retorna Falso se o jogador estiver fora de combate
        
        return True

    def usar_kit_medico(self, cura_por_kit=75):
        """Usa um kit médico para restaurar a vida, se disponível."""
        
        if self.kits_medicos <= 0:
            print(f"\n❌ {self.nome}: Sem Kits Médicos! Procurando por loot...")
            return

        if self.vida_atual == self.vida_maxima:
            print(f"\n⚠️ {self.nome}: Vida já está no máximo! Kit não usado.")
            return

        # Usa o Kit
        self.kits_medicos -= 1
        nova_vida = self.vida_atual + cura_por_kit
        
        # Garante que a vida não exceda o máximo
        self.vida_atual = min(nova_vida, self.vida_maxima) 
        
        print(f"\n🩹 {self.nome} usou 1 Kit Médico.")
        print(f"Vida restaurada para {self.vida_atual}. Kits restantes: {self.kits_medicos}.")

    def status(self):
        """Exibe o status atual do jogador."""
        return f"[Status] {self.nome}: HP={self.vida_atual}/{self.vida_maxima} | Kits={self.kits_medicos}"

# --- Simulação de Combate ---

def iniciar_combate():
    """Sequência de eventos de combate e cura."""
    
    # 1. Preparação do Jogador
    jogador_principal = Jogador("Fera-Gamer")
    print("-" * 30)

    # 2. Primeira Troca de Tiros
    if jogador_principal.sofrer_dano(80): # Dano de um tiro de rifle
        print(jogador_principal.status())
        
        # Cura
        jogador_principal.usar_kit_medico()
        
        print("-" * 30)

    # 3. Segunda Troca de Tiros (Dano Alto)
    if jogador_principal.sofrer_dano(130): # Dano de um tiro de SVD
        print(jogador_principal.status())

        # Cura Sequencial
        print("\nTentando Curar Rapidamente...")
        jogador_principal.usar_kit_medico()
        jogador_principal.usar_kit_medico() 
        jogador_principal.usar_kit_medico() # Tenta usar um kit que não existe mais (teste)
        
        print("-" * 30)

    # 4. Resultado Final
    print("## FIM DA RODADA ##")
    print(jogador_principal.status())
    
    if jogador_principal.vida_atual > 0:
        print("✅ O jogador sobreviveu ao combate e escapou da troca de tiros!")
    else:
        print("❌ O jogador foi nocauteado.")

# Inicia a simulação
if __name__ == "__main__":
    iniciar_combate()