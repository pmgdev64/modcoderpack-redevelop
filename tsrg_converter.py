def convert_tsrg_to_srg(tsrg_path, srg_path):
    with open(tsrg_path, 'r') as f:
        lines = f.readlines()
    
    output = []
    current_class = ""
    
    for line in lines:
        if not line.startswith('\t'):
            parts = line.strip().split()
            if len(parts) >= 2:
                current_class = parts[0]
                output.append(f"CL: {parts[0]} {parts[1]}")
        else:
            parts = line.strip().split()
            if len(parts) == 2: # Field
                output.append(f"FD: {current_class}/{parts[0]} {current_class}/{parts[1]}")
            elif len(parts) == 3: # Method
                output.append(f"MD: {current_class}/{parts[0]} {parts[1]} {current_class}/{parts[2]} {parts[1]}")
                
    with open(srg_path, 'w') as f:
        f.write('\n'.join(output))

# Chạy chuyển đổi
convert_tsrg_to_srg('conf/joined.tsrg', 'conf/joined.srg')
print("Đã chuyển đổi thành công sang joined.srg!")
