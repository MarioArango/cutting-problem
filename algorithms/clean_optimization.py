def clean_optimization(board, trim, saw_width):
    
    orientation = 'h'
    cuts = board['cuts']
    parts = board['part']
    width_initial = board['sheetW']
    height_initial = board['sheetH']
    
    # Convert string values to appropriate types
    parts = [ {
        **part,
        "stockNo": float(part["stockNo"]),
        "part": float(part["part"]),
        "x": float(part["x"]),
        "y": float(part["y"]),
        "length": float(part["length"]),
        "width": float(part["width"]),
        "rotated": False if part["rotated"] == 'False' else True,
        'nItem': int(part.get('nItem', part['datos'].split('|')[0])),
        } for part in parts
    ]
    
    cuts = [ {
        "stockNo": cut["stockNo"],
        "iCut": int(cut["iCut"]),
        "x1": float(cut["x1"]),
        "y1": float(cut["y1"]),
        "x2": float(cut["x2"]),
        "y2": float(cut["y2"]),
        "aLevel": int(cut["aLevel"]) + 1
        } for cut in cuts
    ]
    
    #Verificar si el primer corte es horizontal o vertical
    cutsTrims = board['cutsTrims']    
    if float(board['sheetH']) == float(cutsTrims[0]['y2']):
        orientation = 'v';
         
    if orientation == 'h':        
        x1 = round(trim - saw_width/2, 2)
        x2 = round(float(board['sheetW']) - trim + saw_width/2, 2)
        y1 = round(trim - saw_width/2, 2)
        y2 = round(float(board['sheetH']) - trim + saw_width/2, 2)
    else:
        x1 = round(trim - saw_width/2, 2)
        x2 = round(float(board['sheetH']) - trim + saw_width/2, 2)
        y1 = round(trim - saw_width/2, 2)
        y2 = round(float(board['sheetW']) - trim + saw_width/2, 2)
        
        cuts = [{
            **cut,
            'x1': cut['y1'],
            'y1': cut['x1'],
            'x2': cut['y2'],
            'y2': cut['x2'],
        } for cut in cuts]
    
        parts = [{
            **part,
            'x': part['y'],
            'y': part['x'],
            'length': part['width'],
            'width': part['length'],
        } for part in parts]
        
        board['sheetH'] = width_initial
        board['sheetW'] = height_initial

    
    level1 = [ cut for cut in cuts if cut['aLevel'] == 1 ]
    level2 = [ cut for cut in cuts if cut['aLevel'] == 2 ]
    level3 = [ cut for cut in cuts if cut['aLevel'] == 3 ]
    level4 = [ cut for cut in cuts if cut['aLevel'] == 4 ]
    level5 = [ cut for cut in cuts if cut['aLevel'] == 5 ]
    level6 = [ cut for cut in cuts if cut['aLevel'] == 6 ]
    
    return level1, level2, level3, level4, level5, level6, parts, x1, x2, y1, y2