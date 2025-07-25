def get_new_index(level, lastCut):
    index = level.index(lastCut)
    new_index = index + 1
    new_icut = lastCut['iCut'] + 1  
        
    return new_index, new_icut

def update_icut(new_index, level):
    for i, cut in enumerate(level):
        if i > new_index:
            cut['iCut'] += 1
    

def add_missing_cuts_from_internal(level1, level2, level3, level4, level5, level6, x1, x2, y1, y2):
    '''
        1. CASO DONDE EL ULTIMO CORTE NO EXISTE, PERO SI EXISTE CORTES INTERNOS
    '''
    
    # LEVEL 1 CREADO, CASO DONDE EL NIVEL 1 ESTA EN EXTREMO DE LA ALTURA DEL TABLERO Y HAY LEVEL 2 INTERNOS
    for cutLvl2 in level2:
        exist_cut_level1_created = any(cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == y2 and cutLvl1['x2'] == x2)
        if cutLvl2['y2'] == y2 and not exist_cut_level1_created:
            new_index, new_icut = get_new_index(level1, level1[len(level1) - 1])
            level1.insert(new_index, {
                "stockNo": "",
                "iCut": new_icut,
                "x1": x1,
                "y1": y1,
                "x2": x2,
                "y2": y2,
                "aLevel": 1,
                "type": "created"
            })
            update_icut(new_index, level1 + level2 + level3 + level4 + level5 + level6)
                

    # LEVEL 2 CREADO, CASO DONDE EL NIVEL 2 ESTA EN EXTREMO DEL ANCHO DEL TABLERO EN UNA TIRA Y HAY LEVEL 3 INTERNOS
            ##puede haber un caso donde un lvl2 previo no exista y se deba saber el lvl1 actual para tener el y2, es poco probable porque el optimizador lo consideraria lvl1
    for cutLvl3 in level3:
        #garantiza que ingrese solo una vez, es decir cree un solo corte, porque pueden haber varios niveles 3 en el mismo nivel 2 a crear
        exist_cut_level2_created = any(cutLvl2 for cutLvl2 in level2 if cutLvl2['x2'] == x2 and cutLvl2['y2'] == cutLvl3['y2'])
        if cutLvl3['x2'] == x2 and not exist_cut_level2_created: 
            lastCutsLvl2 = [cutLvl2 for cutLvl2 in level2 if cutLvl2["x1"] == cutLvl3["x1"] and cutLvl2['y1'] < cutLvl3['y2'] and cutLvl2['y2'] >= cutLvl3['y2']]
            if len(lastCutsLvl2):
                lastCutLvl2 = lastCutsLvl2[0]
                new_index, new_icut = get_new_index(level2, lastCutLvl2)
                level2.insert(new_index, {
                        "stockNo": "",
                        "iCut": new_icut,
                        "x1": x2,
                        "y1": lastCutLvl2['y1'],
                        "x2": x2,
                        "y2": lastCutLvl2['y2'],
                        "aLevel": 2,
                        "type": "created"
                    })
                update_icut(new_index, level2 + level3 + level4 + level5 + level6)
                
            
    # LEVEL 3 CREADO, CASO DONDE EL NIVEL 3 ESTA EN EXTREMO DEL ALTO DE LA TIRA DONDE SE ENCUENTRA, CONINCIDIENTO CON EL NIVEL 1 PREVIO, Y HAY NIVELES INTERNOS LEVEL 4
            ##puede haber un caso donde un lvl3 previo no exista y se deba saber el lvl1 previo para tener el y1, es poco probable porque el optimizador lo consideraria lvl2
    for cutLvl4 in level4:
        exist_cut_level3_created = any(cutLvl3 for cutLvl3 in level3 if cutLvl3['y2'] == cutLvl4['y2'] and cutLvl3['x1'] < cutLvl4['x2'] and cutLvl3['x2'] >= cutLvl4['x2'])
        if not exist_cut_level3_created:
            for cutLvl1 in level1:
                if cutLvl4['y2'] == cutLvl1["y2"]: 
                    lastCutsLvl3 = [cutLvl3 for cutLvl3 in level3 if cutLvl3["y1"] == cutLvl4["y1"] and cutLvl3['x1'] < cutLvl4['x1'] and cutLvl3['x2'] >= cutLvl4['x2']]
                    if len(lastCutsLvl3):
                        lastCutLvl3 = lastCutsLvl3[0]
                        new_index, new_icut = get_new_index(level3, lastCutLvl3)
                        level3.insert(new_index, {
                                "stockNo": "",
                                "iCut": new_icut,
                                "x1": lastCutLvl3['x1'],
                                "y1": cutLvl4['y2'],
                                "x2": lastCutLvl3['x2'],
                                "y2": cutLvl4['y2'],
                                "aLevel": 3,
                                "type": "created"
                        })
                        update_icut(new_index, level3 + level4 + level5 + level6)

    # LEVEL 4 CREADO, CASO DONDE EL NIVEL 4 ESTA EN EXTREMO DEL ANCHO, CONINCIDIENTO CON EL NIVEL 2 PREVIO,  Y HAY NIVELES INTERNOS LEVEL 5
            ##puede haber un caso donde un lvl4 previo no exista y se deba saber el lvl2 previo para tener el y1, es poco probable porque el optimizador lo consideraria lvl3
    for cutLvl5 in level5:
        exist_cut_level5_created = any(cutLvl4 for cutLvl4 in level4 if cutLvl4['x2'] == cutLvl5['x2'] and cutLvl4['y2'] == cutLvl5['y2'])
        if not exist_cut_level5_created:
            for cutLvl2 in level2:
                if cutLvl5['x2'] == cutLvl2["x2"]: 
                    lastCutsLvl4 = [cutLvl4 for cutLvl4 in level4 if cutLvl4["x1"] == cutLvl5["x1"] and cutLvl4['y1'] < cutLvl5['y1'] and cutLvl4['y2'] >= cutLvl5['y2']]
                    if len(lastCutsLvl4):
                        lastCutLvl4 = lastCutsLvl4[0]
                        new_index, new_icut = get_new_index(level4, lastCutLvl4)
                        level4.insert(new_index, {
                                "stockNo": "",
                                "iCut": new_icut,
                                "x1": cutLvl5['x2'],
                                "y1": lastCutLvl4['y1'],
                                "x2": cutLvl5['x2'],
                                "y2": lastCutLvl4['y2'],
                                "aLevel": 4,
                                "type": "created"
                            })
                        update_icut(new_index, level4 + level5 + level6)

    # LEVEL 5 CREADO, CASO DONDE EL NIVEL 5 ESTA EN EXTREMO DEL ALTO, CONINCIDIENTO CON EL NIVEL 3 PREVIO,  Y HAY NIVELES INTERNOS LEVEL 6
            ##puede haber un caso donde un lvl5 previo no exista y se deba saber el lvl3 previo para tener el x1 y x2, es poco probable porque el optimizador lo consideraria lvl3
    for cutLvl6 in level6:
        exist_cut_level5_created = any(cutLvl5 for cutLvl5 in level5 if cutLvl5['y2'] == cutLvl6['y2'] and cutLvl5['x1'] < cutLvl6['x2'] and cutLvl5['x2'] >= cutLvl6['x2'])
        if not exist_cut_level5_created:
            for cutLvl3 in level3:
                if cutLvl6['y2'] == cutLvl3["y2"]: 
                    lastCutsLvl5 = [cutLvl5 for cutLvl5 in level5 if cutLvl5["y1"] == cutLvl6["y1"] and cutLvl5['x1'] < cutLvl6['x1'] and cutLvl5['x2'] >= cutLvl6['x2']]
                    if len(lastCutsLvl5):
                        lastCutLvl5 = lastCutsLvl5[0]
                        new_index, new_icut = get_new_index(level5, lastCutLvl5)
                        level5.insert(new_index, {
                                "stockNo": "",
                                "iCut": new_icut,
                                "x1": lastCutLvl5['x1'],
                                "y1": cutLvl6['y2'],
                                "x2": lastCutLvl5['x2'],
                                "y2": cutLvl6['y2'],
                                "aLevel": 5,
                                "type": "created"
                            })
                        update_icut(new_index, level5 + level6)


def add_missing_cuts_from_parts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2):
    '''
        2. CASOS DONDE EL CORTE NO EXISTE PORQUE ESTA AL EXTREMO, PERO SACAN PIEZAS DIRECTAMENTE
        Los part['y'] es la coordenada superior izquierda de la pieza neta, es decir sin saneado inicial
    '''
    ## LEVEL 1 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
        
        if round(part['x'] + part_width + saw_width/2, 2) == round(x2, 2):
            cutLvl1 = [ cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == round(part['y'] + part_length + saw_width/2, 2) ]
            if len(cutLvl1) == 0:
                #Caso donde la tira esta al final del eje Y, debe crear unn corte nivel 1
                new_index, new_icut = get_new_index(level1, level1[len(level1) - 1])
                level1.insert(new_index, {
                    "stockNo": "",
                    "iCut": new_icut,
                    "x1": x1,
                    "y1": y2,
                    "x2": x2,
                    "y2": y2,
                    "aLevel": 1,
                    "type": "created"
                })
                update_icut(new_index, level1 + level2 + level3 + level4 + level5 + level6)
                
            #Este o no al final del eje Y, la tira necesita un Corte nivel 2 creado en el lado derecho de la tira para el refilado
            cutLvl1_father_upper = [cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == round(part['y'] - saw_width/2, 2)]
            lastCutsLvl2 = None
            if len(cutLvl1_father_upper) == 1:
                cutLvl1_upper = cutLvl1_father_upper[0]
                cutsLvl2_upper = [cutLvl2 for cutLvl2 in level2 if cutLvl2['y2'] == cutLvl1_upper['y2']]
                cutsLvl2_upper = sorted(cutsLvl2_upper, key=lambda cutLvl2: cutLvl2['x2'], reversed=True)
                lastCutsLvl2 = cutsLvl2_upper[0]
            
            new_index, new_icut = 0, 1 if lastCutsLvl2 is None else get_new_index(level2, lastCutsLvl2)
            level2.insert(new_index, {
                "stockNo": "",
                "iCut": new_icut,
                "x1": x2,
                "y1": round(part['y'] - saw_width/2, 2),
                "x2": x2,
                "y2": round(part['y'] + part_length + saw_width/2, 2),
                "aLevel": 2,
                "type": "created"
            })
            update_icut(new_index, level2 + level3 + level4 + level5 + level6)
            
    # LEVEL 2 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
                
        if round(part['x'] + part_width + saw_width/2, 2) == round(x2, 2) and round(part['x'] - saw_width/2 , 2) != x1:
            cutLvl1_father = [cutLvl1 for cutLvl1 in level1 if cutLvl1['y2'] == round(part['y'] + part_length + saw_width/2, 2)]
            lastCutsLvl2 = [cutLvl2 for cutLvl2 in level2 if cutLvl2['y2'] == cutLvl1_father[0]['y2']]
            lastCutsLvl2 = sorted(lastCutsLvl2, key=lambda cut: cut['x2'], reverse=True)
            
            if len(lastCutsLvl2):
                new_index, new_icut = get_new_index(level2, lastCutsLvl2[0])
                level2.insert(new_index, {
                    "stockNo": "",
                    "iCut": new_icut,
                    "x1": x2,
                    "y1": round(part['y'] - saw_width/2, 2),
                    "x2": x2,
                    "y2": round(part['y'] + part_length + saw_width/2, 2),
                    "aLevel": 2,
                    "type": "created"
                })
                update_icut(new_index, level2 + level3 + level4 + level5 + level6)

    # LEVEL 3 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
        for cutLvl2 in level2:
            #garantiza que el corte que genera la pieza no es nivel 2, sino que es nivel 3 y falta crear
            exist_cutLvl3_prev = any(cutLvl3 for cutLvl3 in level3 if cutLvl3['x2'] == cutLvl2['x2'] and cutLvl3['y1'] > cutLvl2['y1'] and cutLvl3['y2'] < cutLvl2['y2'] and round(cutLvl3['x2'], 2) == round(part['x'] + part_width + saw_width/2, 2))
            if round(part['y'] + part_length + saw_width/2, 2) == round(cutLvl2['y2'], 2) and exist_cutLvl3_prev:
                lastCutsLvl3 = [cutLvl3 for cutLvl3 in level3 if cutLvl3['x2'] == cutLvl2['x2'] and cutLvl3['y1'] > cutLvl2['y1'] and cutLvl3['y2'] < cutLvl2['y2'] and round(cutLvl3['x2'], 2) == round(part['x'] + part_width + saw_width/2, 2)]
                lastCutsLvl3 = sorted(lastCutsLvl3, key=lambda cut: cut['y2'], reverse=True)
                
                if len(lastCutsLvl3):
                    new_index, new_icut = get_new_index(level3, lastCutsLvl3[0])
                    level3.insert(new_index, {
                        "stockNo": "",
                        "iCut": new_icut,
                        "x1": round(part['x'] - saw_width/2, 2),                                           
                        "y1": cutLvl2['y2'],                                  
                        "x2": round(part['x'] + part_width + saw_width/2, 2),
                        "y2": cutLvl2['y2'],                                  
                        "aLevel": 3,
                        "type": "created"
                    })
                    update_icut(new_index, level3 + level4 + level5 + level6)

    # LEVEL 4 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
        for cutLvl3 in level3:
            #garantiza que el corte que genera la pieza no es nivel 3, sino que es nivel 4 y falta crear
            exist_cutLvl4_prev = any(cutLvl4 for cutLvl4 in level4 if cutLvl4['y2'] == cutLvl3['y2'] and cutLvl4['x2'] > cutLvl3['x1'] and cutLvl4['x2'] < cutLvl3['x2'] and round(cutLvl4['y2'], 2) == round(part['y'] + part_length + saw_width/2 , 2))
            
            if round(part['x'] + part_width + saw_width/2, 2) == round(cutLvl3['x2'], 2) and exist_cutLvl4_prev:
                lastCutsLvl4 = [cutLvl4 for cutLvl4 in level4 if cutLvl4['y2'] == cutLvl3['y2'] and cutLvl4['x2'] > cutLvl3['x1'] and cutLvl4['x2'] < cutLvl3['x2'] and round(cutLvl4['y2'], 2) == round(part['y'] + part_length + saw_width/2 , 2)]
                lastCutsLvl4 = sorted(lastCutsLvl4, key=lambda cut: cut['x2'], reverse=True)

                if len(lastCutsLvl4):
                    new_index, new_icut = get_new_index(level4, lastCutsLvl4[0])
                    level4.insert(new_index, {
                        "stockNo": "",
                        "iCut": new_icut,
                        "x1": cutLvl3['x2'],                                 
                        "y1": round(part['y'] - saw_width/2, 2),                                     
                        "x2": cutLvl3['x2'],                               
                        "y2": round(part['y'] + part_length + saw_width/2, 2), 
                        "aLevel": 4,
                        "type": "created"
                    })
                    update_icut(new_index, level4 + level5 + level6)
        
    # LEVEL 5 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
        for cutLvl4 in level4:
            #garantiza que el corte que genera la pieza no es nivel 4, sino que es nivel 5 y falta crear
            exist_cutLvl5_prev = any(cutLvl5 for cutLvl5 in level5 if cutLvl5['x2'] == cutLvl4['x2'] and cutLvl5['y1'] > cutLvl4['y1'] and cutLvl5['y2'] < cutLvl4['y2'] and round(cutLvl5['x2'], 2) == round(part['x'] + part_width + saw_width/2, 2))
            
            if round(part['y'] + part_length + saw_width/2, 2) == round(cutLvl4['y2'], 2) and exist_cutLvl5_prev:
                lastCutsLvl5 = [cutLvl5 for cutLvl5 in level5 if cutLvl5['x2'] == cutLvl4['x2'] and cutLvl5['y1'] > cutLvl4['y1'] and cutLvl5['y2'] < cutLvl4['y2'] and round(cutLvl5['x2'], 2) == round(part['x'] + part_width + saw_width/2, 2)]
                lastCutsLvl5 = sorted(lastCutsLvl5, key=lambda cut: cut['y2'], reverse=True)
                
                if len(lastCutsLvl5):
                    new_index, new_icut = get_new_index(level5, lastCutsLvl5[0])
                    level5.insert(new_index, {
                        "stockNo": "",
                        "iCut": new_icut,
                        "x1": round(part['x'] - saw_width/2, 2),                                      
                        "y1": cutLvl4['y2'],                            
                        "x2": round(part['x'] + part_width + saw_width/2, 2), 
                        "y2": cutLvl4['y2'],                          
                        "aLevel": 5,
                        "type": "created"
                    })
                    update_icut(new_index, level5 + level6)

    # LEVEL 6 CREADO, PORQUE ESTE GENERA UNA PIEZA DIRECTAMENTE
    for part in parts:
        part_width = part['width'] if part['rotated'] is False else part['length']
        part_length = part['length'] if part['rotated'] is False else part['width']
        for cutLvl5 in level5:
            #garantiza que el corte que genera la pieza no es nivel 4, sino que es nivel 5 y falta crear
            exist_cutLvl6_prev = any(cutLvl6 for cutLvl6 in level6 if cutLvl6['y2'] == cutLvl5['y2'] and cutLvl6['x2'] > cutLvl5['x1'] and cutLvl6['x2'] < cutLvl5['x2'] and round(cutLvl5['x2'], 2) == round(part['y'] + part_length + saw_width/2 , 2))
            
            if round(part['x'] + part_width + saw_width/2, 2) == round(cutLvl5['x2'], 2) and exist_cutLvl6_prev:
                lastCutsLvl6 = [cutLvl6 for cutLvl6 in level6 if cutLvl6['y2'] == cutLvl5['y2'] and cutLvl6['x2'] > cutLvl5['x1'] and cutLvl6['x2'] < cutLvl5['x2'] and round(cutLvl5['x2'], 2) == round(part['y'] + part_length + saw_width/2 , 2)]
                lastCutsLvl6 = sorted(lastCutsLvl6, key=lambda cut: cut['x2'], reverse=True)
                
                if len(lastCutsLvl6):
                    new_index, new_icut = get_new_index(level6, lastCutsLvl6[0])
                    level6.insert(new_index, {
                        "stockNo": "",
                        "iCut": new_icut,
                        "x1": cutLvl5['x2'],                           
                        "y1": round(part['y'] - saw_width/2, 2),                                
                        "x2": cutLvl5['x2'],                             
                        "y2": round(part['y'] + part_length + saw_width/2, 2),
                        "aLevel": 6,
                        "type": "created"
                    })
                    update_icut(new_index, level6)

def process_sanitation_cuts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2):
    """
    Procesa los datos de corte y sanea los cortes faltantes
    """
    add_missing_cuts_from_internal(level1, level2, level3, level4, level5, level6, x1, x2, y1, y2)
   
    add_missing_cuts_from_parts(level1, level2, level3, level4, level5, level6, parts, saw_width, x1, x2, y1, y2)
    
    return level1, level2, level3, level4, level5, level6, parts