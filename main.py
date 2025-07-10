from algorithms import process_sanitation_cuts, add_piece_by_cut, build_nested_structure, sort_level1_by_strip_height
from visualization import visualize_cutting_plan
import json
import os

result_optimization =  [
    {
        "layoutResume": {
            "version": "5.2.2",
            "usedStockCount": "3",
            "layoutCount": "1",
            "elapsedTime": "0.0408143",
            "material": "103057//TAB MELAM BLANCO BIO 15MM 2.15X2.50MTS//15.00//V",
            "sawWidth": "4.4",
            "lTrim": "10",
            "rTrim": "10",
            "tTrim": "10",
            "bTrim": "10",
            "maxBooks": "5",
            "thickness": "15",
            "ptxData": None,
            "dxfData": None
        },
        "layout": [
            {
                "stockCount": "1",
                "material": "103057//TAB MELAM BLANCO BIO 15MM 2.15X2.50MTS//15.00//V",
                "sheetH": "1830",
                "sheetW": "2440",
                "partCount": "3",
                "stockNo": "0",
                "rootStockNo": "0",
                "fillRatio": "0.6136343276896892",
                "stockCuts": "5",
                "part": [
                    {
                        "stockNo": "0",
                        "part": "0",
                        "x": "10",
                        "y": "10",
                        "length": "400",
                        "width": "1600",
                        "rotated": "False",
                        "datos": "4||||||||L|",
                        "nIdPza": 388551,
                        "bCortado": False,
                        "nItem": 4,
                        "nAncho": 400.0000000000,
                        "nLargo": 1600.0000000000,
                        "nAnchoTerm": 400.0000000000,
                        "nLargoTerm": 1600.0000000000,
                        "nCantidad": "1\/3",
                        "bServicioEsp": False,
                        "nPlano": 0,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "0",
                        "part": "1",
                        "x": "10",
                        "y": "414.4",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "2|D|D||||||L|",
                        "nIdPza": 388552,
                        "bCortado": False,
                        "nItem": 1,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 700.0000000000,
                        "nLargoTerm": 1500.0000000000,
                        "nCantidad": "1\/3",
                        "sCantoA1": "",
                        "bA1": "",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sPerforacion": "P-39-13-123-70-70-A1",
                        "sPerforacionTec": "P-1-A1",
                        "bServicioEsp": False,
                        "nPlano": 0,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "0",
                        "part": "2",
                        "x": "10",
                        "y": "1118.8",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "3|D|D|G|||||L|",
                        "nIdPza": 388553,
                        "bCortado": False,
                        "nItem": 1,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 700.0000000000,
                        "nLargoTerm": 1500.0000000000,
                        "nCantidad": "2\/3",
                        "sCantoA1": "",
                        "bA1": "",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sPerforacion": "P-39-13-123-70-70-A1",
                        "sPerforacionTec": "P-1-A1",
                        "bServicioEsp": False,
                        "nPlano": 0,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    }
                ],
                "wastePart": [
                    {
                        "stockNo": "0",
                        "part": "0",
                        "x": "1614.4",
                        "y": "10",
                        "length": "400",
                        "width": "815.6",
                        "rotated": False
                    },
                    {
                        "stockNo": "0",
                        "part": "1",
                        "x": "1514.4",
                        "y": "414.4",
                        "length": "1404.4",
                        "width": "915.6",
                        "rotated": False
                    }
                ],
                "cutsTrims": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "0",
                        "y1": "7.8",
                        "x2": "2440",
                        "y2": "7.8",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "0",
                        "y1": "1822.2",
                        "x2": "2440",
                        "y2": "1822.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "7.8",
                        "y1": "7.8",
                        "x2": "7.8",
                        "y2": "1822.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "2432.2",
                        "y1": "7.8",
                        "x2": "2432.2",
                        "y2": "1822.2",
                        "aLevel": "1"
                    }
                ],
                "cuts": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "7.8",
                        "y1": "412.2",
                        "x2": "2432.2",
                        "y2": "412.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "7.8",
                        "y1": "1821",
                        "x2": "2432.2",
                        "y2": "1821",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "1612.2",
                        "y1": "7.8",
                        "x2": "1612.2",
                        "y2": "412.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "1512.2",
                        "y1": "412.2",
                        "x2": "1512.2",
                        "y2": "1821",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "4",
                        "x1": "7.8",
                        "y1": "1116.6",
                        "x2": "1512.2",
                        "y2": "1116.6",
                        "aLevel": "2"
                    }
                ]
            },
            {
                "stockCount": "1",
                "material": "103057//TAB MELAM BLANCO BIO 15MM 2.15X2.50MTS//15.00//V",
                "sheetH": "1830",
                "sheetW": "2440",
                "partCount": "3",
                "stockNo": "1",
                "rootStockNo": "0",
                "fillRatio": "0.6136343276896892",
                "stockCuts": "5",
                "part": [
                    {
                        "stockNo": "1",
                        "part": "0",
                        "x": "10",
                        "y": "10",
                        "length": "400",
                        "width": "1600",
                        "rotated": "False",
                        "datos": "4||||||||L|",
                        "nIdPza": 388554,
                        "bCortado": False,
                        "nItem": 4,
                        "nAncho": 400.0000000000,
                        "nLargo": 1600.0000000000,
                        "nAnchoTerm": 400.0000000000,
                        "nLargoTerm": 1600.0000000000,
                        "nCantidad": "2\/3",
                        "bServicioEsp": False,
                        "nPlano": 1,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "1",
                        "part": "1",
                        "x": "10",
                        "y": "414.4",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "2|D|D||||||L|",
                        "nIdPza": 388555,
                        "bCortado": False,
                        "nItem": 1,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 700.0000000000,
                        "nLargoTerm": 1500.0000000000,
                        "nCantidad": "3\/3",
                        "sCantoA1": "",
                        "bA1": "",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sPerforacion": "P-39-13-123-70-70-A1",
                        "sPerforacionTec": "P-1-A1",
                        "bServicioEsp": False,
                        "nPlano": 1,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "1",
                        "part": "2",
                        "x": "10",
                        "y": "1118.8",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "3|D|D|G|||||L|",
                        "nIdPza": 388556,
                        "bCortado": False,
                        "nItem": 2,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 699.0000000000,
                        "nLargoTerm": 1500.0000000000,
                        "nCantidad": "1\/2",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sCantoL2": "D02",
                        "sDescL2": "Canto Blanco 1x22",
                        "bL2": "D02",
                        "bServicioEsp": False,
                        "nPlano": 1,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    }
                ],
                "wastePart": [
                    {
                        "stockNo": "0",
                        "part": "0",
                        "x": "1614.4",
                        "y": "10",
                        "length": "400",
                        "width": "815.6",
                        "rotated": False
                    },
                    {
                        "stockNo": "0",
                        "part": "1",
                        "x": "1514.4",
                        "y": "414.4",
                        "length": "1404.4",
                        "width": "915.6",
                        "rotated": False
                    }
                ],
                "cutsTrims": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "0",
                        "y1": "7.8",
                        "x2": "2440",
                        "y2": "7.8",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "0",
                        "y1": "1822.2",
                        "x2": "2440",
                        "y2": "1822.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "7.8",
                        "y1": "7.8",
                        "x2": "7.8",
                        "y2": "1822.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "2432.2",
                        "y1": "7.8",
                        "x2": "2432.2",
                        "y2": "1822.2",
                        "aLevel": "1"
                    }
                ],
                "cuts": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "7.8",
                        "y1": "412.2",
                        "x2": "2432.2",
                        "y2": "412.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "7.8",
                        "y1": "1821",
                        "x2": "2432.2",
                        "y2": "1821",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "1612.2",
                        "y1": "7.8",
                        "x2": "1612.2",
                        "y2": "412.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "1512.2",
                        "y1": "412.2",
                        "x2": "1512.2",
                        "y2": "1821",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "4",
                        "x1": "7.8",
                        "y1": "1116.6",
                        "x2": "1512.2",
                        "y2": "1116.6",
                        "aLevel": "2"
                    }
                ]
            },
            {
                "stockCount": "1",
                "material": "103057//TAB MELAM BLANCO BIO 15MM 2.15X2.50MTS//15.00//V",
                "sheetH": "1830",
                "sheetW": "2440",
                "partCount": "3",
                "stockNo": "2",
                "rootStockNo": "0",
                "fillRatio": "0.6136343276896892",
                "stockCuts": "5",
                "part": [
                    {
                        "stockNo": "2",
                        "part": "0",
                        "x": "10",
                        "y": "10",
                        "length": "400",
                        "width": "1600",
                        "rotated": "False",
                        "datos": "4||||||||L|",
                        "nIdPza": 388557,
                        "bCortado": False,
                        "nItem": 4,
                        "nAncho": 400.0000000000,
                        "nLargo": 1600.0000000000,
                        "nAnchoTerm": 400.0000000000,
                        "nLargoTerm": 1600.0000000000,
                        "nCantidad": "3\/3",
                        "bServicioEsp": False,
                        "nPlano": 2,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "2",
                        "part": "1",
                        "x": "10",
                        "y": "414.4",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "2|D|D||||||L|",
                        "nIdPza": 388558,
                        "bCortado": False,
                        "nItem": 2,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 699.0000000000,
                        "nLargoTerm": 1500.0000000000,
                        "nCantidad": "2\/2",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sCantoL2": "D02",
                        "sDescL2": "Canto Blanco 1x22",
                        "bL2": "D02",
                        "bServicioEsp": False,
                        "nPlano": 2,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    },
                    {
                        "stockNo": "2",
                        "part": "2",
                        "x": "10",
                        "y": "1118.8",
                        "length": "700",
                        "width": "1500",
                        "rotated": "False",
                        "datos": "3|D|D|G|||||L|",
                        "nIdPza": 388559,
                        "bCortado": False,
                        "nItem": 3,
                        "nAncho": 700.0000000000,
                        "nLargo": 1500.0000000000,
                        "nAnchoTerm": 699.0000000000,
                        "nLargoTerm": 1498.0000000000,
                        "nCantidad": "1\/1",
                        "sCantoA1": "G01",
                        "sDescA1": "Canto Blanco 2x22",
                        "bA1": "G01",
                        "sCantoL1": "D01",
                        "sDescL1": "Canto Blanco 0.4x22",
                        "bL1": "D01",
                        "sCantoL2": "D02",
                        "sDescL2": "Canto Blanco 1x22",
                        "bL2": "D02",
                        "bServicioEsp": False,
                        "nPlano": 2,
                        "sVeta": "L",
                        "bEngrosado": False,
                        "sEngrosado": "",
                        "sChaflan": ""
                    }
                ],
                "wastePart": [
                    {
                        "stockNo": "0",
                        "part": "0",
                        "x": "1614.4",
                        "y": "10",
                        "length": "400",
                        "width": "815.6",
                        "rotated": False
                    },
                    {
                        "stockNo": "0",
                        "part": "1",
                        "x": "1514.4",
                        "y": "414.4",
                        "length": "1404.4",
                        "width": "915.6",
                        "rotated": False
                    }
                ],
                "cutsTrims": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "0",
                        "y1": "7.8",
                        "x2": "2440",
                        "y2": "7.8",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "0",
                        "y1": "1822.2",
                        "x2": "2440",
                        "y2": "1822.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "7.8",
                        "y1": "7.8",
                        "x2": "7.8",
                        "y2": "1822.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "2432.2",
                        "y1": "7.8",
                        "x2": "2432.2",
                        "y2": "1822.2",
                        "aLevel": "1"
                    }
                ],
                "cuts": [
                    {
                        "stockNo": "0",
                        "iCut": "0",
                        "x1": "7.8",
                        "y1": "412.2",
                        "x2": "2432.2",
                        "y2": "412.2",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "1",
                        "x1": "7.8",
                        "y1": "1821",
                        "x2": "2432.2",
                        "y2": "1821",
                        "aLevel": "0"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "2",
                        "x1": "1612.2",
                        "y1": "7.8",
                        "x2": "1612.2",
                        "y2": "412.2",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "3",
                        "x1": "1512.2",
                        "y1": "412.2",
                        "x2": "1512.2",
                        "y2": "1821",
                        "aLevel": "1"
                    },
                    {
                        "stockNo": "0",
                        "iCut": "4",
                        "x1": "7.8",
                        "y1": "1116.6",
                        "x2": "1512.2",
                        "y2": "1116.6",
                        "aLevel": "2"
                    }
                ]
            }
        ],
        "error": None
    }
]

def generate_cuts_ordered(result_optimization):
    healthy_material = []    
    for material in result_optimization:
        trim = float(material['layoutResume']['lTrim'])
        saw_width = float(material['layoutResume']['sawWidth'])
        
        healthy_boards = []
        for board in material['layout']:
            width = float(board['sheetW'])
            height = float(board['sheetH'])
            cuts = board['cuts']
            parts = board['part']
    
            # Uso:
            # 1. Crear estructura cortes saneados
            level1, level2, level3, level4, level5, level6, parts = process_sanitation_cuts(cuts, parts, width, height, trim, saw_width)

            # 2. Agregar pieza por corte
            level1, level2, level3, level4, level5, level6 = add_piece_by_cut(level1, level2, level3, level4, level5, level6, parts, trim, saw_width)
        
            # 3. Crear estructura anidada
            nested_structure = build_nested_structure(level1, level2, level3, level4, level5, level6)

            # 4. Ordenar y recalcular coordenadas
            sorted_structure = sort_level1_by_strip_height(nested_structure, parts, trim, saw_width, 'asc')
            
            healthy_boards.append({
                **board,
                'cuts': sorted_structure,
                'parts': parts
            })
        
        healthy_material.append({
            ** material,
            'layout': healthy_boards,
        })
        
    return healthy_material

if __name__ == "__main__":

    healthy_material = generate_cuts_ordered(result_optimization)

    print('Ejecutando...')
    
    output_path = os.path.join(os.path.dirname(__file__), 'sorted_structure.json')
    with open(output_path, 'w') as json_file:
      json.dump(healthy_material, json_file, indent=4)
      
    print(f"Resultado guardado en {output_path}")
    
    # Visualizar el plano con medidas claras
    visualize_cutting_plan(healthy_material)
    

#PYCHARM