#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新所有子页面的返回按钮，指向目录页 catalog.html
"""

import os
import re

def update_back_button(file_path):
    """更新单个HTML文件的返回按钮链接"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否有返回按钮
        if 'class="back-button"' not in content and '返回目录' not in content:
            print(f"✗ {os.path.basename(file_path)} - 未找到返回按钮")
            return

        # 替换返回按钮的 href
        # 匹配 <a href="../menu.html" class="back-button">
        content = re.sub(
            r'<a href="\.\./(menu|catalog)\.html" class="back-button">',
            r'<a href="../catalog.html" class="back-button">',
            content
        )

        # 替换按钮文字为"返回目录"
        content = re.sub(
            r'(class="back-button"[^>]*>[\s\S]*?<span[^>]*>|class="back-button"[^>]*>[\s\S]*?>)返回封面',
            r'\1返回目录',
            content
        )

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ {os.path.basename(file_path)} - 成功更新返回按钮")

    except Exception as e:
        print(f"✗ {os.path.basename(file_path)} - 错误: {e}")

def main():
    """主函数"""
    pages_dir = "pages"

    if not os.path.exists(pages_dir):
        print(f"错误：找不到 {pages_dir} 目录")
        return

    html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

    print(f"\n开始更新 {len(html_files)} 个HTML文件的返回按钮...\n")
    print("=" * 60)

    for html_file in html_files:
        file_path = os.path.join(pages_dir, html_file)
        update_back_button(file_path)

    print("=" * 60)
    print(f"\n更新完成！共处理 {len(html_files)} 个文件\n")

if __name__ == "__main__":
    main()
