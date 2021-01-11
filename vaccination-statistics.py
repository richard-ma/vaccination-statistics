import numpy as np
import pandas as pd
from datetime import datetime


def press_any_key_to_exit(msg):
    input(msg)


file_name = './docs/武清区疫苗.xlsx'
sheet_name = '武清区'
default_engine = 'openpyxl'
data = pd.read_excel(file_name,
                     sheet_name=sheet_name,
                     engine=default_engine,
                     names=['district', 'name', 'type', 'status', 'check_date', 'new_id', 'description', 'fixed',
                            'fix_date'],
                     header=1)


# print(data['check_date'])

# 开始接种点数个
# 机构状态为“已开始接种”
def start_to_use(status):
    return status == "已开始接种"


counter_start_to_use = len(data.loc[data.status.apply(start_to_use)])


# print(counter_start_to_use)

def checked_today(check_date):
    return check_date == datetime.today().date()


def checked_before(check_date):
    return check_date < datetime.today().date()


def problem_fixed(fixed):
    return fixed == '是'


def problem_not_fixed(fixed):
    return fixed == '否'


def fixed_today(fix_date):
    return fix_date == datetime.today().date()


# 今天检查单位数个
# 检查日期为当日日期
counter_checked_today = len(data.loc[data.check_date.apply(checked_today)])


# print(counter_checked_today)


# 今日新发现问题数个
# 检查日期为当日日期
# 新序号不为0

def new_id_is_not_zero(new_id):
    return new_id != 0


counter_today_problem = len(data.loc[data.check_date.apply(checked_today)]. \
                            loc[data.new_id.apply(new_id_is_not_zero)])


# print(counter_today_problem)

# 今日整改数（今日新问题整改：个，今日老问题整改个）
# 今日新问题整改
# 是否整改状态为“是”
# 检查日期为当日日期
# 整改日期为当日日期


counter_fixed_today_problem = len(data.loc[data.fixed.apply(problem_fixed)]. \
                                  loc[data.check_date.apply(checked_today)]. \
                                  loc[data.fix_date.apply(fixed_today)])
# print(counter_fixed_today_problem)

# 今日老问题整改
# 是否整改状态为“是”
# 检查日期为之前日期
# 整改日期为当日日期


counter_fixed_previous_problem = len(data.loc[data.fixed.apply(problem_fixed)]. \
                                   loc[data.check_date.apply(checked_before)]. \
                                   loc[data.fix_date.apply(fixed_today)])
# print(counter_fixed_previous_problem)

# 今日新问题整改和老问题整改数量之和

counter_fixed_problem = counter_fixed_today_problem + counter_fixed_previous_problem
# print(counter_fixed_problem)

# 目前待整改问题数共计个
# 是否整改状态为“否”

counter_unfixed_problem = len(data.loc[data.fixed.apply(problem_not_fixed)])

# print(counter_unfixed_problem)

# 今日未开诊数个
# 机构状态为“适时启用”
def ready_to_use(status):
    return status == "适时启用"


counter_ready_to_use = len(data.loc[data.status.apply(ready_to_use)])
# print(counter_ready_to_use)

outline = ""
outline += "开始接种点数"+ str(counter_start_to_use) +"个" + "\n"
outline += "今天检查单位"+ str(counter_checked_today) +"个" + "\n"
outline += "今日新发现问题"+ str(counter_today_problem) +"个" + "\n"
outline += "今日整改"+ str(counter_fixed_problem) +"个 (今日新问题整改"+ str(counter_fixed_today_problem) +"个, 老问题整改"+ str(counter_fixed_previous_problem) +"个)" + "\n"
outline += "目前待整改问题"+ str(counter_unfixed_problem) +"个" + "\n"
outline += "今日未开诊"+ str(counter_ready_to_use) +"个" + "\n"

print(outline)

press_any_key_to_exit('按任意键退出...')