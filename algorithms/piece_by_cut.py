def add_piece_by_cut(level1, level2, level3, level4, level5, level6, parts, trim, saw_width):
    """
    Si el corte saca pieza, setea el identificador de la pieza en el corte.
    """    
    
    #NIVEL 1
    for cutLvl1 in level1:
        
        #Calcular la altura de la tira
        height_strip = 0
        if(cutLvl1['iCut'] == 0):
            height_strip = cutLvl1['y2'] - saw_width / 2 - trim
        else:
            prev_cut = next((cut for cut in level1 if cut['iCut'] == cutLvl1['iCut'] - 1), None)
            height_strip = cutLvl1['y2'] - prev_cut['y2'] - saw_width
        
        # Verificar si tiene cortes internos (nivel 2), osea no saca pieza
        has_internal_cuts = any(cutLvl2['y2'] == cutLvl1['y2'] for cutLvl2 in level2)

        part_index = 0
        if(not has_internal_cuts and height_strip != 0):
            #Buscar la parte correspondiente al corte  
            for part in parts:
                if part['rotated'] == True:
                    if (
                        round(height_strip, 2) == round(part['width'], 2)
                        and round(part['y'] + part['width'] + saw_width/2, 2) == round(cutLvl1['y2'], 2)
                        and round(cutLvl1['x1'] + saw_width/2, 2)== round(part['x'], 2)
                    ):
                        part_index = part['nItem']
                else:
                    if (
                        round(height_strip, 2) == round(part['length'], 2) 
                        and round(part['y'] + part['length'] + saw_width/2, 2) == round(cutLvl1['y2'], 2)
                        and round(cutLvl1['x1'] + saw_width/2, 2) == round(part['x'], 2)
                    ):
                        part_index = part['nItem']
        
        cutLvl1['nItem'] = part_index
        
    #NIVEL 2
    for cutLvl2 in level2:
        
        width_strip = 0

        cut_level1_father = next((cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == cutLvl2['y2']), None)
        
        prev_cut_level2 = next((prevCutLvl2 for prevCutLvl2 in level2 if prevCutLvl2['iCut'] == cutLvl2['iCut'] - 1 and prevCutLvl2['y1'] == cutLvl2['y1'] and prevCutLvl2['y2'] == cutLvl2['y2'] and prevCutLvl2['y2'] == cut_level1_father['y2']), None)
                
        if prev_cut_level2 is not None:
            width_strip = cutLvl2['x2'] - prev_cut_level2['x2'] - saw_width
        else:
            width_strip = cutLvl2['x2'] - saw_width/2 - trim
            
        # Verificar si tiene cortes internos (nivel 3), osea no saca pieza
        has_internal_cuts = any(
            cutLvl3['x2'] == cutLvl2['x2'] 
            and cutLvl3['y2'] > cutLvl2['y1'] 
            and cutLvl3['y2'] <= cutLvl2['y2'] 
            for cutLvl3 in level3
        )

        part_index = 0                   
        if not has_internal_cuts:
            #Buscar la parte correspondiente al corte 
            for part in parts:
                if part['rotated'] == True:
                    if (
                        round(width_strip, 2) == round(part['length'], 2)
                        and round(part['x'] + part['length'] + saw_width/2) == round(cutLvl2['x2'])
                        and round(cutLvl2['y1'] + saw_width/2, 2) == round(part['y'], 2)
                    ):
                        part_index = part['nItem']
                else:
                    if (
                        round(width_strip, 2) == round(part['width'], 2)
                        and round(part['x'] + part['width'] + saw_width/2, 2) == round(cutLvl2['x2'], 2)
                        and round(cutLvl2['y1'] + saw_width/2, 2) == round(part['y'], 2)
                    ):
                        part_index = part['nItem']
        
        cutLvl2['nItem'] = part_index
        
    #NIVEL 3
    for cutLvl3 in level3:
        height_strip = 0
        
        cut_level2_father = next((cutLvl2 for cutLvl2 in level2 if cutLvl2['x2'] == cutLvl3['x2'] and cutLvl2['y1'] < cutLvl3['y2'] and cutLvl2['y2'] >= cutLvl3['y2']), None)
    
        cut_level1_father = next((cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == cut_level2_father['y2']), None)
        prev_cut_level1_father = next((cutLvl1 for cutLvl1 in level1 if cutLvl1['iCut'] == cut_level1_father['iCut'] - 1 and cutLvl1['y2'] == cut_level2_father['y1']), None)
        
        prev_cut_level3 = next((prevCutLvl3 for prevCutLvl3 in level3 if prevCutLvl3['iCut'] == cutLvl3['iCut'] - 1 and prevCutLvl3['x1'] == cutLvl3['x1'] and prevCutLvl3['x2'] == cutLvl3['x2'] and prevCutLvl3['x2'] == cut_level2_father['x2']), None)
        
        if prev_cut_level3 is not None:
            height_strip = cutLvl3['y2'] - prev_cut_level3['y2'] - saw_width
        else:
            if prev_cut_level1_father is not None:
                height_strip = cutLvl3['y2'] - prev_cut_level1_father['y2'] - saw_width
            else:
                height_strip = cutLvl3['y2'] - saw_width/2 - trim
                
        # Verificar si tiene cortes internos en el siguiente nivel (nivel 4), o sea, no saca pieza aún
        has_internal_cuts = any(
            cutLvl4['y2'] == cutLvl3['y2'] 
            and cutLvl3['x1'] < cutLvl4['x2'] 
            and cutLvl3['x2'] >= cutLvl4['x2'] 
            for cutLvl4 in level4
        )

        part_index = 0
        if not has_internal_cuts:
            for part in parts:
                if part['rotated'] == True:
                    if (
                        round(height_strip, 2) == round(part['width'], 2)
                        and round(part['y'] + part['width'] + saw_width/2, 2) == round(cutLvl3['y2'], 2) 
                        and round(cutLvl3['x1'] + saw_width/2, 2) == round(part['x'], 2)
                    ):
                        part_index = part['nItem']
                else:
                    if (
                        round(height_strip, 2) == round(part['length'], 2)
                        and round(part['y'] + part['length'] + saw_width/2, 2) == round(cutLvl3['y2'], 2)
                        and round(cutLvl3['x1'] + saw_width/2, 2) == round(part['x'], 2)
                    ):
                        part_index = part['nItem']

        cutLvl3['nItem'] = part_index
    
    #NIVEL 4
    for cutLvl4 in level4:
        width_strip = 0

        # Buscar el padre en nivel 3
        cut_level3_father = next(
            (
                cutLvl3 for cutLvl3 in level3
                if cutLvl3['y2'] == cutLvl4['y2']
                and cutLvl3['x1'] < cutLvl4['x2']
                and cutLvl3['x2'] >= cutLvl4['x2']
            ),
            None
        )

        # Buscar el padre en nivel 2, en caso se necesite para cortes iniciales 
        cut_level2_father = next(
            (
                cutLvl2 for cutLvl2 in level2 
                if cutLvl2['x2'] == cut_level3_father['x2'] 
                and cutLvl2['y1'] < cut_level3_father['y2'] 
                and cutLvl2['y2'] >= cut_level3_father['y2']
            ),
            None
        )
        
        prev_cut_level2_father = next(
            (
                cutLvl2 for cutLvl2 in level2 
                if cutLvl2['iCut'] == cut_level2_father['iCut'] - 1 
                and cutLvl2['y1'] == cut_level2_father['y1']
                and cutLvl2['y2'] == cut_level2_father['y2']
                and cutLvl2['x2'] == cut_level3_father['x1']
             ),
            None
        ) if cut_level2_father is not None and cut_level3_father is not None else None

        # Buscar corte previo (hermano anterior) en nivel 4
        prev_cut_level4 = next(
            (
                prevCutLvl4 for prevCutLvl4 in level4
                if prevCutLvl4['iCut'] == cutLvl4['iCut'] - 1
                and prevCutLvl4['y1'] == cutLvl4['y1']
                and prevCutLvl4['y2'] == cutLvl4['y2']
                and prevCutLvl4['y2'] == cut_level3_father['y2']
            ),
            None
        )

        if prev_cut_level4 is not None:
            width_strip = cutLvl4['x2'] - prev_cut_level4['x2'] - saw_width
        else:
            if prev_cut_level2_father is not None:
                width_strip = cutLvl4['x2'] - prev_cut_level2_father['x1'] - saw_width
            else:
                width_strip = cutLvl4['x2'] - saw_width/2 - trim

        # Verificar si tiene cortes internos (nivel 5), o sea, no saca pieza aún
        has_internal_cuts = any(
            cutLvl5['x2'] == cutLvl4['x2']
            and cutLvl5['y2'] > cutLvl4['y1']
            and cutLvl5['y2'] <= cutLvl4['y2']
            for cutLvl5 in level5
        )

        part_index = 0
        if not has_internal_cuts:
            for part in parts:
                if part['rotated'] == True:
                    if (
                        round(width_strip, 2) == round(part['length'], 2)
                        and round(part['x'] + part['length'] + saw_width/2, 2) == round(cutLvl4['x2'], 2)
                        and round(cutLvl4['y1'] + saw_width/2, 2) == round(part['y'], 2)
                    ):
                        part_index = part['nItem']
                else:
                    if (
                        round(width_strip, 2) == round(part['width'], 2)
                        and round(part['x'] + part['width'] + saw_width/2, 2) == round(cutLvl4['x2'], 2)
                        and round(cutLvl4['y1'] + saw_width/2, 2) == round(part['y'], 2)
                    ):
                        part_index = part['nItem']

        cutLvl4['nItem'] = part_index

    # NIVEL 5
    for cutLvl5 in level5:
        height_strip = 0

        # Buscar el padre en nivel 4 (vertical)
        cut_level4_father = next(
            (
                cutLvl4 for cutLvl4 in level4
                if cutLvl4['x2'] == cutLvl5['x2']
                and cutLvl4['y1'] < cutLvl5['y2']
                and cutLvl4['y2'] >= cutLvl5['y2']
            ),
            None
        )

        # Buscar el padre en nivel 3 (horizontal)
        cut_level3_father = next(
            (
                cutLvl3 for cutLvl3 in level3
                if cutLvl3['y2'] == cut_level4_father['y2']
                and cutLvl3['x1'] < cut_level4_father['x2']
                and cutLvl3['x2'] >= cut_level4_father['x2']
            ),
            None
        )

        # Buscar el padre en nivel 2 (vertical) del padre nivel 3
        cut_level2_father = next(
            (
                cutLvl2 for cutLvl2 in level2
                if cutLvl2['x2'] == cut_level3_father['x2']
                and cutLvl2['y1'] < cut_level3_father['y2']
                and cutLvl2['y2'] >= cut_level3_father['y2']
            ),
            None
        )

        # Buscar el padre en nivel 1 (horizontal) del padre nivel 2
        cut_level1_father = next(
            (
                cutLvl1 for cutLvl1 in level1
                if cutLvl1['y2'] == cut_level2_father['y2']
            ),
            None
        )

        # 1. Corte previo en nivel 5 (hermano anterior)
        prev_cut_level5 = next(
            (
                prevCutLvl5 for prevCutLvl5 in level5
                if prevCutLvl5['iCut'] == cutLvl5['iCut'] - 1
                and prevCutLvl5['x1'] == cutLvl5['x1']
                and prevCutLvl5['x2'] == cutLvl5['x2']
                and prevCutLvl5['x2'] == cut_level4_father['x2']
            ),
            None
        )

        # 2. Corte previo en nivel 3 (hermano anterior del padre nivel 3)
        prev_cut_level3_father = next(
            (
                cutLvl3 for cutLvl3 in level3
                if cutLvl3['iCut'] == cut_level3_father['iCut'] - 1
                and cutLvl3['x1'] == cut_level3_father['x1']
                and cutLvl3['x2'] == cut_level3_father['x2']
            ),
            None
        )

        # 3. Corte previo en nivel 1 (hermano anterior del padre nivel 1)
        prev_cut_level1_father = next(
            (
                cutLvl1 for cutLvl1 in level1
                if cutLvl1['iCut'] == cut_level1_father['iCut'] - 1
            ),
            None
        )

        # Cálculo del height_strip con lógica jerárquica
        if prev_cut_level5 is not None:
            height_strip = cutLvl5['y2'] - prev_cut_level5['y2'] - saw_width
        elif prev_cut_level3_father is not None:
            height_strip = cutLvl5['y2'] - prev_cut_level3_father['y2'] - saw_width
        elif prev_cut_level1_father is not None:
            height_strip = cutLvl5['y2'] - prev_cut_level1_father['y2'] - saw_width
        else:
            height_strip = cutLvl5['y2'] - saw_width/2 - trim

        # Verificar si tiene cortes internos en nivel 6 (verticales)
        has_internal_cuts = any(
            cutLvl6['y2'] == cutLvl5['y2']
            and cutLvl6['x1'] < cutLvl5['x2']
            and cutLvl6['x2'] >= cutLvl5['x2']
            for cutLvl6 in level6
        )

        part_index = 0
        if not has_internal_cuts:
            for part in parts:
                if part['rotated'] == True:
                    if (
                        round(height_strip, 2) == round(part['width'], 2)
                        and round(part['y'] + part['width'] + saw_width/2, 2) == round(cutLvl5['y2'], 2)
                        and round(cutLvl5['x1'] + saw_width/2, 2) == round(part['x'], 2)
                    ):
                        part_index = part['nItem']
                else:
                    if (
                        round(height_strip, 2) == round(part['length'], 2)
                        and round(part['y'] + part['length'] + saw_width/2, 2) == round(cutLvl5['y2'], 2)
                        and round(cutLvl5['x1'] + saw_width/2, 2) == round(part['x'], 2)
                    ):
                        part_index = part['nItem']

        cutLvl5['nItem'] = part_index
    
    # NIVEL 6
    for cutLvl6 in level6:
        width_strip = 0

        # Padre en nivel 5 (horizontal)
        cut_level5_father = next(
            (
                cutLvl5 for cutLvl5 in level5
                if cutLvl5['y2'] == cutLvl6['y2']
                and cutLvl5['x1'] < cutLvl6['x2']
                and cutLvl5['x2'] >= cutLvl6['x2']
            ),
            None
        )

        # Padre en nivel 4 (vertical)
        cut_level4_father = next(
            (
                cutLvl4 for cutLvl4 in level4
                if cutLvl4['x2'] == cut_level5_father['x2']
                and cutLvl4['y1'] < cut_level5_father['y2']
                and cutLvl4['y2'] >= cut_level5_father['y2']
            ),
            None
        )

        # Padre en nivel 3 (horizontal)
        cut_level3_father = next(
            (
                cutLvl3 for cutLvl3 in level3
                if cutLvl3['y2'] == cut_level4_father['y2']
                and cutLvl3['x1'] < cut_level4_father['x2']
                and cutLvl3['x2'] >= cut_level4_father['x2']
            ),
            None
        )

        # Padre en nivel 2 (vertical)
        cut_level2_father = next(
            (
                cutLvl2 for cutLvl2 in level2
                if cutLvl2['x2'] == cut_level3_father['x2']
                and cutLvl2['y1'] < cut_level3_father['y2']
                and cutLvl2['y2'] >= cut_level3_father['y2']
            ),
            None
        )

        # 1. Corte previo en nivel 6 (hermano anterior)
        prev_cut_level6 = next(
            (
                prevCutLvl6 for prevCutLvl6 in level6
                if prevCutLvl6['iCut'] == cutLvl6['iCut'] - 1
                and prevCutLvl6['y1'] == cutLvl6['y1']
                and prevCutLvl6['y2'] == cutLvl6['y2']
                and prevCutLvl6['y2'] == cut_level5_father['y2']
            ),
            None
        )

        # 2. Corte previo en nivel 4 (hermano anterior del padre nivel 4)
        prev_cut_level4_father = next(
            (
                cutLvl4 for cutLvl4 in level4
                if cutLvl4['iCut'] == cut_level4_father['iCut'] - 1
                and cutLvl4['y1'] == cut_level4_father['y1']
                and cutLvl4['y2'] == cut_level4_father['y2']
                and cutLvl4['x2'] == cut_level5_father['x1']
            ),
            None
        )

        # 3. Corte previo en nivel 2 (hermano anterior del padre nivel 2, respecto a nivel 3)
        prev_cut_level2_father = next(
            (
                cutLvl2 for cutLvl2 in level2
                if cutLvl2['iCut'] == cut_level2_father['iCut'] - 1
                and cutLvl2['y1'] == cut_level2_father['y1']
                and cutLvl2['y2'] == cut_level2_father['y2']
                and cutLvl2['x2'] == cut_level3_father['x1']
            ),
            None
        )

        # Cálculo del width_strip con lógica jerárquica
        if prev_cut_level6 is not None:
            width_strip = cutLvl6['x2'] - prev_cut_level6['x2'] - saw_width
        elif prev_cut_level4_father is not None:
            width_strip = cutLvl6['x2'] - prev_cut_level4_father['x1'] - saw_width
        elif prev_cut_level2_father is not None:
            width_strip = cutLvl6['x2'] - prev_cut_level2_father['x1'] - saw_width
        else:
            width_strip = cutLvl6['x2'] - saw_width/2 - trim

        # En nivel 6 ya no hay más cortes internos, así que piezas finales
        part_index = 0
        for part in parts:
            if part['rotated'] == True:
                if (
                    round(width_strip, 2) == round(part['length'], 2)
                    and round(part['x'] + part['length'] + saw_width/2, 2) == round(cutLvl6['x2'], 2)
                    and round(cutLvl6['y1'] + saw_width/2, 2) == round(part['y'], 2)
                ):
                    part_index = part['nItem']
            else:
                if (
                    round(width_strip, 2) == round(part['width'], 2)
                    and round(part['x'] + part['width'] + saw_width/2, 2) == round(cutLvl6['x2'], 2)
                    and round(cutLvl6['y1'] + saw_width/2, 2) == round(part['y'], 2)
                ):
                    part_index = part['nItem']

        cutLvl6['nItem'] = part_index
        
    return level1, level2, level3, level4, level5, level6