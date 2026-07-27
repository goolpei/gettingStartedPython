def get_neighbourhood(n_type, mat, coordinates):  
    if not mat: return []
    row, col = coordinates
    total_rows = len(mat)
    total_cols = len(mat[0])
    if row >= total_rows or row < 0 or col >= total_cols or col < 0: return [] 

    offsets_vn = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    offsets_m = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    res = []
    if n_type == 'von_neumann': ofs = offsets_vn
    else: ofs = offsets_m

    for dr, dc in ofs:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < total_rows and 0 <= new_col < total_cols:
            res.append(mat[new_row][new_col])

    return res