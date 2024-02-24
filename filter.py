import yaml

# 要过滤的字符串列表
filter_strings = ["type: hysteria2", "type: trojan"]

def filter_yaml_file(input_file, output_file):
    # 读取YAML文件
    with open(input_file, 'r',  encoding='utf-8') as file:
        data = yaml.safe_load(file)
        #lines = file.readline()

    # 使用列表推导式过滤出满足条件的项目
    filtered_data = [item for item in data['proxies'] if item.get('type') == 'hysteria2' or item.get('type') == 'trojan']
    vmess = [item for item in data['proxies'] if item.get('type') == 'vmess']

    # 打印过滤后的结果
    print(len(filtered_data), " 个代理")
    print(len(vmess), " 个vmess")

    # 将结果写回YAML文件
    with open(output_file, 'w') as file:
        # 写入 "proxies:" 头部
        file.write("proxies:\n")
        yaml.dump(filtered_data, file)

    with open(output_vmess, 'w') as file:
        # 写入 "proxies:" 头部
        file.write("proxies:\n")
        yaml.dump(vmess, file)
        
# Main
input_file = 'clash.yaml'
output_file = 'htonly.yml'
output_vmess = 'vmess.yml'
filter_yaml_file(input_file, output_file)
