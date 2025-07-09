def build_nested_structure(level1, level2, level3, level4, level5, level6):
    '''
        ANIDAMIENTO POR NIVELES
    '''
    # Nivel 1 -> Nivel 2
    for cut1 in level1:
        children_level2 = [cut2 for cut2 in level2 if cut1["y2"] == cut2['y2']]
        if children_level2:  # Solo agregar si tiene elementos
            cut1["level2"] = children_level2
            
            # Nivel 2 -> Nivel 3
            for cut2 in cut1['level2']:
                children_level3 = [cut3 for cut3 in level3 if cut2["x2"] == cut3['x2']]
                if children_level3:  # Solo agregar si tiene elementos
                    cut2["level3"] = children_level3
                    
                    # Nivel 3 -> Nivel 4
                    for cut3 in cut2['level3']:
                        children_level4 = [cut4 for cut4 in level4 if cut3["y2"] == cut4['y2']]
                        if children_level4:  # Solo agregar si tiene elementos
                            cut3["level4"] = children_level4
                            
                            # Nivel 4 -> Nivel 5
                            for cut4 in cut3['level4']:
                                children_level5 = [cut5 for cut5 in level5 if cut4["x2"] == cut5['x2']]
                                if children_level5:  # Solo agregar si tiene elementos
                                    cut4["level5"] = children_level5
                                    
                                    # Nivel 5 -> Nivel 6
                                    for cut5 in cut4['level5']:
                                        children_level6 = [cut6 for cut6 in level6 if cut5["y2"] == cut6['y2']]
                                        if children_level6:  # Solo agregar si tiene elementos
                                            cut5["level6"] = children_level6
        
    return level1