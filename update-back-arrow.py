#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
更新所有子页面的返回按钮为小箭头样式
"""

import os
import re

# 新的返回按钮CSS样式
NEW_BACK_BUTTON_CSS = """
        /* 返回按钮 - 小箭头样式 */
        .back-button {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            width: 36px;
            height: 36px;
            background: rgba(200, 48, 46, 0.15);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
        }

        .back-button:hover {
            background: rgba(200, 48, 46, 0.25);
            transform: scale(1.1);
        }

        .back-button svg {
            width: 18px;
            height: 18px;
            stroke: #c8302e;
            stroke-width: 2.5;
            fill: none;
        }
"""

# 新的返回按钮HTML
NEW_BACK_BUTTON_HTML = """    <!-- 返回按钮 -->
    <a href="../catalog.html" class="back-button" title="返回目录">
        <svg viewBox="0 0 24 24">
            <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
    </a>

"""

def update_back_button_style(file_path):
    """更新单个HTML文件的返回按钮样式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否有返回按钮
        if 'class="back-button"' not in content:
            print(f"✗ {os.path.basename(file_path)} - 未找到返回按钮")
            return

        # 替换返回按钮的CSS样式
        # 匹配整个 .back-button 样式块
        pattern = r'/\* 返回按钮.*?\*/.+?\.back-button\s*\{[^}]+\}.*?\.back-button:hover\s*\{[^}]+\}.*?\.back-button svg\s*\{[^}]+\}'

        if re.search(pattern, content, re.DOTALL):
            content = re.sub(pattern, NEW_BACK_BUTTON_CSS.strip(), content, flags=re.DOTALL)
        else:
            print(f"⚠ {os.path.basename(file_path)} - 未找到CSS样式块，跳过CSS更新")

        # 替换返回按钮的HTML
        # 匹配 <!-- 返回按钮 --> 到下一个空行
        html_pattern = r'<!-- 返回按钮 -->.*?</a>\s*'

        if re.search(html_pattern, content, re.DOTALL):
            content = re.sub(html_pattern, NEW_BACK_BUTTON_HTML, content, flags=re.DOTALL)
        else:
            print(f"⚠ {os.path.basename(file_path)} - 未找到HTML按钮，跳过HTML更新")

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ {os.path.basename(file_path)} - 成功更新为小箭头样式")

    except Exception as e:
        print(f"✗ {os.path.basename(file_path)} - 错误: {e}")

def main():
    """主函数"""
    pages_dir = "pages"

    if not os.path.exists(pages_dir):
        print(f"错误：找不到 {pages_dir} 目录")
        return

    html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

    print(f"\n开始更新 {len(html_files)} 个HTML文件的返回按钮样式...\n")
    print("=" * 60)

    for html_file in html_files:
        file_path = os.path.join(pages_dir, html_file)
        update_back_button_style(file_path)

    print("=" * 60)
    print(f"\n更新完成！共处理 {len(html_files)} 个文件\n")

if __name__ == "__main__":
    main()
