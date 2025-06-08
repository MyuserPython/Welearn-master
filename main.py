import welearn_time
import welearn

print("**********  特别鸣谢 Avenshy & SSmJaE  **********")
print("                 Version:0.5dev\n")
print("**********   刷完成度此版本更新于Hhy       **********")
print("***************************************************\n")

print("********** Created By Avenshy & SSmJaE  **********")
print("                 刷时长Version:0.4dev")
print("         原作者github https://github.com/Avenshy")
print("         更新维护者github https://github.com/YZBRH/Welearn_helper/")
print("                              BR更新--2024.12.1")
print("***************************************************\n")


print("**********  Update By 冷柒残  **********")
print("            Version:0.5.0           ")
print("                              UPDATE--2025.5.29")
print("***************************************************\n")


if __name__ == '__main__':
    while True:
        selected = input("1.刷完成度正确度启动\n2.刷时长启动\n0.退出=>")
        if selected == "1":
            welearn.run_mode(selected)
        elif selected == "2":
            welearn_time.welearn_time_run()
        else:
            break