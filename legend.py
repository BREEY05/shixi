legends={}
weapons={}
class legend:
    def add_legend(self,id,name,weapon_name):
        if id in legends:
            print(f"{id}编号已存在，请使用其他编号")
            return False
        legends[id]=name
        weapons[id]=weapon_name
        print(f"英雄{name}  编号:{id}已添加到英雄池")
        print(f"绑定武器:{weapon_name}")
        print(f"英雄池已更新")
        self.show_legend()
        return True

    def show_legend(self):
        if not legends:
            print("英雄池为空，还没有添加任何英雄")
        else:
            print("当前英雄池为:")
            for id, name in legends.items():#开始遍历了
                print(f"{id}. 英雄: {name}  武器: {weapons.get(id, '无')}")#更安全，不报错
    
    def modify_legend(self, id, new_name, new_weapon):
        if id not in legends:
            print(f"编号{id}不存在于英雄池中")
            return False
        old_name=legends[id]
        legends[id]=new_name
        weapons[id]=new_weapon
        print(f"英雄{old_name}  已修改为{new_name}")
        print(f"武器更新为:{new_weapon}")    
        print(f"英雄池已更新")
        self.show_legend()
        return True

    def delete_legend(self, id):
        if id in legends:  
            name = legends[id]
            del legends[id]  
            del weapons[id]
            print(f"已删除英雄{name}")
            print(f"英雄池已更新")
            self.show_legend()
        else:
            print(f"编号{id}不存在于英雄池中")

    def menu(self):
        print("1.查看英雄池")
        print("2.录入英雄信息")
        print("3.修改英雄信息")
        print("4.删除英雄信息")
        print("5.退出")

    def main(self):
      while True:
        self.menu()
        num=int(input("请输入您的选择(1-5):"))
        if num == 1:
            self.show_legend()
        elif num == 2:
            while True:
                id=int(input("请输入英雄编号:"))
                name=input("请输入英雄名称:")
                weapon_name=input("请输入兵器名称:")
                self.add_legend(id,name,weapon_name)
                QueRen=input("是否结束录入(是/否): ")
                if QueRen == '是':
                    break
        elif num == 3:  
            self.show_legend()
            id=int(input("请输入要修改的英雄编号:"))
            new_name=input("请输入新的英雄名称:")
            new_weapon=input("请输入新的武器名称:")
            self.modify_legend(id, new_name, new_weapon)
        elif num == 4:
            self.show_legend()
            id=int(input("请输入要删除的英雄编号:"))
            QueRen=input("确认删除这个英雄吗(是/否)?: ")
            if QueRen=="是":
                if id in legends:
                    self.delete_legend(id)
                else:
                    print(f"编号{id}不存在")
            else:
                print("取消删除")
        elif num == 5:
            print("感谢使用英雄管理系统")
            break
        else:
            print("输入错误，只能输入数字")
        input("\n(按回车键继续):")

if __name__=="__main__":
    print("----英雄管理系统-----")
    manager=legend()
    manager.main()
    



