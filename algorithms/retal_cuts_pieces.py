def add_retal_cut_pieces(sorted_structure, parts, saw_width, x1, x2, y1, y2):
    '''
        AGREGANDO PIEZAS  Y CORTES DE RETAL A CADA NIVEL DE CORTES
    '''
    index = 10000
    
    #NIVEL 1
    last_cut_level1 = sorted_structure[len(sorted_structure) - 1]
    if last_cut_level1['y2'] < y2:
        cut_level1_retal = {
            "x1": x1,
            "y1": y2,
            "x2": x2,
            "y2": y2,
            "aLevel": 1,
            "nItem": index,
            "type": 'retal'
        }
        part_retal = {
            "x": round(last_cut_level1["x1"] + saw_width/2, 2),
            "y": round(last_cut_level1["y1"] + saw_width/2, 2),
            "length": round(y2 - last_cut_level1["y1"] - saw_width),
            "width": round(x2 - last_cut_level1["x1"] - saw_width),
            "nItem": index,
            "rotated": False,
            "type": 'retal'
        }
        sorted_structure.append(cut_level1_retal)
        parts.append(part_retal)
        index += 1
        
        
    for cutLvl1 in sorted_structure:
        
        #NIVEL 2
        cuts_level2 = cutLvl1.get('level2', [])
        if cuts_level2: 
            last_cut_level2 = cuts_level2[len(cuts_level2) - 1]
            if last_cut_level2['x2'] < x2:
                cut_level2_retal = {
                    "x1": x2,
                    "y1": last_cut_level2['y1'],
                    "x2": x2,
                    "y2": last_cut_level2['y2'],
                    "aLevel": 2,
                    "nItem": index,
                    "type": 'retal'
                }
                part_retal = {
                    "x": round(last_cut_level2["x1"] + saw_width/2, 2),
                    "y": round(last_cut_level2["y1"] + saw_width/2, 2),
                    "length": round(last_cut_level2["y2"] - last_cut_level2["y1"] - saw_width, 2),
                    "width": round(x2 - last_cut_level2["x2"] - saw_width, 2),
                    "nItem": index,
                    "rotated": False,
                    "type": 'retal'
                }
                cuts_level2.append(cut_level2_retal)
                parts.append(part_retal)
                index += 1
            
            #NIVEL 3
            for cutLvl2 in cuts_level2:
                cuts_level3 = cutLvl2.get('level3', [])
                if cuts_level3:
                    last_cut_level3 = cuts_level3[len(cuts_level3) - 1]
                    if last_cut_level3['y2'] < cutLvl1['y2']: #padre inmediato paralelo
                        cut_level3_retal = {
                            "x1": last_cut_level3['x1'],
                            "y1": cutLvl1['y2'],
                            "x2": last_cut_level3['x2'],
                            "y2": cutLvl1['y2'],
                            "aLevel": 3,
                            "nItem": index,
                            "type": 'retal'
                        }
                        part_retal = {
                            "x": round(last_cut_level3["x1"] + saw_width/2, 2),
                            "y": round(last_cut_level3["y1"] + saw_width/2, 2),
                            "length": round(cutLvl1['y2'] - last_cut_level3["y1"] - saw_width, 2),
                            "width": round(last_cut_level3['x2'] - last_cut_level3["x1"] - saw_width, 2),
                            "nItem": index,
                            "rotated": False,
                            "type": 'retal'
                        }
                        cuts_level3.append(cut_level3_retal)
                        parts.append(part_retal)
                        index += 1
                        
                    #NIVEL 4
                    for cutLvl3 in cuts_level3:
                        cuts_level4 = cutLvl3.get('level4', [])
                        if cuts_level4:
                            last_cut_level4 = cuts_level4[len(cuts_level4) - 1]
                            if last_cut_level4['x2'] < cutLvl2['x2']:
                                cut_level4_retal = {
                                    "x1": cutLvl2['x2'],
                                    "y1": last_cut_level4['y1'],
                                    "x2": cutLvl2['x2'],
                                    "y2": last_cut_level4['y2'],
                                    "aLevel": 4,
                                    "nItem": index,
                                    "type": 'retal'
                                }
                                part_retal = {
                                    "x": round(last_cut_level4['x1'] + saw_width/2, 2),
                                    "y": round(last_cut_level4["y1"] + saw_width/2, 2),
                                    "length": round(last_cut_level3["y2"] - last_cut_level4["y1"] - saw_width, 2),
                                    "width": round(cutLvl2['x2'] - last_cut_level4["x2"] - saw_width, 2),
                                    "nItem": index,
                                    "rotated": False,
                                    "type": 'retal'
                                }
                                cuts_level4.append(cut_level4_retal)
                                parts.append(part_retal)
                                index += 1
                        
                        #NIVEL 5
                        for cutLvl4 in cuts_level4:
                            cuts_level5 = cutLvl4.get('level5', [])
                            if cuts_level5:
                                last_cut_level5 = cuts_level5[len(cuts_level5) - 1]
                                if last_cut_level5['y2'] < cutLvl3['y2']:
                                    cut_level5_retal = {
                                        "x1": last_cut_level5['x1'],
                                        "y1": cutLvl3['y2'],
                                        "x2": last_cut_level5['x2'],
                                        "y2": cutLvl3['y2'],
                                        "aLevel": 5,
                                        "nItem": index,
                                        "type": 'retal'
                                    }
                                    part_retal = {
                                        "x": round(last_cut_level5["x1"] + saw_width/2, 2),
                                        "y": round(last_cut_level5["y1"] + saw_width/2, 2),
                                        "length": round(cutLvl3['y2'] - last_cut_level5["y1"] - saw_width, 2),
                                        "width": round(last_cut_level5['x2'] - last_cut_level5["x1"] - saw_width, 2),
                                        "nItem": index,
                                        "rotated": False,
                                        "type": 'retal'
                                    }
                                    cuts_level5.append(cut_level5_retal)
                                    parts.append(part_retal)
                                    index += 1
                                    
                            #NIVEL 6
                            for cutLvl5 in cuts_level5:
                                cuts_level6 = cutLvl5.get('level6', [])
                                if cuts_level6:
                                    last_cut_level6 = cuts_level6[len(cuts_level6) - 1]
                                    if last_cut_level6['x2'] < cutLvl4['x2']:
                                        cut_level6_retal = {
                                            "x1": cutLvl4['x2'],
                                            "y1": last_cut_level6['y1'],
                                            "x2": cutLvl4['x2'],
                                            "y2": last_cut_level6['y2'],
                                            "aLevel": 6,
                                            "nItem": index,
                                            "type": 'retal'
                                        }
                                        part_retal = {
                                            "x": round(last_cut_level6["x1"] + saw_width/2, 2),
                                            "y": round(last_cut_level6["y1"] + saw_width/2, 2),
                                            "length": round(last_cut_level5["y2"] - last_cut_level6["y1"] - saw_width, 2),
                                            "width": round(cutLvl4['x2'] - last_cut_level6["x2"] - saw_width, 2),
                                            "nItem": index,
                                            "rotated": False,
                                            "type": 'retal'
                                        }
                                        cuts_level6.append(cut_level6_retal)
                                        parts.append(part_retal)
                                        index += 1
                                    
    return sorted_structure