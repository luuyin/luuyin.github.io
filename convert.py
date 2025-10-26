import os
import re
from pathlib import Path

def convert_brackets_to_span(content):
    """
    将 [标签内容] 格式转换为 <span class="badge-flag" data-conf="publication">标签内容</span> 格式
    只转换行首的方括号标签
    """
    # 正则表达式匹配行首的 [xxx] 格式
    # 使用 re.MULTILINE 使 ^ 匹配每行的开头
    pattern = r'^(\[([^\]]+)\])'
    
    def replace_bracket(match):
        full_match = match.group(1)  # 完整的 [xxx]
        tag_content = match.group(2)  # 方括号内的内容
        
        # 根据标签内容确定 data-conf 属性
        # 你可以根据需要调整这个逻辑
        conf_value = determine_conf_value(tag_content)
        
        return f'<span class="badge-flag" data-conf="{conf_value}">{tag_content}</span>'
    
    # 执行替换
    converted_content = re.sub(pattern, replace_bracket, content, flags=re.MULTILINE)
    return converted_content

def determine_conf_value(tag_content):
    """
    根据标签内容决定 data-conf 的值
    可以根据你的需求自定义规则
    """
    tag_lower = tag_content.lower()

    return 'publication'
    
    # # 根据会议/期刊名称设置不同的 conf 值
    # if 'neurips' in tag_lower:
    #     return 'neurips'
    # elif 'publication' in tag_lower:
    #     return 'publication'
    # elif 'icml' in tag_lower:
    #     return 'icml'
    # elif 'cvpr' in tag_lower:
    #     return 'cvpr'
    # elif 'eccv' in tag_lower:
    #     return 'eccv'
    # elif 'iccv' in tag_lower:
    #     return 'iccv'
    # elif 'aaai' in tag_lower:
    #     return 'aaai'
    # elif 'acl' in tag_lower:
    #     return 'acl'
    # elif 'emnlp' in tag_lower:
    #     return 'emnlp'
    # elif 'challenge' in tag_lower:
    #     return 'challenge'
    # else:
    #     # 默认值
    #     return 'conf'

def process_md_files(news_folder_path, backup=True):
    """
    处理指定文件夹下的所有.md文件
    
    参数:
    news_folder_path: _news 文件夹的路径
    backup: 是否在修改前备份原文件
    """
    news_path = Path(news_folder_path)
    
    if not news_path.exists():
        print(f"错误: 文件夹 {news_folder_path} 不存在")
        return
    
    # 获取所有 .md 文件
    md_files = list(news_path.glob("*.md"))
    
    if not md_files:
        print(f"在 {news_folder_path} 中没有找到 .md 文件")
        return
    
    print(f"找到 {len(md_files)} 个 .md 文件")
    
    converted_count = 0
    
    for md_file in md_files:
        print(f"\n处理文件: {md_file.name}")
        
        try:
            # 读取文件内容
            with open(md_file, 'r', encoding='utf-8') as f:
                original_content = f.read()
            
            # 转换内容
            converted_content = convert_brackets_to_span(original_content)
            
            # 检查是否有变化
            if original_content != converted_content:
                # 如果需要备份
                if backup:
                    backup_file = md_file.with_suffix('.md.bak')
                    with open(backup_file, 'w', encoding='utf-8') as f:
                        f.write(original_content)
                    print(f"  - 已创建备份: {backup_file.name}")
                
                # 写入转换后的内容
                with open(md_file, 'w', encoding='utf-8') as f:
                    f.write(converted_content)
                
                print(f"  - 转换成功")
                converted_count += 1
            else:
                print(f"  - 无需转换（没有找到匹配的方括号标签）")
                
        except Exception as e:
            print(f"  - 处理失败: {e}")
    
    print(f"\n处理完成！共转换了 {converted_count} 个文件")

def preview_conversion(news_folder_path, num_lines=10):
    """
    预览转换效果，不实际修改文件
    """
    news_path = Path(news_folder_path)
    
    if not news_path.exists():
        print(f"错误: 文件夹 {news_folder_path} 不存在")
        return
    
    md_files = list(news_path.glob("*.md"))[:1]  # 只预览第一个文件
    
    if not md_files:
        print(f"在 {news_folder_path} 中没有找到 .md 文件")
        return
    
    md_file = md_files[0]
    print(f"预览文件: {md_file.name}")
    print("=" * 50)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 跳过 YAML front matter
    if content.startswith('---'):
        # 找到第二个 ---
        parts = content.split('---', 2)
        if len(parts) >= 3:
            # parts[0] 是空的，parts[1] 是 YAML，parts[2] 是实际内容
            actual_content = parts[2].strip()
        else:
            actual_content = content
    else:
        actual_content = content
    
    # 只显示实际内容的前几行
    actual_lines = actual_content.split('\n')[:num_lines]
    original_text = '\n'.join(actual_lines)
    
    if not original_text.strip():
        print("注意: 文件中似乎没有实际内容，只有YAML头部")
        print("\n完整文件内容预览:")
        print(content[:500])  # 显示前500个字符
    else:
        converted_text = convert_brackets_to_span(original_text)
        
        print("原始内容（跳过YAML头部）:")
        print(original_text)
        print("\n转换后:")
        print(converted_text)
    
    print("=" * 50)

# 使用示例
if __name__ == "__main__":
    # 设置 _news 文件夹的路径
    NEWS_FOLDER = "_news"  # 根据实际情况修改路径
    
    # 先预览转换效果
    print("=== 预览转换效果 ===\n")
    preview_conversion(NEWS_FOLDER)
    
    # 询问是否继续
    user_input = input("\n是否继续转换所有文件？(y/n): ")
    
    if user_input.lower() == 'y':
        # 执行转换，默认创建备份
        process_md_files(NEWS_FOLDER, backup=True)
        print("\n提示: 原文件已备份为 .md.bak 文件")
        print("如果需要恢复，可以将 .bak 文件重命名回 .md")
    else:
        print("已取消操作")