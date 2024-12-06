


def lang(language):

    levels_fr = {
        "facil": ["agenda", "ami", "souris"],
        "intermedio": ["ordinateur", "algorithme", "développeur"],
        "dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle"]
    }

    levels_it = {
        "facil": ["agenda", "amico", "topo"],
        "intermedio": ["computer", "algoritmo", "sviluppatore"],
        "dificil": ["rete neurale", "apprendimento automatico", "intelligenza artificiale"]
    }

    levels_pt = {
        "facil": ["agenda", "amigo", "rato"],
        "intermedio": ["computador", "algoritmo", "desenvolvedor"],
        "dificil": ["rede neural", "aprendizado de máquina", "inteligência artificial"]
    }

    levels_en = {
        "facil": ["book", "friend", "mouse"],
        "intermedio": ["computer", "algorithm", "developer"],
        "dificil": ["neural network", "machine learning", "artificial intelligence"]
    }
    if language == 'ingles':
        return levels_en
    elif language == 'portugues':
        return levels_pt
    elif language == 'italiano':
        return levels_it
    elif language == 'frances':
        return levels_fr
