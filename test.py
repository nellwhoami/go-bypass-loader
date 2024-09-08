import binascii

# C语言字节数组（替换为实际的字节数据）
c_data = b"\x4d\x5a"

# 将字节数据转换为十六进制字符串
hex_data = binascii.hexlify(c_data).decode('ascii')

# 打印Go语言字节切片代码
go_code = "[]byte{\n"
for i in range(0, len(hex_data), 2):
    byte_val = hex_data[i:i+2]
    go_code += f"    0x{byte_val.upper()},\n"
go_code += "}"

print(go_code)
