import os

def generate_readme():
    header = "# 🐍 小白摸鱼的 LeetCode 进化之路\n\n"
    solutions_dir = './solutions'
    
    if not os.path.exists(solutions_dir):
        os.makedirs(solutions_dir)

    total_count = 0
    content = ""

    # 1. 遍历第一层：题型分类文件夹 (如 01_数组_Array)
    categories = sorted([d for d in os.listdir(solutions_dir) if os.path.isdir(os.path.join(solutions_dir, d))])
    
    for cat in categories:
        cat_path = os.path.join(solutions_dir, cat)
        
        # 2. 遍历第二层：题目文件夹 (如 001_TwoSum)
        topics = sorted([d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))])
        
        if not topics:
            continue
            
        total_count += len(topics)
        
        # 写入题型标题
        content += f"### {cat}\n\n"
        content += "| 题号 | 题目名称 | 解法代码 | 笔记 |\n| :--- | :--- | :--- | :--- |\n"
        
        for folder in topics:
            if '_' in folder:
                num, name = folder.split('_', 1)
                
                # 定义代码和笔记的相对路径
                code_path = f"solutions/{cat}/{folder}/solution.py"
                notes_path = f"solutions/{cat}/{folder}/notes.md"
                
                # 检查文件是否存在，存在才给链接
                code_link = f"[Python 🐍]({code_path})" if os.path.exists(code_path) else "未上传"
                notes_link = f"[笔记 📝]({notes_path})" if os.path.exists(notes_path) else "-"
                
                content += f"| {num} | {name} | {code_link} | {notes_link} |\n"
        content += "\n"

    stats = f"目前已完成: **{total_count}** 题\n\n"
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(header + stats + content)
    
    print(f"✅ 成功更新！当前结构：题型分类文件夹 -> 题目文件夹。共计 {total_count} 题。")

if __name__ == "__main__":
    generate_readme()