# 游戏配置
GAME_WINDOW_TITLE = "星辰变"
GAME_PROCESS_NAME = "星辰变-2.0.0.55"

# 循环坐标点 (屏幕像素坐标)
ROUTE_POINTS = [
    (133, 51),    # 左上角
    (313, 149),   # 右上角
    (338, 324),   # 右下角
    (68, 270),    # 左下角
    (243, 201),   # 中心点
]

# 攻击配置
ATTACK_KEY = "1"
ATTACK_INTERVAL = 0.2  # 秒 (200ms)

# 拾取配置
PICKUP_KEY = "space"
PICKUP_DELAY = 0.5  # 拾取后等待时间

# 寻路配置
MOVE_TO_COORDINATE_DELAY = 0.5  # 点击坐标后的等待时间
ARRIVAL_CHECK_INTERVAL = 1.0  # 检查是否到达的间隔时间
MAX_WAIT_TIME = 30  # 最多等待30秒到达一个点

# 怪物检测配置
MONSTER_DETECTION_METHOD = "ocr"  # "ocr" 或 "memory"
MONSTER_CHECK_INTERVAL = 0.5  # 每0.5秒检查一次怪物

# OCR配置 (如果使用OCR方式)
MONSTER_NAME_KEYWORDS = ["深渊", "魔兽", "焰兽", "祸兽", "恐兽"]
OCR_CONFIDENCE_THRESHOLD = 0.6

# 热键配置
HOTKEY_START = "f5"  # 启动脚本
HOTKEY_STOP = "f6"   # 停止脚本

# 日志配置
ENABLE_LOGGING = True
LOG_FILE = "auto_hunt.log"
DEBUG_MODE = True