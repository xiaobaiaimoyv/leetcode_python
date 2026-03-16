import os
import datetime

def generate_readme():
    # 获取今天的日期（作为你提到的“标签”）
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    header = f"# 🐍 小白摸鱼的 LeetCode 进化之路\n\n"
    header += f"> 📅 最后更新时间：{today}\n\n"
    
    solutions_dir = './solutions'
    
    if not os.path.exists(solutions_dir):
        os.makedirs(solutions_dir)

    total_count = 0
    content = ""

    # 1. 遍历第一层：题型分类文件夹
    categories = sorted([d for d in os.listdir(solutions_dir) if os.path.isdir(os.path.join(solutions_dir, d))])
    
    for cat in categories:
        cat_path = os.path.join(solutions_dir, cat)
        
        # 2. 遍历第二层：题目文件夹
        topics = sorted([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))])
        
        if not topics:
            continue
            
        total_count += len(topics)
        content += f"### {cat}\n\n"
        content += "| 题号 | 题目名称 | 解法代码 | 笔记 |\n| :--- | :--- | :--- | :--- |\n"
        
        for folder in topics:
            if '_' in folder:
                num, name = folder.split('_', 1)
                topic_path = os.path.join(cat_path, folder)
                
                # --- 核心修改部分：检测目录下任何 .py 文件 ---
                all_files = os.listdir(topic_path)
                py_files = [f for f in all_files if f.endswith('.py')]
                
                if py_files:
                    # 取找到的第一个 py 文件作为链接
                    target_py = py_files[0]
                    code_link = f"[Python 🐍](solutions/{cat}/{folder}/{target_py})"
                else:
                    code_link = "未上传"
                # ------------------------------------------

                # 笔记检测保持不变
                notes_exist = "notes.md" in all_files
                notes_link = f"[笔记 📝](solutions/{cat}/{folder}/notes.md)" if notes_exist else "-"
                
                content += f"| {num} | {name} | {code_link} | {notes_link} |\n"
        content += "\n"

    stats = f"目前已完成: **{total_count}** 题\n\n"
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header + stats + content)
    
    print(f"✅ 更新成功！日期：{today}，共计 {total_count} 题。")

if __name__ == "__main__":
    generate_readme()