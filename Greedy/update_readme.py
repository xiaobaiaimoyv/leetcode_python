import os
import datetime

def generate_readme():
    # 获取当前日期，作为仓库的更新标签
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    header = f"# 🐍 小白摸鱼的 LeetCode 进化之路\n\n"
    header += f"> 📅 仓库最后更新：{today}\n\n"
    
    solutions_dir = './solutions'
    
    # 如果没有 solutions 目录则创建一个
    if not os.path.exists(solutions_dir):
        os.makedirs(solutions_dir)

    total_count = 0
    # 用来存储所有题目信息的列表，方便后面统一处理
    all_topics_content = ""

    # 1. 遍历题型分类文件夹 (例如 01_数组_Array)
    categories = sorted([d for d in os.listdir(solutions_dir) if os.path.isdir(os.path.join(solutions_dir, d))])
    
    for cat in categories:
        cat_path = os.path.join(solutions_dir, cat)
        
        # 2. 遍历题目文件夹 (例如 001_TwoSum)
        topics = sorted([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))])
        
        if not topics:
            continue
            
        total_count += len(topics)
        
        # 题型标题
        all_topics_content += f"### {cat}\n\n"
        # 按照你的要求重新排列的表头
        all_topics_content += "| 题号 | 类型 | 题目名称 | 题目 (笔记) | 解法代码 |\n| :--- | :--- | :--- | :--- | :--- |\n"
        
        for folder in topics:
            if '_' in folder:
                num, name = folder.split('_', 1)
                topic_path = os.path.join(cat_path, folder)
                
                # 获取该题目文件夹下的所有文件
                all_files = os.listdir(topic_path)
                
                # --- 检测 .py 文件 ---
                py_files = [f for f in all_files if f.endswith('.py')]
                if py_files:
                    # 链接到发现的第一个 py 文件
                    code_link = f"[查看代码 💻](solutions/{cat}/{folder}/{py_files[0]})"
                else:
                    code_link = "⏳ 待上传"

                # --- 检测 note.md (题目详情/笔记) ---
                # 兼容大小写：Note.md 或 note.md
                notes_file = next((f for f in all_files if f.lower() == "note.md"), None)
                if notes_file:
                    notes_link = f"[题目详情 📝](solutions/{cat}/{folder}/{notes_file})"
                else:
                    notes_link = "-"
                
                # 组装表格行
                # 类型这里直接显示 cat（也就是你的题型文件夹名）
                all_topics_content += f"| {num} | {cat} | {name} | {notes_link} | {code_link} |\n"
        
        all_topics_content += "\n"

    stats = f"目前已完成: **{total_count}** 题\n\n"
    
    # 写入文件
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header + stats + all_topics_content)
    
    print(f"✅ 更新完成！")
    print(f"统计：{len(categories)} 个类型，{total_count} 道题目。")

if __name__ == "__main__":
    generate_readme()