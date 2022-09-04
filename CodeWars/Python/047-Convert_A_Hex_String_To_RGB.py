def hex_string_to_RGB(hex_string): 
    r_hex = hex_string[1:3]
    g_hex = hex_string[3:5]
    b_hex = hex_string[5:7]    
    
    return {"r": int(r_hex, 16), "g": int(g_hex, 16), "b": int(b_hex, 16)}
