import pandas as pd

# 定义文件路径
excel_file = 'item_with_openrank.xlsx'  # 请替换为你的Excel文件名

# 尝试读取 Excel 文件中的 Sheet3
try:
    df = pd.read_excel(excel_file, sheet_name='Sheet3')
except FileNotFoundError:
    print(f"错误：未找到文件 {excel_file}。请确保文件和脚本在同一目录下。")
    exit()
except ValueError:
    print("错误：未找到名为 'Sheet3' 的工作表。请检查工作表名称是否正确。")
    exit()

# 获取 C 列的数据
# 假设 Excel 有表头，并且 C 列的列名是 'license'
if 'license' in df.columns:
    license_series = df['license']
else:
    # 如果没有表头，或者列名不同，我们使用列索引 C (第3列，索引为2)
    print("警告：未找到 'license' 列，将使用第3列 (索引2)。")
    license_series = df.iloc[:, 2]

# 统计每个 license 的数量
license_counts = license_series.value_counts()

# 计算每个 license 的占比
total_licenses = len(license_series)
license_percentages = (license_counts / total_licenses) * 100

# 将结果合并到一个 DataFrame
summary_df = pd.DataFrame({
    '数量': license_counts,
    '占比 (%)': license_percentages
})

# 打印结果
print("License 统计结果：")
print(summary_df)

# 将结果保存到新的 Excel 文件
output_file = 'license_summary.xlsx'
summary_df.to_excel(output_file)
print(f"\n结果已保存到 {output_file} 文件中。")