"""Funções para implementar as regras do clássico jogo arcade Pac-Man."""
def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """Verifique se o Pac-Man pode comer um fantasma se for fortalecido por uma bolinha de energia.
    """
    return power_pellet_active and touching_ghost
def score(touching_power_pellet: bool, touching_dot: bool) -> bool:
    """Verifique se o Pac-Man marcou quando um pellet ou ponto de energia foi comido.
    """
    return touching_power_pellet or touching_dot
def lose(power_pellet_active, touching_ghost):
    """Acione o loop do jogo para terminar (GAME OVER) quando Pac-Man toca um fantasma sem seu pellet de energia.
    """
    return touching_ghost and not power_pellet_active
def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Acione o evento de vitória quando todos os pontos forem consumidos.
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)
