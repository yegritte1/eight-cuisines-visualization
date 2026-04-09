#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量为所有子页面添加返回按钮
"""

import os
import re

# 返回按钮的CSS样式
BACK_BUTTON_CSS = """
        /* 返回按钮 */
        .back-button {
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(8px);
            border: 2px solid rgba(200, 48, 46, 0.2);
            border-radius: 12px;
            padding: 10px 20px;
            color: #c8302e;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .back-button:hover {
            transform: translateX(-4px);
            border-color: #c8302e;
            background: rgba(255, 255, 255, 1);
            box-shadow: 0 4px 12px rgba(200, 48, 46, 0.2);
        }

        .back-button svg {
            width: 18px;
            height: 18px;
            stroke: currentColor;
            stroke-width: 2.5;
            fill: none;
        }
"""

# 返回按钮的HTML
BACK_BUTTON_HTML = """    <!-- 返回按钮 -->
    <a href="../menu.html" class="back-button">
        <svg viewBox="0 0 24 24">
            <polyline points="15 18 9 12 15 6"></polyline>
        </svg>
        返回目录
    </a>

"""

def add_back_button(file_path):
    """给单个HTML文件添加返回按钮"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 检查是否已经有返回按钮
        if 'class="back-button"' in content or '返回目录' in content:
            print(f"✓ {os.path.basename(file_path)} - 已有返回按钮，跳过")
            return

        # 在</style>标签前添加CSS
        if '</style>' in content:
            content = content.replace('</style>', BACK_BUTTON_CSS + '    </style>')
        else:
            print(f"✗ {os.path.basename(file_path)} - 未找到</style>标签")
            return

        # 在<body>标签后添加HTML按钮
        if '<body>' in content:
            content = content.replace('<body>', '<body>\n' + BACK_BUTTON_HTML)
        elif '<body' in content:
            # 处理带属性的body标签
            content = re.sub(r'(<body[^>]*>)', r'\1\n' + BACK_BUTTON_HTML, content)
        else:
            print(f"✗ {os.path.basename(file_path)} - 未找到<body>标签")
            return

        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"✓ {os.path.basename(file_path)} - 成功添加返回按钮")

    except Exception as e:
        print(f"✗ {os.path.basename(file_path)} - 错误: {e}")

def main():
    """主函数"""
    pages_dir = "pages"

    if not os.path.exists(pages_dir):
        print(f"错误：找不到 {pages_dir} 目录")
        return

    html_files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

    print(f"\n开始处理 {len(html_files)} 个HTML文件...\n")
    print("=" * 60)

    for html_file in html_files:
        file_path = os.path.join(pages_dir, html_file)
        add_back_button(file_path)

    print("=" * 60)
    print(f"\n处理完成！共处理 {len(html_files)} 个文件\n")

if __name__ == "__main__":
    main()
