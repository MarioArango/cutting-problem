def clean_optimization(board, trim, saw_width):
    
    width = float(board['sheetW'])
    height = float(board['sheetH'])
    cuts = board['cuts']
    parts = board['part']
            
    x1 = round(trim - saw_width/2, 2)
    x2 = round(width - trim + saw_width/2, 2)
    y1 = round(trim - saw_width/2, 2)
    y2 = round(height - trim + saw_width/2, 2)
    
    parts = [ {
        **part,
        "stockNo": float(part["stockNo"]),
        "part": float(part["part"]),
        "x": float(part["x"]),
        "y": float(part["y"]),
        "length": float(part["length"]),
        "width": float(part["width"]),
        "rotated": False if part["rotated"] == 'False' else True
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
    
    level1 = [ cut for cut in cuts if cut['aLevel'] == 1 ]
    level2 = [ cut for cut in cuts if cut['aLevel'] == 2 ]
    level3 = [ cut for cut in cuts if cut['aLevel'] == 3 ]
    level4 = [ cut for cut in cuts if cut['aLevel'] == 4 ]
    level5 = [ cut for cut in cuts if cut['aLevel'] == 5 ]
    level6 = [ cut for cut in cuts if cut['aLevel'] == 6 ]
    
    return level1, level2, level3, level4, level5, level6, parts, x1, x2, y1, y2