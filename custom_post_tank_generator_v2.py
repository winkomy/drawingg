import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ==========================================
# PROFESSIONAL HDG TANK HANDRAIL GENERATOR
# ==========================================
# Editable Parameters
TANK_LENGTH = 20000        
TANK_HEIGHT = 4000         
PANEL_SIZE = 1000          
HANDRAIL_HEIGHT = 1050     

# ------------------------------------------
# FRONT ELEVATION PARAMETERS
# ------------------------------------------
LADDER_WIDTH = 390
LADDER_CENTERS = [8500, 11500] 

FRONT_POST_LOCATIONS = [
    0, 2000, 4000, 6000, 8000,       
    8305, 8695,                      
    10000,                           
    11305, 11695,                    
    12000, 14000, 16000, 18000, 20000 
]

FRONT_PIPE_SEGMENTS = [
    (0, 3000), (3000, 6000), (6000, 8255), 
    (8745, 11255), 
    (11745, 14000), (14000, 17000), (17000, 20000)
]

# ------------------------------------------
# BACK ELEVATION PARAMETERS
# ------------------------------------------
# The back elevation has no ladders.
# Vertical angles are spaced every 2000mm.
BACK_POST_LOCATIONS = [
    0, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000, 20000
]

# Based on your BOM: 20m span = Six 3m pipes + One 2m pipe
BACK_PIPE_SEGMENTS = [
    (0, 3000), 
    (3000, 6000), 
    (6000, 9000), 
    (9000, 12000), 
    (12000, 15000), 
    (15000, 18000), 
    (18000, 20000) # The final 2m pipe
]


# ==========================================
# DRAWING FUNCTIONS
# ==========================================
def draw_front_elevation(output_file="custom_post_front_elevation.png"):
    fig, ax = plt.subplots(figsize=(22, 7))
    
    for x in range(0, TANK_LENGTH, PANEL_SIZE):
        for y in range(0, TANK_HEIGHT, PANEL_SIZE):
            ax.add_patch(patches.Rectangle((x, y), PANEL_SIZE, PANEL_SIZE, linewidth=0.5, edgecolor='#A9A9A9', facecolor='#F5F5F5'))

    post_y_start = TANK_HEIGHT
    post_y_end = TANK_HEIGHT + HANDRAIL_HEIGHT
    for x in FRONT_POST_LOCATIONS:
        ax.plot([x, x], [post_y_start, post_y_end], color='#2F4F4F', linewidth=3.0)

    mid_rail_height = TANK_HEIGHT + (HANDRAIL_HEIGHT / 2)
    for start_x, end_x in FRONT_PIPE_SEGMENTS:
        ax.plot([start_x, end_x], [post_y_end, post_y_end], color='#2F4F4F', linewidth=3.5)
        ax.plot([start_x, end_x], [mid_rail_height, mid_rail_height], color='#2F4F4F', linewidth=2.5)
        pipe_len = end_x - start_x
        label = f"{int(pipe_len/1000)}m" if pipe_len % 1000 == 0 else f"{pipe_len/1000:.3f}m"
        ax.text(start_x + (pipe_len / 2), post_y_end + 100, label, ha='center', va='bottom', fontsize=10, fontweight='bold', color='#191970')
        
    for center in LADDER_CENTERS:
        lad_start = center - LADDER_WIDTH/2
        lad_end = center + LADDER_WIDTH/2
        ax.plot([lad_start, lad_start], [-600, post_y_end], color='#4682B4', linewidth=2)
        ax.plot([lad_end, lad_end], [-600, post_y_end], color='#4682B4', linewidth=2)
        for rung_y in range(-600, int(post_y_end), 300):
            ax.plot([lad_start, lad_end], [rung_y, rung_y], color='#4682B4', linewidth=1.5)

    ax.set_aspect('equal')
    ax.set_xlim(-1000, TANK_LENGTH + 1000)
    ax.set_ylim(-1000, TANK_HEIGHT + HANDRAIL_HEIGHT + 1000)
    ax.set_title("FRONT Elevation - Custom Vertical Angle Spacing", fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved Front: {output_file}")


def draw_back_elevation(output_file="custom_post_back_elevation.png"):
    fig, ax = plt.subplots(figsize=(22, 7))
    
    for x in range(0, TANK_LENGTH, PANEL_SIZE):
        for y in range(0, TANK_HEIGHT, PANEL_SIZE):
            ax.add_patch(patches.Rectangle((x, y), PANEL_SIZE, PANEL_SIZE, linewidth=0.5, edgecolor='#A9A9A9', facecolor='#F5F5F5'))

    post_y_start = TANK_HEIGHT
    post_y_end = TANK_HEIGHT + HANDRAIL_HEIGHT
    for x in BACK_POST_LOCATIONS:
        ax.plot([x, x], [post_y_start, post_y_end], color='#2F4F4F', linewidth=3.0)

    mid_rail_height = TANK_HEIGHT + (HANDRAIL_HEIGHT / 2)
    for start_x, end_x in BACK_PIPE_SEGMENTS:
        ax.plot([start_x, end_x], [post_y_end, post_y_end], color='#2F4F4F', linewidth=3.5)
        ax.plot([start_x, end_x], [mid_rail_height, mid_rail_height], color='#2F4F4F', linewidth=2.5)
        pipe_len = end_x - start_x
        label = f"{int(pipe_len/1000)}m" if pipe_len % 1000 == 0 else f"{pipe_len/1000:.3f}m"
        ax.text(start_x + (pipe_len / 2), post_y_end + 100, label, ha='center', va='bottom', fontsize=10, fontweight='bold', color='#191970')

    ax.set_aspect('equal')
    ax.set_xlim(-1000, TANK_LENGTH + 1000)
    ax.set_ylim(-1000, TANK_HEIGHT + HANDRAIL_HEIGHT + 1000)
    ax.set_title("BACK Elevation - Custom Vertical Angle Spacing", fontsize=16, fontweight='bold')
    ax.axis('off')
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved Back: {output_file}")


if __name__ == '__main__':
    draw_front_elevation()
    draw_back_elevation()
