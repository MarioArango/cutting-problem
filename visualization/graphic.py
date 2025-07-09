import matplotlib.pyplot as plt
import matplotlib.patches as patches

class CuttingPlanVisualizer:
    def __init__(self, board_width, board_height):
        self.figsize = (15, 9)
        self.piece_colors = [
              '#d1ffd6',
    '#ffc759',
    '#e8ffc7',
    '#ffdb52',
    '#ebffb5',
    '#ffd67a',
    '#ffc7a8',
    '#ffedbd',
    '#cfffe6',
    '#ffba91',
    '#e0ff96',
    '#ffdec2',
    '#fff08c',
    '#d7ffd7',
    '#edffe6',
    '#fde2cd',
    '#d1eaf9',
    '#d0f3ee',
    '#dcd9f8',
    '#f7d8c3',
    '#d7ffff',
    '#ffc8c3',
    '#a9e5e3',
    '#fae087',
    '#d8f79a',
    '#e8ba86',
    '#a2edce',
    '#afd7ff',
    '#afffaf',
    '#d0f3ee',
    '#f4d1f4',
    '#fafda4',
    '#ded6f8',
    '#fdd1fd',
    '#fcf0e4',
    '#d9edf6',
    '#d787af',
    '#d787d7',
    '#d7af5f',
    '#d7af87',
    '#d7afaf',
    '#d7d787',
    '#d7d7ff',
    '#d7ffff',
    '#ffe870',
    '#ffd7af',
    '#ffd7ff',
    '#ffff87',
    '#ffffd7'
        ]
        self.cut_line_color = '#000000'
        self.piece_counter = 0
        self.pieces_drawn = set()
        self.board_width = board_width
        self.board_height = board_height

    def get_piece_color(self):
        color = self.piece_colors[self.piece_counter % len(self.piece_colors)]
        self.piece_counter += 1
        return color

    def draw_piece(self, ax, x1, y1, x2, y2, scale, x_offset, y_offset):
        piece_key = (x1, y1, x2, y2)
        if piece_key in self.pieces_drawn:
            return
        self.pieces_drawn.add(piece_key)

        # Chequeo si está fuera del tablero
        fuera = (
            x1 < 0 or x2 > self.board_width or
            y1 < 0 or y2 > self.board_height
        )
        if fuera:
            print(f"⚠️ Pieza fuera del tablero: ({x1:.1f},{y1:.1f}) a ({x2:.1f},{y2:.1f})")
            color = "#f55"  # Rojo
            edge_color = "#b00"
        else:
            color = self.get_piece_color()
            edge_color = self.cut_line_color

        # Escalado y offset
        x1s, y1s = x1 * scale + x_offset, y1 * scale + y_offset
        x2s, y2s = x2 * scale + x_offset, y2 * scale + y_offset
        width = abs(x2s - x1s)
        height = abs(y2s - y1s)

        rect = patches.Rectangle(
            (min(x1s, x2s), min(y1s, y2s)),
            width, height,
            facecolor=color, edgecolor=edge_color, linewidth=2, alpha=0.88
        )
        ax.add_patch(rect)

        # Solo mostrar dimensiones si la pieza es suficientemente grande
        min_text_dim = 60
        if width > min_text_dim and height > min_text_dim:
            cx, cy = (x1s + x2s) / 2, (y1s + y2s) / 2
            real_w, real_h = abs(x2 - x1), abs(y2 - y1)
            font_size = 14
            ax.text(
                cx, cy, f"{int(real_w)}x{int(real_h)}",
                ha="center", va="center", fontsize=font_size,
                fontweight="bold", color="#222"
            )

    def draw_cuts(self, ax, cuts, x_min, x_max, y_min, y_max, scale, x_offset, y_offset):
        if not cuts:
            self.draw_piece(ax, x_min, y_min, x_max, y_max, scale, x_offset, y_offset)
            return

        cuts_by_level = {}
        for cut in cuts:
            level = cut['aLevel']
            cuts_by_level.setdefault(level, []).append(cut)

        min_level = min(cuts_by_level.keys())
        level_cuts = sorted(
            cuts_by_level[min_level],
            key=lambda c: c['y1'] if min_level % 2 == 1 else c['x1']
        )

        if min_level % 2 == 1:
            current_y = y_min
            for cut in level_cuts:
                cut_y = cut['y1']
                x1_plot = x_min * scale + x_offset
                x2_plot = x_max * scale + x_offset
                y_plot = cut_y * scale + y_offset
                ax.plot([x1_plot, x2_plot], [y_plot, y_plot], color='#444', lw=2.2)
                subcuts = []
                for i in range(2, 7):
                    key = f'level{i}'
                    if key in cut and cut[key]:
                        subcuts += cut[key]
                if subcuts:
                    self.draw_cuts(ax, subcuts, x_min, x_max, current_y, cut_y, scale, x_offset, y_offset)
                else:
                    self.draw_piece(ax, x_min, current_y, x_max, cut_y, scale, x_offset, y_offset)
                current_y = cut_y
            if current_y < y_max:
                last_cut = level_cuts[-1]
                subcuts = []
                for i in range(2, 7):
                    key = f'level{i}'
                    if key in last_cut and last_cut[key]:
                        subcuts += last_cut[key]
                if subcuts:
                    self.draw_cuts(ax, subcuts, x_min, x_max, current_y, y_max, scale, x_offset, y_offset)
                else:
                    self.draw_piece(ax, x_min, current_y, x_max, y_max, scale, x_offset, y_offset)
        else:
            current_x = x_min
            for cut in level_cuts:
                cut_x = cut['x1']
                y1_plot = y_min * scale + y_offset
                y2_plot = y_max * scale + y_offset
                x_plot = cut_x * scale + x_offset
                ax.plot([x_plot, x_plot], [y1_plot, y2_plot], color='#444', lw=2.2)
                subcuts = []
                for i in range(2, 7):
                    key = f'level{i}'
                    if key in cut and cut[key]:
                        subcuts += cut[key]
                if subcuts:
                    self.draw_cuts(ax, subcuts, current_x, cut_x, y_min, y_max, scale, x_offset, y_offset)
                else:
                    self.draw_piece(ax, current_x, y_min, cut_x, y_max, scale, x_offset, y_offset)
                current_x = cut_x
            if current_x < x_max:
                last_cut = level_cuts[-1]
                subcuts = []
                for i in range(2, 7):
                    key = f'level{i}'
                    if key in last_cut and last_cut[key]:
                        subcuts += last_cut[key]
                if subcuts:
                    self.draw_cuts(ax, subcuts, current_x, x_max, y_min, y_max, scale, x_offset, y_offset)
                else:
                    self.draw_piece(ax, current_x, y_min, x_max, y_max, scale, x_offset, y_offset)

    def visualize(self, cuts_data):
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.set_facecolor('white')
        margin_x, margin_y = 90, 80
        scale = min(
            (self.figsize[0]*100 - 2*margin_x)/self.board_width,
            (self.figsize[1]*100 - 2*margin_y)/self.board_height
        )
        scale = min(scale, 0.32)
        x_offset = margin_x + ((self.figsize[0]*100 - 2*margin_x) - self.board_width*scale) / 2
        y_offset = margin_y + ((self.figsize[1]*100 - 2*margin_y) - self.board_height*scale) / 2

        # Tablero principal
        ax.add_patch(patches.Rectangle(
            (x_offset, y_offset),
            self.board_width*scale, self.board_height*scale,
            linewidth=2.5, edgecolor='#000', facecolor='#F4F4F4', alpha=0.98, zorder=1
        ))

        self.piece_counter = 0
        self.pieces_drawn = set()
        self.draw_cuts(ax, cuts_data, 0, self.board_width, 0, self.board_height, scale, x_offset, y_offset)

        # Título
        ax.text(
            x_offset + (self.board_width*scale)/2, y_offset - 30,
            "PLANO DE CORTE - OPTIMIZACIÓN",
            ha="center", va="bottom", fontsize=20, fontweight="bold"
        )
        # Medidas
        ax.text(
            x_offset, y_offset + self.board_height*scale + 30,
            f"TABLERO: {int(self.board_width)} x {int(self.board_height)} mm", fontsize=12, fontweight="bold"
        )
        ax.text(
            x_offset, y_offset + self.board_height*scale + 48,
            f"PIEZAS: {self.piece_counter}", fontsize=11
        )
        ax.text(
            x_offset + self.board_width*scale - 160, y_offset + self.board_height*scale + 30,
            "MATERIAL: MELAMINA", fontsize=11
        )

        ax.set_xlim(0, self.figsize[0]*100)
        ax.set_ylim(0, self.figsize[1]*100)
        ax.invert_yaxis()
        ax.set_aspect('equal')
        ax.axis('off')
        plt.tight_layout()
        plt.show()

def visualize_cutting_plan(width, height, cuts_data):
    visualizer = CuttingPlanVisualizer(width, height)
    visualizer.visualize(cuts_data)